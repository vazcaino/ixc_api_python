import json
from unittest import TestCase
from core_api_ixc.client import IxcApiClient

class IxcApiClientTeste(TestCase):

    def setUp(self):
        config = self.ler_config()

        token = str(config['token'])
        dominio = str(config['dominio'])
        versao_api = str(config['versao_api'])

        self.recurso = 'cidade'
        self.id_cidade = '5568'

        self.id_cliente = '500'

        self.IxcApi = IxcApiClient(token, dominio, versao_api)


    def ler_config(self):
        arquivo = open('param.txt', 'r')
        parametros = {}
        texto = arquivo.readlines()
        for linha in texto:
            if (linha[0:1] == '#'):
                continue
            chave = linha.split('=')[0]
            valor = linha.split('=')[1]
            parametros.update({chave: valor[:-1]})

        arquivo.close()

        return parametros


    def getParamCidade(self, id):
        return {'qtype': 'cidade.id', 'query': id, 'oper': '=', 'page': '1', 'rp': '20', 'sortname': 'cidade.id', 'sortorder': 'asc',}


    def getParamCliente(self, id):
        return {'qtype': 'cliente.id', 'query': id, 'oper': '=', 'page': '1', 'rp': '20', 'sortname': 'cliente.id', 'sortorder': 'asc',}


    def getTamanhoDados(self, dados_json):
        dados = dados_json['registros']
        return len(dados)


    def getIdDados(self, dados_json):
        dados = dados_json['registros']
        registro = dados[0]
        return registro['id']


    def test_comunicacaoGET(self):
        ''' Tem que retornar 200 que é o código de sucesso '''

        self.assertEqual(200, self.IxcApi.conexao_get(self.recurso, self.getParamCidade(self.id_cidade)).status_code)


    def test_comunicacaoPOST(self):
        ''' Tem que retornar 200 que é o código de sucesso '''

        self.assertEqual(200, self.IxcApi.conexao_post(self.recurso, self.getParamCidade(self.id_cidade)).status_code)


    def test_retornouJSON(self):
        ''' Tem que retornar um json '''

        self.assertTrue(json.loads(self.IxcApi.get(self.recurso, self.getParamCidade(self.id_cidade))))


    def test_getUsuario(self):
        ''' Tem que retornar um inteiro '''

        usuario = int(self.IxcApi.get_usuario());
        self.assertIsInstance(usuario, int)


    def test_getSenha(self):
        ''' Tem que retornar uma senha com 64 caracteres, pois base64 '''

        tamanho_senha = len(self.IxcApi.get_senha());
        self.assertEqual(tamanho_senha, 64)


    def test_filtroGET(self):
        ''' Tem que retornar apenas um (1) registro no json '''

        resposta_cidade = self.IxcApi.get('cidade', self.getParamCidade(self.id_cidade))
        dados_json_cidade = json.loads(resposta_cidade)
        self.assertEqual(1, self.getTamanhoDados(dados_json_cidade))
        self.assertEqual(self.id_cidade, self.getIdDados(dados_json_cidade))

        resposta_cliente = self.IxcApi.get('cliente', self.getParamCliente(self.id_cliente))
        dados_json_cliente = json.loads(resposta_cliente)
        self.assertEqual(1, self.getTamanhoDados(dados_json_cliente))
        self.assertEqual(self.id_cliente, self.getIdDados(dados_json_cliente))
