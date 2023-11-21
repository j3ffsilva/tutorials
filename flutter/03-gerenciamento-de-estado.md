# Nível 3: Gerenciamento de Estado

## 1. `setState`

**Tópico:** Introdução ao Gerenciamento de Estado

**Objetivo:** Entender o conceito básico de estado e como ele é gerenciado em Flutter.

**Código de Exemplo:**
```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String text = "Estado inicial";

  void _updateText() {
    setState(() {
      text = "Estado alterado";
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Gerenciamento de Estado Básico"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(text),
            ElevatedButton(
              onPressed: _updateText,
              child: Text('Alterar Texto'),
            )
          ],
        ),
      ),
    );
  }
}
```

**Explicação do Código:**
- `MyHomePage` é um `StatefulWidget` que permite a alteração do seu estado.
- `_MyHomePageState` mantém o estado do texto.
- `setState` é chamado dentro de `_updateText`, que atualiza o texto e sinaliza a reconstrução do widget.


## 2. Gerenciamento de Estado Local com `StatefulWidget`

**Tópico:** Uso de `StatefulWidget` para Gerenciamento de Estado Local

**Objetivo:** Aprender a usar `StatefulWidget` para gerenciar o estado local de um widget.

**Código de Exemplo:**
```dart
// Importa o pacote Material Design do Flutter, que oferece uma variedade de widgets pré-construídos.
import 'package:flutter/material.dart';

// Função principal, ponto de entrada para o aplicativo Flutter.
// runApp() inicia o aplicativo com o widget MyApp.
void main() => runApp(MyApp());

// MyApp é um widget sem estado que herda de StatelessWidget.
// StatelessWidget é uma classe base para widgets que não precisam de estado interno.
class MyApp extends StatelessWidget {
  @override
  // Método build que desenha o widget MyApp.
  Widget build(BuildContext context) {
    // MaterialApp é um widget que envolve vários widgets necessários para aplicativos que seguem o Material Design.
    return MaterialApp(
      // Define a tela inicial do aplicativo para MyHomePage.
      home: MyHomePage(),
    );
  }
}

// MyHomePage é um widget com estado que herda de StatefulWidget.
// StatefulWidget é usado para criar widgets que mantêm um estado mutável.
class MyHomePage extends StatefulWidget {
  @override
  // Cria o estado associado ao MyHomePage.
  _MyHomePageState createState() => _MyHomePageState();
}

// _MyHomePageState é a classe que contém o estado para MyHomePage.
class _MyHomePageState extends State<MyHomePage> {
  // String para armazenar o texto exibido na tela.
  String text = "Estado inicial";

  // Método para atualizar o texto e o estado do widget.
  void _updateText() {
    setState(() {
      // Atualiza o texto e marca o widget para reconstrução.
      text = "Estado alterado";
    });
  }

  @override
  // Método build que desenha o estado atual do widget MyHomePage.
  Widget build(BuildContext context) {
    // Scaffold fornece a estrutura básica do layout visual para a página.
    return Scaffold(
      // AppBar fornece uma barra de aplicativos na parte superior da tela.
      appBar: AppBar(
        // Text define o título exibido na AppBar.
        title: Text("Gerenciamento de Estado Básico"),
      ),
      // Corpo centralizado do Scaffold.
      body: Center(
        // Column organiza seus filhos verticalmente.
        child: Column(
          // Alinha os filhos no centro da coluna.
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            // Exibe o texto que muda de acordo com o estado.
            Text(text),
            // ElevatedButton é um botão estilizado que, quando pressionado, chama _updateText.
            ElevatedButton(
              // Define a ação a ser executada quando o botão é pressionado.
              onPressed: _updateText,
              // Texto exibido no botão.
              child: Text('Alterar Texto'),
            )
          ],
        ),
      ),
    );
  }
}

```

**Explicação do Código:**
- `CounterPage` é um `StatefulWidget` que gerencia um contador.
- `_CounterPageState` mantém e atualiza o valor do contador.
- O método `_incrementCounter` incrementa o contador e chama `setState` para atualizar a interface.