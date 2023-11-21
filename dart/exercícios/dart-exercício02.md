# Exercício 2: Encapsulamento

Modifique a classe `ContaBancaria` para incluir um método que permita depósitos, mas impeça valores negativos.

# Solução

Clique em `raw` para ver a solução.

<!--
```dart
class ContaBancaria {
  double _saldo = 0;

  void depositar(double valor) {
    if (valor > 0) {
      _saldo += valor;
      print('Depósito realizado: $valor');
    } else {
      print('Valor inválido para depósito');
    }
  }

  double get saldo => _saldo;
}

void main() {
  var minhaConta = ContaBancaria();
  minhaConta.depositar(100);
  print('Saldo: ${minhaConta.saldo}');
}
```
-->