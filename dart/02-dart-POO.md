# Programação Orientada a Objetos em Dart

## Introdução

A programação orientada a objetos (POO) é fundamental em Dart, principalmente por sua compatibilidade com o Flutter, um framework amplamente usado para desenvolvimento móvel e web. A POO em Dart promove a reutilização de código, organização, e manutenibilidade, tornando o desenvolvimento mais eficiente e escalável. Ela permite encapsulamento de dados, garantindo segurança e facilitando a manutenção, enquanto o polimorfismo oferece flexibilidade. Além disso, a POO suporta a implementação de padrões de design e boas práticas, essenciais para aplicações robustas e colaboração efetiva em equipe.

## 1. Conceitos Básicos

### 1.1 Classes e Objetos

Exemplo em Dart.

```dart
class Carro {
  String marca;
  void acelerar() {
    // código para acelerar
  }
}
void main() {
  Carro meuCarro = new Carro();
  meuCarro.marca = 'Toyota';
  meuCarro.acelerar();
}
```

### 1.2 Encapsulamento

Exemplo em Dart.

```dart
class ContaBancaria {
  double _saldo;  // Variável privada
  double get saldo => _saldo;
  set deposito(double valor) {
    if (valor > 0) _saldo += valor;
  }
}
```

## 2. Herança

Exemplo em Dart.

```dart
class Veiculo {
  void mover() {
    // código genérico para mover
  }
}
class Carro extends Veiculo {
  @override
  void mover() {
    // implementação específica para carro
  }
}
```

## 3. Polimorfismo

Exemplo em Dart.

```dart
class Animal {
  void fazerSom() {
    // som genérico do animal
  }
}
class Cachorro extends Animal {
  @override
  void fazerSom() {
    print('Au au');
  }
}
```

## 4. Interfaces e Classes Abstratas

Exemplo em Dart.

```dart
abstract class OperacaoMatematica {
  double operar(double a, double b);
}
class Soma implements OperacaoMatematica {
  @override
  double operar(double a, double b) => a + b;
}
```