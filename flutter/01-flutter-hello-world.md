# Nível 1: Um Widget Simples

**Tópico:** Criação de um Widget Simples no Flutter

**Explicação:**
Flutter utiliza widgets para criar a interface do usuário. Um widget básico no Flutter pode ser um texto ou um botão. Vamos criar um widget de texto simples.

**Código de Exemplo:**
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Hello Flutter World'),
        ),
        body: Center(
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
6. **Corpo do Scaffold:** Contém um widget `Center` que centraliza o widget filho, neste caso, um `Text` com o conteúdo "Olá, Flutter!".

