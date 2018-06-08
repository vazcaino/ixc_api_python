# API IXCSoft Python
[![Build Status](https://travis-ci.org/vazcaino/ixc_api_python.svg?branch=master)](https://travis-ci.org/vazcaino/ixc_api_python)
[![Maintainability](https://api.codeclimate.com/v1/badges/b77cb29c3a4bdfe5a90d/maintainability)](https://codeclimate.com/github/vazcaino/ixc_api_python/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b77cb29c3a4bdfe5a90d/test_coverage)](https://codeclimate.com/github/vazcaino/ixc_api_python/test_coverage)

Exemplo na linguagem Python 3.5, de utilização da API RESTFUL para troca de informações com o sistema IXCProvedor


## Como iniciar o desenvolvimento:

1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Configure o param.txt
5. Instale as dependências
6. Configure os dados de acesso através do exemplo com o .env
7. Execute os testes
8. Gere a documentação da classe IxcApiClient() (após executado ficará acessível em http://localhost:9876/core_api_ixc.client.html)

```console
git clone git@github.com:vazcaino/ixc_api_python.git ixc_api
cd ixc_api
python -m venv .ixc_api
source .ixc_api/bin/activate
pip install -r requirements.txt
cp contrib/env-exemplo .env
python -m unittest core_api_ixc/tests/test_client.py
pydoc -p 9876
```

## Instruções adicionais

O arquivo exemplo_api.py contém a os exemplo para consultar (GET) Clientes e Cidades pelo campo ID, utilizando a classe IxcApiClient.

Contém também os exemplos de inserção (POST), atualização (PUT) e exclusão (DELETE) do formulário de cidades.

A classe para comunicação esta no diretório "core_api_ixc".

OBS: Método de atualização (PUT) ainda não esta funcional.

