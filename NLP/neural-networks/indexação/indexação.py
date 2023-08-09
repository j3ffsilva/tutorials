# Bibliotecas
#===============================================================================
import pandas as pd
from indexador import Indexador

from tqdm import tqdm

import nltk
from nltk.tokenize import word_tokenize

from sklearn.model_selection import train_test_split

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

# Ingestão
#===============================================================================
print("Ingestão")
df = pd.read_csv('./meus-dados-UTF8.csv', sep=';')

df['sentimento'] = df['sentimento'].map({'POSITIVE': 0, 'NEUTRAL': 1, 'NEGATIVE': 2})

frases = list(df['texto'])
rotulos = list(df['sentimento'])

# Preparação dos dados
#===============================================================================
print("Divide em treino e teste")
# Divide o dataset em treino e teste
train_frases, test_frases, train_rotulos, test_rotulos = \
    train_test_split(frases, rotulos, random_state=42, test_size=0.3, stratify=rotulos)

# DataLoaders
#===============================================================================
class DatasetSentimento(Dataset):
    def __init__(self, frases, rotulos, indexador, max_length=None):
        self.frases = frases
        self.rotulos = rotulos
        self.indexador = indexador
        self.max_length = max_length

    def __len__(self):
        return len(self.frases)

    def __getitem__(self, idx):
        frase = self.frases[idx]
        rotulo = self.rotulos[idx]

        # Aqui truncamos a frase se ela exceder o max_length
        if self.max_length is not None and len(frase) > self.max_length:
            frase = frase[:self.max_length]

        codificada = indexador.codificar(frase)
        codificada_tensor = torch.tensor(codificada)
        return codificada_tensor, rotulo

class ClassificadorSentimento(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(ClassificadorSentimento, self).__init__()

        self.embedding = nn.Embedding(input_size, hidden_size)
        self.lstm = nn.LSTM(hidden_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        embedded = self.embedding(x)
        output, _ = self.lstm(embedded)
        output = self.fc(output[:, -1, :])
        return output

# Função de treinamento
#===============================================================================
def train(model, train_loader, criterion, optimizer, device):
    model.train()
    total_loss = 0
    for inputs, labels in tqdm(train_loader):
        inputs = inputs.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    return total_loss / len(train_loader)

# Função de avaliação
#===============================================================================
def evaluate(model, test_loader, criterion, device):
    model.eval()
    total_loss = 0
    correct = 0
    total = 0

    with torch.no_grad():
        for inputs, labels in tqdm(test_loader):
            inputs = inputs.to(device)
            labels = labels.to(device)

            outputs = model(inputs)
            loss = criterion(outputs, labels)
            total_loss += loss.item()

            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = correct / total
    return total_loss / len(test_loader), accuracy


# Parâmetros
#===============================================================================
print("Criando um índice para cada palavra")
indexador = Indexador(frases)

# Parâmetros
#===============================================================================
VOCAB_SIZE = len(indexador.vocabulario()) + 1
HIDDEN_SIZE = 128
N_CLASSES = 3
BATCH_SIZE = 8
learning_rate = 0.001
MAX_LENGTH = 1000

train_dataset = DatasetSentimento(train_frases, train_rotulos, indexador, max_length=MAX_LENGTH)
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)

test_dataset = DatasetSentimento(test_frases, test_rotulos, indexador)
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=True)

# Instanciar o modelo
#===============================================================================
print("Instancia o modelo")
model = ClassificadorSentimento(VOCAB_SIZE, HIDDEN_SIZE, N_CLASSES)

# Definir função de perda e otimizador
#===============================================================================
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Verificar se a GPU está disponível
#===============================================================================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"device: {device}")
model.to(device)


N_EPOCHS = 10
# Treinamento do modelo
#===============================================================================
print("Inicia o treinamento")
for epoch in range(N_EPOCHS):
    print(f"# Epoch: {epoch+1}")
    print("-" * 80)
    train_loss = train(model, train_loader, criterion, optimizer, device)
    test_loss, test_accuracy = evaluate(model, test_loader, criterion, device)

    print(f"Epoch {epoch+1}/{N_EPOCHS}:")
    print(f"Train Loss: {train_loss:.4f}")
    print(f"Test Loss: {test_loss:.4f}")
    print(f"Test Accuracy: {test_accuracy:.4f}")
    print()

# Salva o modelo inteiro
torch.save(model, 'model.pt')
