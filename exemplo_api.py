from core_api_ixc.client import IxcApiClient

def get_cidades(token, dominio, versao_api):
    api_ixc = IxcApiClient(token, dominio, versao_api)

    parametros = {'qtype': 'cidade.id',  # campo de filtro
                  'query': '5568',  # valor para consultar
                  'oper': '=',  # operador da consulta
                  'page': '1',  # página a ser mostrada
                  'rp': '20',  # quantidade de registros por página
                  'sortname': 'cidade.id',  # campo para ordenar a consulta
                  'sortorder': 'asc',  # //ordenação (asc= crescente | desc=decrescente)
                  }

    json_cidades = api_ixc.get('cidade', parametros)

    return json_cidades


def get_cliente(token, dominio, versao_api):
    api_ixc = IxcApiClient(token, dominio, versao_api)

    parametros = {'qtype': 'cliente.id',  # campo de filtro
                  'query': '500',  # valor para consultar
                  'oper': '=',  # operador da consulta
                  'page': '1',  # página a ser mostrada
                  'rp': '20',  # quantidade de registros por página
                  'sortname': 'cliente.id',  # campo para ordenar a consulta
                  'sortorder': 'asc',  # //ordenação (asc= crescente | desc=decrescente)
                  }

    json_clientes = api_ixc.get('cliente', parametros)

    return json_clientes


def ler_config():
    arquivo = open('param.txt', 'r')
    parametros = {}
    texto = arquivo.readlines()
    for linha in texto:
        chave = linha.split('=')[0]
        valor = linha.split('=')[1]
        parametros.update({chave: valor[:-1]})

    arquivo.close()

    return parametros


def ___main___():
    config = ler_config()

    token = str(config['token'])
    seu_dominio = str(config['dominio'])
    versao_api = str(config['versao_api'])

    print('Obtendo a cidade ID = 5568 \n')
    print(get_cidades(token, seu_dominio, versao_api))
    print('\n*****\n')
    print('Obtendo o cliente ID = 500 \n')
    print(get_cliente(token, seu_dominio, versao_api))


if __name__ == "__main__":
    ___main___()