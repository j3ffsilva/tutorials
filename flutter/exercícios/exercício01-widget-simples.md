# Exercicío 1: Desenvolvendo um Catálogo de Produtos Simples com Flutter

## Objetivo

Criar um aplicativo Flutter que exibe um catálogo de produtos em uma lista dinâmica, utilizando widgets básicos e conceitos de listas roláveis
.
## Descrição 

1. **Estrutura Básica do Aplicativo:**
   - Inicie seu aplicativo Flutter importando o pacote Material Design.
   - Defina a função `main` para iniciar o aplicativo com uma instância da classe `CatalogApp`.

2. **Criação do Widget Principal (`CatalogApp`):**
   - Crie um widget sem estado `CatalogApp`, herdando de `StatelessWidget`, similar ao widget `MyApp` no exemplo fornecido.
   - No método `build` de `CatalogApp`, retorne um `MaterialApp` contendo um `Scaffold` com um `AppBar` tendo o título 'Catálogo de Produtos'.

3. **Implementação da Lista de Produtos (`ProductList`):**
   - Crie um widget sem estado chamado `ProductList`.
   - Gere uma lista de strings representando produtos (por exemplo, `Produto 1`, `Produto 2`, etc.), de maneira similar à lista de itens no código de exemplo.
   - Utilize um `ListView.builder` para exibir a lista dinâmica de produtos, onde cada produto é representado por um `ListTile` contendo apenas um título.


## Solução

<!-- Clique aqui para ver a solução 

```dart
import 'package:flutter/material.dart';

void main() => runApp(CatalogApp());

class CatalogApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Catálogo de Produtos'),
        ),
        body: ProductList(),
      ),
    );
  }
}

class ProductList extends StatelessWidget {
  final List<String> products = List<String>.generate(100, (i) => "Produto $i");

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: products.length,
      itemBuilder: (context, index) {
        return ListTile(
          title: Text(products[index]),
        );
      },
    );
  }
}
```

-->