import requests

class IxcApiClient:


    def __init__(self, token, url_base, versao):
        self.token = token
        #TODO adicionar / no final da url caso nao venha
        self.api_url_base = url_base + 'webservice/v' + versao + '/'

        self.set_cabecalho_padrao({'Content-Type': 'application/x-www-form-urlencoded'})
        self.set_cabecalho_get({'Content-Type': 'application/x-www-form-urlencoded', 'ixcsoft': "listar"})


    def set_parametros(self, parametros):
        #TODO validar se estao vindo de forma correta, os nomes
        self.parametros = parametros


    def get_parametros(self):
        return self.parametros


    def get_usuario(self):
        return self.token.split(':')[0]


    def get_senha(self):
        return self.token.split(':')[1]


    def get_url(self, recurso):
        return self.api_url_base + recurso + '/'


    def set_cabecalho_padrao(self, cabecalho):
        self.cabecalho_padrao = cabecalho


    def get_cabecalho_padrao(self):
        return self.cabecalho_padrao


    def set_cabecalho_get(self, cabecalho):
        self.cabecalho_get = cabecalho


    def get_cabecalho_get(self):
        return self.cabecalho_get


    def conexao_get(self, recurso, parametros):
        resposta = requests.post(self.get_url(recurso), data=parametros, auth=(self.get_usuario(), self.get_senha()), headers=self.get_cabecalho_get())

        return resposta


    def conexao_post(self, recurso, parametros):
        resposta = requests.post(self.get_url(recurso), parametros, auth=(self.get_usuario(), self.get_senha()), headers=self.get_cabecalho_padrao())

        return resposta


    def get(self, recurso, parametros):
        self.set_parametros(parametros)
        conexao = self.conexao_get(recurso, self.get_parametros())
        dados = conexao.text

        return dados


    def post(self, recurso, parametros):
        self.set_parametros(parametros)
        conexao = self.conexao_get(recurso, self.get_parametros())
        dados = conexao.text

        return dados
