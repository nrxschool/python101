# REST (Representational State Transfer)

- Orientado a CRUD - Create, Read, Update, Delete.
- Baseado em HTTP/1.1
- Baseado em recursos, representados por URLs, e verbos HTTP (GET, POST, PUT, DELETE).
- REST utiliza URLs para representar recursos.

EXEMPLO

```js
// Buscar informações sobre tênis femininos, tamanho 36
GET meusite.com/tenis/feminino/36

// Adicionar um novo produto
POST meusite.com/adicionar-produto/ {"produto": "tenis nike"}

// Atualizar informações de um produto existente.
PUT meusite.com/atualizar-produto/
```

PROS/CONTRAS

- ✅ Flexibilidade e simplicidade de uso: pode usar JSON, XML, etc.
- ✅ Amplamente adotado e bem documentado.
- 🚨 Não oferece um contrato de dados rígido, o que pode levar a inconsistências.
- 🚨 Tudo ou nada: não permite solicitar ou enviar apenas parte dos dados de um recurso.

# gRPC (Google Remote Procedure Call)

- Focado em chamadas de procedimento remoto.
- Baseado em HTTP/2, que permite comunicação bidirecional e mais eficiente.
- Usa Protocol Buffers como mecanismo de serialização de dados, que é mais eficiente que o JSON ou XML.

EXEMPLO

```js
// Um cliente faz uma chamada de procedimento remoto para um serviço no servidor
obterDetalhesDoProduto(produtoId);
```

PROS/CONTRAS

- ✅ Alta performance e baixa latência.

- ✅ Ideal para comunicações internas de microserviços.
- 🚨 Requer definição rigorosa de interface usando Protocol Buffers.
- 🚨 Menos flexível em termos de manipulação de dados em comparação com REST.

## SOAP (Simple Object Access Protocol)

- Protocolo baseado em XML para troca de informações.
- Usa WSDL (Web Services Description Language) para descrição rigorosa do serviço.
- Suporta operações além de CRUD, incluindo transações e mensagens confiáveis.

EXEMPLO

```js
// Uma requisição SOAP para buscar informações de um pedido pode incluir um envelope XML detalhando a operação e os parâmetros.

HTTP/1.1 200 OK
Content-Type: text/xml; charset=utf-8
Content-Length: tamanho_do_conteúdo

<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <prod:ObterDetalhesDoProdutoResponse xmlns:prod="http://exemplo.com/produto">
            <prod:Produto>
                <prod:Id>12345</prod:Id>
                <prod:Nome>Tênis de Corrida</prod:Nome>
                <prod:Preco>99.99</prod:Preco>
                <!-- Outros detalhes do produto -->
            </prod:Produto>
        </prod:ObterDetalhesDoProdutoResponse>
    </soap:Body>
</soap:Envelope>
```

PROS/CONTRAS

- ✅ Segurança robusta (WS-Security), adequada para transações empresariais.
- ✅ Padrão bem estabelecido em ambientes corporativos.
- 🚨 Mais verboso e pesado que REST e gRPC.
- 🚨 Complexidade e sobrecarga maior na criação e consumo de serviços.

## GraphQL (Graph Query Language)

- Linguagem de consulta para APIs.
- Permite que os clientes solicitem exatamente os dados que precisam.
- Uma única endpoint pode manipular diversas consultas e mutações.

EXEMPLO

- Uma consulta GraphQL para buscar produtos por categoria, como:

```graphql
{
  produtos(categoria: "tenis") {
    nome
    preco
    quantidade
  }
}
```

PROS/CONTRAS

- ✅ Eficiência de dados e redução de sobrecarga de rede.
- ✅ Facilita a evolução da API sem quebrar as consultas existentes.
- 🚨 Complexidade na implementação do lado do servidor.
- 🚨 Consultas profundamente aninhadas podem impactar o desempenho.
