# Programação Assíncrona em Dart

## 1. `Future`

Um `Future` em Dart é um objeto que representa um resultado que será obtido em algum momento no futuro, geralmente como resultado de uma operação assíncrona. Ele permite que o programa continue a execução sem bloquear enquanto espera por esse resultado. Quando a operação assíncrona é concluída, o `Future` é "completado" com um valor (o resultado da operação) ou um erro. É uma parte fundamental do manejo de tarefas assíncronas em Dart, permitindo que operações como chamadas de rede, leitura de arquivos, ou qualquer outra tarefa que leve tempo para ser concluída, sejam gerenciadas de forma eficiente e não bloqueante.

### 1.1. Exemplo Simples de Future

- **Objetivo**: Mostrar como criar um Future simples em Dart.

  ```dart
  Future<String> getMessage() {
    return Future.delayed(Duration(seconds: 2), () => "Olá, Mundo Assíncrono!");
  }
  ```

`Future.delayed` cria um atraso de 2 segundos antes de retornar a mensagem.

### 1.2. Acessando o Resultado de um Future

- **Uso do `async` e `await`**:

  ```dart
  void showFutureResult() async {
    String message = await getMessage();
    print(message);
  }

  showFutureResult(); // Chamada da função
  ```

  - `await` aguarda o resultado do Future, e `async` indica que a função pode ter operações assíncronas.

## 2. Trabalhando com Erros em Futures

### 2.1. Capturando Erros

- **Exemplo com Try-Catch**:

  ```dart
  Future<String> getError() {
    return Future.delayed(Duration(seconds: 2), () => throw "Erro simulado!");
  }

  Future<void> handleFutureError() async {
    try {
      String result = await getError();
    } catch (e) {
      print("Capturado um erro: $e");
    }
  }

  handleFutureError(); // Chamada da função
  ```

## 3. Introdução a Streams

### 3.1. Criando e Usando Streams

- **Exemplo de Stream**:

  ```dart
  Stream<int> numberStream() async* {
    for (int i = 1; i <= 5; i++) {
      await Future.delayed(Duration(seconds: 1));
      yield i;
    }
  }

  void printStream() async {
    await for (int number in numberStream()) {
      print(number);
    }
  }

  printStream(); // Chamada da função
  ```

  - `yield` é usado para enviar valores de volta um a um.