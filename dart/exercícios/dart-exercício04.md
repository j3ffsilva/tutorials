# Exercício 4: Polimorfismo

Crie uma interface `Forma` com um método `calcularArea`. Implemente esta interface em duas classes: `Quadrado` e `Circulo`.

# Solução

Clique em `raw` para ver a solução.

<!--
```dart
abstract class Forma {
  double calcularArea();
}

class Quadrado implements Forma {
  double lado;

  Quadrado(this.lado);

  @override
  double calcularArea() => lado * lado;
}

class Circulo implements Forma {
  double raio;

  Circulo(this.raio);

  @override
  double calcularArea() => 3.14 * raio * raio;
}

void main() {
  var quadrado = Quadrado(4);
  var circulo = Circulo(3);
  print('Área do quadrado: ${quadrado.calcularArea()}');
  print('Área do círculo: ${circulo.calcularArea()}');
}
```
-->