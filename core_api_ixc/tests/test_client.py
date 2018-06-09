import json
from unittest import TestCase
from core_api_ixc.client import IxcApiClient
from decouple import config

class IxcApiTesteAux():

    def ler_config(self):
        parametros = {}

        parametros.update({'token': config('token')})
        parametros.update({'dominio': config('dominio')})
        parametros.update({'versao_api': config('versao_api', default='1')})

        return parametros


    def get_param_cidade(self, id):
        return {'qtype': 'cidade.id', 'query': id, 'oper': '=', 'page': '1', 'rp': '20', 'sortname': 'cidade.id', 'sortorder': 'asc',}


    def get_param_cliente(self, id):
        return {'qtype': 'cliente.id', 'query': id, 'oper': '=', 'page': '1', 'rp': '20', 'sortname': 'cliente.id', 'sortorder': 'asc',}


    def get_tamanho_dados(self, dados_json):
        print(dados_json)
        if 'error' in dados_json:
            return 1

        dados = dados_json['registros']
        return len(dados)


    def get_id_dados(self, dados_json):
        print(dados_json)
        if 'error' in dados_json:
            return '11122'

        dados = dados_json['registros']
        registro = dados[0]
        return registro['id']


    def get_campos_put_cidade(self, id):
        if (id == '11122'):
            return {'nome': 'Palmas', 'uf': '29',}

        return False


    def get_campos_post_cidade(self, id):
        if (id == '11122'):
            return {'nome': 'Palmas',}

        return False


class IxcApiClientTesteAux(TestCase):

    def setUp(self):
        self.metodos_aux = IxcApiTesteAux()
        config = self.metodos_aux.ler_config()
        self.ixc_api_client = IxcApiClient(str(config['token']), str(config['dominio']), str(config['versao_api']))


    def test_retornou_json(self):
        ''' Tem que retornar um json '''

        self.assertTrue(json.loads(self.ixc_api_client.get('cidade', self.metodos_aux.get_param_cidade('5568'))))


    def test_get_usuario(self):
        ''' Tem que retornar um inteiro '''

        usuario = int(self.ixc_api_client.get_usuario());
        self.assertIsInstance(usuario, int)


    def test_get_senha(self):
        ''' Tem que retornar uma senha com 64 caracteres, pois base64 '''

        tamanho_senha = len(self.ixc_api_client.get_senha());
        self.assertEqual(tamanho_senha, 64)


    def test_get_eh_inteiro(self):
        ''' Tem que retornar se o valor é um inteiro ou não '''

        self.assertEqual(self.ixc_api_client.get_eh_inteiro('1'), True)
        self.assertEqual(self.ixc_api_client.get_eh_inteiro(1), True)


class IxcApiClientTeste(TestCase):

    def setUp(self):
        self.metodos_aux = IxcApiTesteAux()
        config = self.metodos_aux.ler_config()
        self.ixc_api_client = IxcApiClient(str(config['token']), str(config['dominio']), str(config['versao_api']))

        self.recurso = 'cidade'
        self.id_cidade = '11122'

        self.id_cliente = '500'


    def test_filtro_get(self):
        ''' Tem que retornar apenas um (1) registro no json '''

        resposta_cidade = self.ixc_api_client.get('cidade', self.metodos_aux.get_param_cidade(self.id_cidade))
        dados_json_cidade = json.loads(resposta_cidade)
        self.assertEqual(1, self.metodos_aux.get_tamanho_dados(dados_json_cidade))
        self.assertEqual(self.id_cidade, self.metodos_aux.get_id_dados(dados_json_cidade))

        resposta_cliente = self.ixc_api_client.get('cliente', self.metodos_aux.get_param_cliente(self.id_cliente))
        dados_json_cliente = json.loads(resposta_cliente)
        self.assertEqual(1, self.metodos_aux.get_tamanho_dados(dados_json_cliente))
        self.assertEqual(self.id_cliente, self.metodos_aux.get_id_dados(dados_json_cliente))


    def test_comunicacao_get(self):
        ''' Tem que retornar 200 que é o código de sucesso '''

        resposta = self.ixc_api_client.conexao_get(self.recurso, self.metodos_aux.get_param_cidade(self.id_cidade))
        self.assertEqual(200, resposta.status_code)


    def test_comunicacao_post(self):
        ''' Tem que retornar 200 que é o código de sucesso '''

        resposta = self.ixc_api_client.conexao_post(self.recurso, self.metodos_aux.get_campos_post_cidade(self.id_cidade))
        self.assertEqual(200, resposta.status_code)


    def test_comunicacao_put(self):
        ''' Tem que retornar 200 que é o código de sucesso '''

        resposta = self.ixc_api_client.conexao_put(self.recurso, self.metodos_aux.get_campos_put_cidade(self.id_cidade), self.id_cidade)
        self.assertEqual(200, resposta.status_code)


    def test_comunicacao_delete(self):
        ''' Tem que retornar 200 que é o código de sucesso '''

        resposta = self.ixc_api_client.conexao_delete(self.recurso, '1')
        self.assertEqual(200, resposta.status_code)

