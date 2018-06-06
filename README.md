# API IXCSoft Python

Exemplo na linguagem Python 3.5, de utilização da API RESTFUL para troca de informações com o sistema IXCProvedor


##Como desenvolver:

1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Configure o param.txt
5. Instale as dependencias
6. Execute os testes

```console
git clone git@github.com:vazcaino/ixc_api_python.git ixc_api
cd ixc_api
python -m venv .ixc_api
source .ixc_api/bin/activate
pip install -r requirements.txt
python -m unittest core_api_ixc/tests/test_client.py
```

##Instruções adicionais

O arquivo exemplo_api.py contém a os exemplo para consultar (GET) Clientes e Cidades utilizando a classe IxcApiClient.

Em breve serão liberados os exemplos de inserção (POST), atualização (PUT) e exclusão (DELETE)

A classe para comunicação esta no diretório core_api_ixc, e por enquanto contém apenas os métodos "get" (consulta) e "post" (inclusão). 

