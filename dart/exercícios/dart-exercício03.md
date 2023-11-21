# Exercício 3: Herança

Crie uma classe `Animal` com um método `emitirSom`. Depois, crie uma classe `Cachorro` que herda de `Animal` e sobrescreve o método `emitirSom`.

# Solução

Clique em `raw` para ver a solução.

<!--
```dart
class Animal {
  void emitirSom() {
    print('Som do animal');
  }
}

class Cachorro extends Animal {
  @override
  void emitirSom() {
    print('Au au');
  }
}

void main() {
  var dog = Cachorro();
  dog.emitirSom();  // Saída: Au au
}
```
-->