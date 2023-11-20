# Nível 2. Widgets 

## Listas Dinâmicas com `ListView`

**Objetivo:** Criar uma lista rolável de itens usando o widget `ListView`.

**Código de Exemplo:**
```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Lista Dinâmica'),
        ),
        body: MyListView(),
      ),
    );
  }
}

class MyListView extends StatelessWidget {
  final List<String> items = List<String>.generate(100, (i) => "Item $i");

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: items.length,
      itemBuilder: (context, index) {
        return ListTile(
          title: Text(items[index]),
        );
      },
    );
  }
}
```

**Explicação:**
- `ListView.builder` cria uma lista de itens rolável. 
- `itemCount` define o número total de itens na lista.
- `itemBuilder` é uma função que constrói cada item da lista.

## 2. Sobreposição com`Stack` e Posicionamento com `Positioned`

**Objetivo:** Sobrepor widgets utilizando `Stack` e posicionar elementos com `Positioned`.

**Código de Exemplo:**
```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Stack e Positioned'),
        ),
        body: MyStack(),
      ),
    );
  }
}

class MyStack extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Stack(
      children: <Widget>[
        Positioned(
          left: 50,
          top: 50,
          child: Container(
            color: Colors.red,
            width: 100,
            height: 100,
          ),
        ),
        Positioned(
          right: 50,
          bottom: 50,
          child: Text('Texto Sobreposto'),
        )
      ],
    );
  }
}
```

**Explicação:**
- `Stack` permite a sobreposição de widgets.
- `Positioned` é usado para posicionar os elementos dentro do `Stack`.


## 3. Layouts de Grade com `GridView`

**Objetivo:** Criar um layout de grade com várias imagens ou elementos usando `GridView`.

**Código de Exemplo:**
```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Grade de Imagens'),
        ),
        body: MyGridView(),
      ),
    );
  }
}

class MyGridView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return GridView.count(
      crossAxisCount: 3,
      children: List.generate(20, (index) {
        return Container(
          child: Card(
            color: Colors.blueAccent,
            child: Center(
              child: Text('Item $index'),
            ),
          ),
        );
      }),
    );
  }
}
```

**Explicação:**
- `GridView.count` permite criar um layout de grade com um número fixo de colunas (`crossAxisCount`).
- `List.generate` cria uma lista de widgets que são exibidos na grade.