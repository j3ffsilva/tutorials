# Exercício 2: Manipulando Estados em Flutter

## Objetivo 

Desenvolver um aplicativo Flutter que demonstre o gerenciamento básico de estados, inspirando-se no exemplo fornecido.

## Descrição

1. **Estrutura Básica do Aplicativo:**
   - Crie um aplicativo Flutter iniciando com a função `main` e um widget principal chamado `StateDemoApp`, similar ao `MyApp` no exemplo.
   - O widget `StateDemoApp` deve retornar um `MaterialApp` que contém um widget `StateDemoHomePage` como sua home.

2. **Widget de Página com Estado (`StateDemoHomePage`):**
   - Defina `StateDemoHomePage` como um widget com estado, utilizando `StatefulWidget`.
   - Crie uma classe de estado, por exemplo, `_StateDemoHomePageState`, que estende `State<StateDemoHomePage>`.

3. **Gerenciamento de Estado:**
   - No estado de `StateDemoHomePage`, defina uma variável para armazenar um texto, semelhante ao `text` no exemplo.
   - Implemente um método para alterar o valor desta variável. Este método deve chamar `setState` para atualizar a interface do usuário quando o estado é alterado.

4. **Interface do Usuário:**
   - Construa a interface do usuário no método `build` do estado de `StateDemoHomePage`.
   - Inclua um `AppBar` com um título relevante, como "Exemplo de Estado Flutter".
   - Use um `Column` no corpo para organizar os widgets, incluindo um widget `Text` que exibe o texto armazenado na variável de estado.
   - Adicione um `ElevatedButton` que, quando pressionado, aciona a alteração do texto, demonstrando a mudança de estado.


## Solução

*Acesse a versão `raw` deste arquivo para ver a solução*

<!-- 
import 'package:flutter/material.dart';

void main() => runApp(StateDemoApp());

class StateDemoApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: StateDemoHomePage(),
    );
  }
}

class StateDemoHomePage extends StatefulWidget {
  @override
  _StateDemoHomePageState createState() => _StateDemoHomePageState();
}

class _StateDemoHomePageState extends State<StateDemoHomePage> {
  String text = "Texto Inicial";

  void _changeText() {
    setState(() {
      text = "Texto Alterado";
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Exemplo de Estado Flutter"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(text),
            ElevatedButton(
              onPressed: _changeText,
              child: Text('Mudar Texto'),
            )
          ],
        ),
      ),
    );
  }
}
-->