import requests

class IxcApiClient:


    def __init__(self, token, url_base, versao):
        self.token = token
        if (url_base[-1:] != '/'):
            url_base = url_base + '/'
        self.api_url_base = url_base + 'webservice/v' + versao + '/'

        self.set_cabecalho_padrao({'Content-Type': 'application/x-www-form-urlencoded'})
        #self.set_cabecalho_padrao({'Content-Type': 'text/json'})
        self.set_cabecalho_get({'Content-Type': 'application/x-www-form-urlencoded', 'ixcsoft': "listar"})


    def get_eh_inteiro(self, valor):
        if (not isinstance(valor, int)):
            valor_int = int(valor)
            if (not isinstance(valor_int, int)):
                return False

        return True


    def set_parametros(self, parametros):
        #TODO validar se estao vindo de forma correta, os nomes
        self.parametros = parametros


    def get_parametros(self):
        return self.parametros


    def set_campos(self, campos):
        self.campos = campos


    def get_campos(self):
        return self.campos


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


    def conexao_put(self, recurso, campos, id_registro):
        if (not self.get_eh_inteiro(id_registro)):
            return False

        url_put = self.get_url(recurso)
        resposta = requests.put(url_put + id_registro, campos, auth=(self.get_usuario(), self.get_senha()), headers=self.get_cabecalho_padrao())

        return resposta


    def conexao_delete(self, recurso, id_registro):
        if (not self.get_eh_inteiro(id_registro)):
            return False

        url_delete = self.get_url(recurso)
        resposta = requests.delete(url_delete + id_registro, auth=(self.get_usuario(), self.get_senha()), headers=self.get_cabecalho_padrao())

        return resposta


    def get(self, recurso, parametros):
        self.set_parametros(parametros)
        conexao = self.conexao_get(recurso, self.get_parametros())
        dados = conexao.text

        return dados


    def post(self, recurso, campos):
        self.set_campos(campos)
        conexao = self.conexao_post(recurso, self.get_campos())
        dados = conexao.text

        return dados


    def put(self, recurso, campos, id_registro):
        self.set_campos(campos)
        conexao = self.conexao_put(recurso, self.get_campos(), id_registro)
        dados = conexao.text

        return dados


    def delete(self, recurso, id_registro):
        conexao = self.conexao_delete(recurso, id_registro)
        dados = conexao.text

        return dados