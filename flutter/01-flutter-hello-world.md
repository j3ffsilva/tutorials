# Nível 1: Um Widget Simples

**Tópico:** Criação de um Widget Simples no Flutter

**Explicação:**
Flutter utiliza widgets para criar a interface do usuário. Um widget básico no Flutter pode ser um texto ou um botão. Vamos criar um widget de texto simples.

**Código de Exemplo:**
```dart
// Importa o pacote do Material Design, que fornece widgets e outras ferramentas para a criação de UIs.
import 'package:flutter/material.dart';

// Função principal do aplicativo, onde a execução começa.
void main() {
  // Executa o aplicativo criando uma instância da classe MyApp.
  runApp(MyApp());
}

// Define a classe MyApp, que é um widget sem estado (stateless).
class MyApp extends StatelessWidget {
  // Sobrescreve o método build, que descreve como o UI do widget será construído.
  @override
  Widget build(BuildContext context) {
    // Retorna um MaterialApp, que é um widget que envolve uma série de widgets que implementam o design do Material.
    return MaterialApp(
      // Define o título do aplicativo, usado na barra de tarefas, entre outros.
      title: 'Flutter Demo',
      // Define a tela inicial do aplicativo.
      home: Scaffold(
        // Cria uma AppBar (barra de aplicativos) com um título.
        appBar: AppBar(
          title: Text('Hello Flutter World'),
        ),
        // Define o corpo da tela inicial como um widget Center, que centraliza seu filho.
        body: Center(
          // Cria um widget Text, que exibe um texto simples.
          child: Text('Hello, Flutter!'),
        ),
      ),
    );
  }
}
```

**Explicação do Código:**
1. **Importação do pacote Flutter Material:** Fornece os elementos visuais básicos.
2. **Função main:** Ponto de entrada do aplicativo Flutter.
3. **MyApp class:** Um widget sem estado que cria um MaterialApp.
4. **MaterialApp:** Define o título e a estrutura básica do app.
5. **Scaffold:** Fornece a estrutura visual, incluindo a AppBar (barra superior) e o corpo.
6. **Corpo do Scaffold:** Contém um widget `Center` que centraliza o widget filho, neste caso, um `Text` com o conteúdo "Hello, Flutter!".

