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
            RaisedButton(
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
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: CounterPage(),
    );
  }
}

class CounterPage extends StatefulWidget {
  @override
  _CounterPageState createState() => _CounterPageState();
}

class _CounterPageState extends State<CounterPage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Contador"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('Você pressionou o botão $_counter vezes.'),
            RaisedButton(
              onPressed: _incrementCounter,
              child: Text('Incrementar'),
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



## 3. Gerenciamento de Estado com `Provider`

**Tópico:** Gerenciamento de Estado com Provider

**Objetivo:** Utilizar o Provider para gerenciar e acessar o estado através da árvore de widgets.

**Código de Exemplo:**
```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => ThemeModel(),
      child: Consumer<ThemeModel>(
        builder: (context, theme, child) => MaterialApp(
          theme: ThemeData(
            primarySwatch: theme.currentTheme ? Colors.blue : Colors.red,
          ),
          home: HomePage(),
        ),
      ),
    );
  }
}

class ThemeModel extends ChangeNotifier {
  bool _isBlueTheme = true;

  bool get currentTheme => _isBlueTheme;

  void toggleTheme() {
    _isBlueTheme = !_isBlueTheme;
    notifyListeners();
  }
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Provider Theme Example"),
      ),
      body: Center(
        child: Text("Toque no botão para mudar o tema"),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => Provider






        of(context, listen: false).toggleTheme(),
        child: Icon(Icons.color_lens),
      ),
    );
  }
}
```

**Explicação do Código:**
- `ChangeNotifierProvider` cria uma instância de `ThemeModel`, disponibilizando-a para seus descendentes.
- `ThemeModel` é uma classe que estende `ChangeNotifier` e gerencia o estado do tema.
- `Consumer<ThemeModel>` reconstrói seus filhos quando `ThemeModel` notifica ouvintes sobre mudanças.
- O botão na tela chama `toggleTheme`, que alterna o tema e notifica os ouvintes para reconstruir a interface.

---

## 4. Gerenciamento de Estado com Riverpod

**Tópico:** Gerenciamento de Estado com Riverpod

**Objetivo:** Implementar gerenciamento de estado com Riverpod, uma abordagem moderna e flexível.

**Código de Exemplo:**
```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

void main() => runApp(ProviderScope(child: MyApp()));

class MyApp extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final counter = ref.watch(counterProvider);
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("Riverpod Counter Example"),
        ),
        body: Center(
          child: Text('Valor do contador: $counter'),
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () => ref.read(counterProvider.notifier).state++,
          child: Icon(Icons.add),
        ),
      ),
    );
  }
}

final counterProvider = StateProvider((ref) => 0);
```

**Explicação do Código:**
- `ProviderScope` envolve `MyApp` para fornecer escopo para os providers.
- `counterProvider` é um `StateProvider` que gerencia o estado do contador.
- `ConsumerWidget` permite a leitura do estado atual e a reação às mudanças.
- O botão incrementa o contador através de `ref.read`.


## 5. Explorando o Gerenciamento de Estado com GetX

**Tópico:** Gerenciamento de Estado com GetX

**Objetivo:** Construir uma pequena aplicação com navegação e estado compartilhado usando GetX.

**Código de Exemplo:**
```dart
import 'package:flutter/material.dart';
import 'package:get/get.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return GetMaterialApp(
      home: HomePage(),
    );
  }
}

class Controller extends GetxController {
  var count = 0.obs;
  increment() => count++;
}

class HomePage extends StatelessWidget {
  final Controller c = Get.put(Controller());

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("GetX Example")),
      body: Center(
        child: Obx(() => Text("Clicks: ${c.count}")),
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: c.increment,
      ),
    );
  }
}
```

**Explicação do Código:**
- `GetMaterialApp` é usado em vez de `MaterialApp` para facilitar a navegação e o gerenciamento de estado com GetX.
- `Controller` é uma classe que estende `GetxController`, gerenciando o estado do contador.
- `count` é uma variável reativa. Ao ser alterada, todos



os widgets que a observam são reconstruídos.
- `Obx` é usado para criar um widget reativo que será reconstruído sempre que `count` mudar.
- O botão chama `increment` no controlador, atualizando o valor de `count` e, consequentemente, o texto exibido.