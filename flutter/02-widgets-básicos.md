# Nível 2. Widgets 

## Listas Dinâmicas com `ListView`

**Objetivo:** Criar uma lista rolável de itens usando o widget `ListView`.

**Código de Exemplo:**
```dart
// Importa o pacote Material Design do Flutter, que oferece uma variedade de widgets pré-construídos.
import 'package:flutter/material.dart';

// A função main é o ponto de entrada do aplicativo Flutter. 
// Ela executa o aplicativo criando uma instância da classe MyApp.
void main() => runApp(MyApp());

// MyApp é um widget sem estado que herda de StatelessWidget.
class MyApp extends StatelessWidget {
  @override
  // O método build é chamado para desenhar e construir o layout do widget MyApp.
  Widget build(BuildContext context) {
    // MaterialApp é um widget conveniente que inclui muitos widgets úteis por padrão.
    return MaterialApp(
      // Scaffold é um layout para a estrutura básica de um app de Material Design.
      home: Scaffold(
        // AppBar fornece uma barra de aplicativos na parte superior da tela.
        appBar: AppBar(
          // Text define o título exibido na AppBar.
          title: Text('Lista Dinâmica'),
        ),
        // O corpo do Scaffold está definido como uma instância do widget MyListView.
        body: MyListView(),
      ),
    );
  }
}

// MyListView é um widget sem estado para exibir uma lista dinâmica de itens.
class MyListView extends StatelessWidget {
  // Gera uma lista de strings. Cada string é prefixada com 'Item ' seguido de um número.
  final List<String> items = List<String>.generate(100, (i) => "Item $i");

  @override
  // Método build para desenhar o widget MyListView.
  Widget build(BuildContext context) {
    // ListView.builder cria uma lista rolável de widgets.
    return ListView.builder(
      // itemCount define o número total de itens na lista.
      itemCount: items.length,
      // itemBuilder é uma função chamada para cada item da lista. 
      // Ela retorna um widget que será usado para representar esse item.
      itemBuilder: (context, index) {
        // ListTile é um widget que representa um item de linha única em uma lista.
        return ListTile(
          // Text exibe o conteúdo de cada item da lista.
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
// Importa o pacote Material Design do Flutter, que oferece uma variedade de widgets pré-construídos.
import 'package:flutter/material.dart';

// Função principal, ponto de entrada para o aplicativo Flutter.
// runApp() inicia o aplicativo com o widget MyApp.
void main() => runApp(MyApp());

// MyApp é um widget sem estado que herda de StatelessWidget.
// StatelessWidget é uma classe base para widgets que não requerem estado.
class MyApp extends StatelessWidget {
  @override
  // O método build é chamado para desenhar e construir o layout do widget MyApp.
  Widget build(BuildContext context) {
    // MaterialApp é um widget que envolve vários widgets necessários para aplicativos que seguem o Material Design.
    return MaterialApp(
      // Scaffold fornece a estrutura básica do layout visual para a página.
      home: Scaffold(
        // AppBar fornece uma barra de aplicativos na parte superior da tela.
        appBar: AppBar(
          // Text define o título exibido na AppBar.
          title: Text('Stack e Positioned'),
        ),
        // O corpo do Scaffold é definido como uma instância do widget MyStack.
        body: MyStack(),
      ),
    );
  }
}

// MyStack é um widget sem estado para demonstrar o uso de Stack e Positioned.
class MyStack extends StatelessWidget {
  @override
  // Método build para desenhar o widget MyStack.
  Widget build(BuildContext context) {
    // Stack permite sobrepor widgets uns sobre os outros.
    return Stack(
      // Lista de widgets que serão empilhados.
      children: <Widget>[
        // Positioned é um widget que controla onde um filho de uma Stack é posicionado.
        Positioned(
          // Define a posição do canto superior esquerdo do widget.
          left: 50,
          top: 50,
          // Container é um widget que permite personalização visual, como cor e dimensão.
          child: Container(
            color: Colors.red,
            width: 100,
            height: 100,
          ),
        ),
        // Outro widget Positioned para posicionar um texto.
        Positioned(
          // Posiciona o widget no canto inferior direito da Stack.
          right: 50,
          bottom: 50,
          // Text exibe um texto simples.
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
// Importa o pacote Material Design do Flutter, que oferece uma variedade de widgets pré-construídos.
import 'package:flutter/material.dart';

// A função main é o ponto de entrada para o aplicativo Flutter.
// runApp inicia o aplicativo com o widget MyApp.
void main() => runApp(MyApp());

// MyApp é um widget sem estado que herda de StatelessWidget.
// StatelessWidget é usado para criar um widget que não requer um estado mutável.
class MyApp extends StatelessWidget {
  @override
  // O método build é chamado para desenhar e construir o layout do widget MyApp.
  Widget build(BuildContext context) {
    // MaterialApp é um widget que envolve vários widgets necessários para aplicativos que seguem o Material Design.
    return MaterialApp(
      // Scaffold fornece a estrutura básica do layout visual para a página.
      home: Scaffold(
        // AppBar fornece uma barra de aplicativos na parte superior da tela.
        appBar: AppBar(
          // Text define o título exibido na AppBar.
          title: Text('Grade de Imagens'),
        ),
        // O corpo do Scaffold é definido como uma instância do widget MyGridView.
        body: MyGridView(),
      ),
    );
  }
}

// MyGridView é um widget sem estado que cria uma grade de itens.
class MyGridView extends StatelessWidget {
  @override
  // Método build para desenhar o widget MyGridView.
  Widget build(BuildContext context) {
    // GridView.count cria uma grade com um número fixo de colunas.
    return GridView.count(
      // Define o número de colunas transversais na grade.
      crossAxisCount: 3,
      // Cria uma lista de widgets para os itens da grade.
      children: List.generate(20, (index) {
        // Retorna um container para cada item.
        return Container(
          // Um Card é usado para adicionar um efeito visual a cada item.
          child: Card(
            // Define a cor do Card.
            color: Colors.blueAccent,
            // Center é usado para centralizar o conteúdo dentro do Card.
            child: Center(
              // Text exibe um texto com o índice do item.
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