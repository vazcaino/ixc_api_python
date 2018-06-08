from decouple import config

from core_api_ixc.client import IxcApiClient


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


def get_cidades(token, dominio, versao_api):
    api_ixc = IxcApiClient(token, dominio, versao_api)

    parametros = {'qtype': 'cidade.id',  # campo de filtro
                  'query': '11122',  # valor para consultar
                  'oper': '=',  # operador da consulta
                  'page': '1',  # página a ser mostrada
                  'rp': '20',  # quantidade de registros por página
                  'sortname': 'cidade.id',  # campo para ordenar a consulta
                  'sortorder': 'asc',  # //ordenação (asc= crescente | desc=decrescente)
                  }

    json_cidades = api_ixc.get('cidade', parametros)

    return json_cidades


def post_cidades(token, dominio, versao_api):
    api_ixc = IxcApiClient(token, dominio, versao_api)

    campos = {'nome': 'PalmasTO'}

    json_retorno = api_ixc.post('cidade', campos)

    return json_retorno


def put_cidades(token, dominio, versao_api):
    api_ixc = IxcApiClient(token, dominio, versao_api)

    campos = {'nome': 'PalmasTO', 'uf': '29',}

    json_retorno = api_ixc.put('cidade', campos, '11122')

    return json_retorno


def delete_cidades(token, dominio, versao_api):
    api_ixc = IxcApiClient(token, dominio, versao_api)

    json_retorno = api_ixc.delete('cidade', '1')

    return json_retorno


def ler_config():
    parametros = {}

    parametros.update({'token': config('token')})
    parametros.update({'dominio': config('dominio')})
    parametros.update({'versao_api': config('versao_api', default='1')})

    return parametros


def ___main___():
    config = ler_config()

    token = str(config['token'])
    seu_dominio = str(config['dominio'])
    versao_api = str(config['versao_api'])

    print('Consultando a cidade ID = 11122 \n')
    print(get_cidades(token, seu_dominio, versao_api))
    print('\n*****\n')
    print('Cadastrando uma cidade PalmasTO \n')
    print(post_cidades(token, seu_dominio, versao_api))
    print('\n*****\n')
    print('Atualizando a cidade ID = 11122 \n')
    print(put_cidades(token, seu_dominio, versao_api))
    print('\n*****\n')
    print('Excluindo a cidade ID = 1 \n')
    print(delete_cidades(token, seu_dominio, versao_api))
    # print('\n*****\n')
    # print('Consultando o cliente ID = 500 \n')
    # print(get_cliente(token, seu_dominio, versao_api))


if __name__ == "__main__":
    ___main___()