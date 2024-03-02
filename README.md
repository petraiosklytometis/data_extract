# Conversão e Tratamento de Dados
#### _Este algoritmo, originalmente, foi desenvolvido de forma rápida para atender as necessidades de uma empresa. Trata-se portanto, de um algoritmo de caso real._
#### A empresa me disponibilizou os dados de um formulário de captação de clientes, onde acabou percebendo que alguns contatos eram repetidos e algumas linhas não foram preenchidas. O objetivo era eliminar essas linhas repetidas e vazias, para então obter o número real de clientes passíveis de serem contactados.

Os dados originais foram suprimidos, estando de acordo com a LGPD.

- Primeiro, obtive dados do 4Devs para criação de uma base de dados de clientes fictícios, que prov arquivos em formato JSON.
- Após isso, converti a base JSON do 4Devs para o formato XLSX, enviando para outro diretório.
- No diretório seguinte, os arquivos XLSX são processados e unidos num só arquivo.
- São então analisadas as linhas do arquivo, para atender os seguintes critérios:
    1. Remover linhas duplicadas.
    2. Remover linhas sem ao menos uma forma de contato, seja essa forma um telefone fixo, um email ou um celular.
    3. Fazer um levantamento da quantidade de linhas antes da análise pedida; da quantidade de linhas duplicadas; e da quantidade de linhas sem opção de contato.
- Posteriormente podem ser incluídos:
    - [ ] Automação da captação de dados no 4Devs, com o uso do Selenium.
    - [ ] Criar uma alternativa de caso real com o Forms do Google, que salva em XLSX por padrão.
    - [ ] Armazenamento em banco de dados SQL.
    - [ ] Criação de interface web com Django.

Clique para executar no [Google Colab](https://colab.research.google.com/drive/1QMmJjCRcnBjHpuaLXyOyF9bDBf21KARD?usp=sharing)
