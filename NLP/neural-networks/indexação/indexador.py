from nltk.tokenize import word_tokenize
from nltk import FreqDist

class Indexador:
    def __init__(self, frases):
        self.__vocabulario = None
        self.__mapa_palavras = None
        self.__mapa_codigos = None
        self.__freq_palavras = None
        self.__indexar(frases)

    def __indexar(self, frases):
        todos_tokens = []

        # Tokenização de cada frase e armazenamento dos tokens
        for frase in frases:
            tokens = word_tokenize(frase, language="portuguese")
            todos_tokens.extend(tokens)

        # Cálculo da frequência de cada token
        self.__freq_palavras = FreqDist(todos_tokens)

        # Criação do vocabulário
        self.__vocabulario = list(self.__freq_palavras.keys())

        # Atribuição de um número único para cada token com deslocamento
        self.__mapa_palavras = {palavra: indice+1 for indice, palavra in enumerate(self.__vocabulario)}

        m = self.__mapa_palavras
        self.__mapa_codigos = {m[key]: key for key in m.keys()}

    def codificar(self, frase):
        m = self.__mapa_palavras
        return [m[k] for k in m.keys()]

    def decodificar(self, codigos):
        m = self.__mapa_codigos
        return [m[k] for k in m.keys()]

    def vocabulario(self):
        return self.__vocabulario

    def mapa_palavras(self):
        return self.__mapa_palavras

    def mapa_codigos(self):
        return self.__mapa_codigos
