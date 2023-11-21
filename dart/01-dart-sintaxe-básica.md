# Primeiros passos com o Dart

## Introdução

Dart é uma linguagem de programação moderna e orientada a objetos, desenvolvida pelo Google, usada principalmente para a criação de aplicativos móveis e web. Este guia apresenta os conceitos básicos da linguagem Dart para iniciantes.

## Sintaxe Básica

### Estrutura de um Programa Dart

Todo programa Dart começa com a função `main()`, que é o ponto de entrada do programa.

```dart
void main() {
  print('Olá, Dart!');
}
```

### Declaração de Variáveis

Em Dart, você pode declarar variáveis usando os tipos de dados ou a palavra-chave `var` quando o tipo é inferido automaticamente. Por exemplo:

```dart
String nome = "Alice";
var idade = 30;
```

### Tipos de Dados

Os tipos de dados mais comuns em Dart são:

- `int` para números inteiros.
- `double` para números de ponto flutuante.
- `String` para textos.
- `bool` para valores booleanos (true/false).

### Operadores

Dart suporta vários operadores:

- Operadores aritméticos: `+`, `-`, `*`, `/`, `%`
- Operadores de comparação: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Operadores lógicos: `&&`, `||`, `!`

### Estruturas de Controle de Fluxo

Estruturas de controle de fluxo ajudam a controlar o fluxo do programa. Dart inclui `if`, `else`, loops `for` e `while`.

#### Exemplo de `if`:

```dart
var numero = 10;
if (numero > 0) {
  print('Número é positivo');
} else {
  print('Número é negativo ou zero');
}
```

#### Exemplo de loop `for`:

```dart
for (var i = 0; i < 5; i++) {
  print('Valor de i: $i');
}
```

### Funções

Funções são blocos de código que realizam uma tarefa específica.

```dart
void cumprimentar(String nome) {
  print('Olá, $nome!');
}

main() {
  cumprimentar('Alice');
}
```