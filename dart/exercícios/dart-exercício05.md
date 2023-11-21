# Exercício 5: Classes Abstratas

Crie uma classe abstrata `Veiculo` com um método abstrato `mover`. Implemente esta classe em duas subclasses: `Carro` e `Bicicleta`, fornecendo implementações para o método `mover`.

# Solução

Clique em `raw` para ver a solução.

<!--
```dart
abstract class Veiculo {
  void mover();
}

class Carro extends Veiculo {
  @override
  void mover() {
    print('Carro se movendo');
  }
}

class Bicicleta extends Veiculo {
  @override
  void mover() {
    print('Bicicleta se movendo');
  }
}

void main() {
  var carro = Carro();
  var bicicleta = Bicicleta();
  carro.mover();  // Saída: Carro se movendo
  bicicleta.mover();  // Saída: Bicicleta se movendo
}
```
-->