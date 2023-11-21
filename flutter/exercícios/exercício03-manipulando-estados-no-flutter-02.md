# Exercicío 3: Alternância de Textos com Estado em Flutter

## Objetivo
Aprender a manipular o estado interno de um widget em Flutter para alternar entre diferentes textos em resposta à interação do usuário.

## Descrição
Desenvolva um aplicativo Flutter que contenha um widget principal (`MainScreen`). Esse widget deve exibir um texto inicial (por exemplo, "Texto A") e um botão. Quando o botão é pressionado, o texto deve alternar entre "Texto A" e "Texto B". O aplicativo deve utilizar um `StatefulWidget` para gerenciar essa mudança de estado, similar ao exemplo fornecido, demonstrando a funcionalidade do `setState`.

## Solução

*Acesse a versão `raw` deste arquivo para ver a solução*

<!--  
```dart
import 'package:flutter/material.dart';

void main() => runApp(TextToggleApp());

class TextToggleApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MainScreen(),
    );
  }
}

class MainScreen extends StatefulWidget {
  @override
  _MainScreenState createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  bool isTextA = true;

  void _toggleText() {
    setState(() {
      isTextA = !isTextA;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Alternância de Textos"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(isTextA ? 'Texto A' : 'Texto B'),
            ElevatedButton(
              onPressed: _toggleText,
              child: Text('Alterar Texto'),
            ),
          ],
        ),
      ),
    );
  }
}
```
-->