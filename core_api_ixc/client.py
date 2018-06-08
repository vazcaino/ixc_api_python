import requests

class IxcApiClient:
    """
    Classe para comunicação com API da IXCSoft a partir de um software Python.
    """


    def __init__(self, token, url_base, versao):
        """

        Args:
            token (String): Token gerado no usuário de webservice criado no sistema da IXC.
            url_base (String): Caminho (URL) completo do site da sua empresa. Ex: 'http://www.suaempresa.com.br/'
            versao (String): Versão da API da IXCSoft. Utilizar '1'.
        """
        self.token = token
        if (url_base[-1:] != '/'):
            url_base = url_base + '/'
        self.api_url_base = url_base + 'webservice/v' + versao + '/'

        self.set_cabecalho_padrao({'Content-Type': 'application/x-www-form-urlencoded'})
        self.set_cabecalho_get({'Content-Type': 'application/x-www-form-urlencoded', 'ixcsoft': "listar"})


    def get_eh_inteiro(self, valor):
        """

        Args:
            valor (String): Valor para ser validado se é um inteiro

        Returns : Boolean

        """
        if (not isinstance(valor, int)):
            valor_int = int(valor)
            if (not isinstance(valor_int, int)):
                return False

        return True


    def set_parametros(self, parametros):
        """

        Args:
            parametros (Dicionário): Parâmetros de consulta para o método GET.
        """
        #TODO validar se estao vindo de forma correta, os nomes
        self.parametros = parametros


    def get_parametros(self):
        """

        Returns: Dicionário com os parâmetros de consulta.

        """
        return self.parametros


    def set_campos(self, campos):
        """

        Args:
            campos (Dicionário): Campos a serem enviados na requisição.
        """
        self.campos = campos


    def get_campos(self):
        """

        Returns: Dicionário de dados com os campos passados em set_campos().

        """
        return self.campos


    def get_usuario(self):
        """

        Returns: String com o ID do usuário.

        """
        return self.token.split(':')[0]


    def get_senha(self):
        """

        Returns: String com a senha do usuário.

        """
        return self.token.split(':')[1]


    def get_url(self, recurso):
        """

        Args:
            recurso (String): Nome do recurso. Ex: 'cliente'

        Returns: String com a url completa do webservice.

        """
        return self.api_url_base + recurso + '/'


    def set_cabecalho_padrao(self, cabecalho):
        """

        Args:
            cabecalho (Dicionário): Cabeçalho http/https.
        """
        self.cabecalho_padrao = cabecalho


    def get_cabecalho_padrao(self):
        """

        Returns: Dicionário com um cabeçalho http/https.

        """
        return self.cabecalho_padrao


    def set_cabecalho_get(self, cabecalho):
        """

        Args:
            cabecalho (Dicionário): Cabeçalho http/https.
        """
        self.cabecalho_get = cabecalho


    def get_cabecalho_get(self):
        """

        Returns: Dicionário com um cabeçalho http/https.

        """
        return self.cabecalho_get


    def conexao_get(self, recurso, parametros):
        """

        Args:
            recurso (String): Nome do recurso que deseja acessar, normalmente o nome do formulário no IXCSoft.
            Exemplo: 'cidade'.

            parametros (Dicionário): Dados de filtro para a requisição GET.
            Exemplo: {'qtype': 'cidade.id',  # campo de filtro
                      'query': '11122',  # valor para consultar
                      'oper': '=',  # operador da consulta
                      'page': '1',  # página a ser mostrada
                      'rp': '20',  # quantidade de registros por página
                      'sortname': 'cidade.id',  # campo para ordenar a consulta
                      'sortorder': 'asc',  # //ordenação (asc= crescente | desc=decrescente)
                      }

        Returns: Requisição post http/https do módulo requests do Python.

        """
        resposta = requests.post(self.get_url(recurso), data=parametros, auth=(self.get_usuario(), self.get_senha()), headers=self.get_cabecalho_get())

        return resposta


    def conexao_post(self, recurso, campos):
        """

        Args:
            recurso (String): Nome do recurso que deseja acessar, normalmente o nome do formulário no IXCSoft.
            Exemplo: 'cidade'.

            campos(Dicionário): Campos com valores a serem passados para a requisição POST.
            Exemplo: {'nome': 'Palmas', 'uf': '29',} - Onde '29' é o ID da UF Tocantins.

        Returns: Requisição post http/https do módulo requests do Python.

        """
        resposta = requests.post(self.get_url(recurso), campos, auth=(self.get_usuario(), self.get_senha()), headers=self.get_cabecalho_padrao())

        return resposta


    def conexao_put(self, recurso, campos, id_registro):
        """

        Args:
            recurso (String): Nome do recurso que deseja acessar, normalmente o nome do formulário no IXCSoft.
            Exemplo: 'cidade'.

            campos(Dicionário): Campos com valores a serem passados para a requisição PUT.
            Exemplo: {'nome': 'Palmas TO', 'uf': '29',} - Onde '29' é o ID da UF Tocantins.

            id_registro (String): ID do registro a ser atualizado pela requisição.
            Exemplo: '5765'.

        Returns: Requisição put http/https do módulo requests do Python.

        """
        if (not self.get_eh_inteiro(id_registro)):
            return False

        url_put = self.get_url(recurso)
        resposta = requests.put(url_put + id_registro, campos, auth=(self.get_usuario(), self.get_senha()), headers=self.get_cabecalho_padrao())

        return resposta


    def conexao_delete(self, recurso, id_registro):
        """

        Args:
            recurso (String): Nome do recurso que deseja acessar, normalmente o nome do formulário no IXCSoft.
            Exemplo: 'cidade'.

            id_registro (String): ID do registro a ser excluído pela requisição.
            Exemplo: '5765'.

        Returns: Requisição delete http/https do módulo requests do Python.

        """
        if (not self.get_eh_inteiro(id_registro)):
            return False

        url_delete = self.get_url(recurso)
        resposta = requests.delete(url_delete + id_registro, auth=(self.get_usuario(), self.get_senha()), headers=self.get_cabecalho_padrao())

        return resposta


    def get(self, recurso, parametros):
        """

        Args:
            recurso (String): Nome do recurso que deseja acessar, normalmente o nome do formulário no IXCSoft.
            Exemplo: 'cidade'.

            parametros (Dicionário): Dados de filtro para a requisição GET.
            Exemplo: {'qtype': 'cidade.id',  # campo de filtro
                      'query': '11122',  # valor para consultar
                      'oper': '=',  # operador da consulta
                      'page': '1',  # página a ser mostrada
                      'rp': '20',  # quantidade de registros por página
                      'sortname': 'cidade.id',  # campo para ordenar a consulta
                      'sortorder': 'asc',  # //ordenação (asc= crescente | desc=decrescente)
                      }

        Returns: String com o JSON do retorno da requisição.

        """
        self.set_parametros(parametros)
        conexao = self.conexao_get(recurso, self.get_parametros())
        dados = conexao.text

        return dados


    def post(self, recurso, campos):
        """

        Args:
            recurso (String): Nome do recurso que deseja acessar, normalmente o nome do formulário no IXCSoft.
            Exemplo: 'cidade'.

            campos(Dicionário): Campos com valores a serem passados para a requisição POST.
            Exemplo: {'nome': 'Palmas', 'uf': '29',} - Onde '29' é o ID da UF Tocantins.

        Returns: String com o JSON do retorno da requisição.

        """
        self.set_campos(campos)
        conexao = self.conexao_post(recurso, self.get_campos())
        dados = conexao.text

        return dados


    def put(self, recurso, campos, id_registro):
        """

        Args:
            recurso (String): Nome do recurso que deseja acessar, normalmente o nome do formulário no IXCSoft.
            Exemplo: 'cidade'.

            campos(Dicionário): Campos com valores a serem passados para a requisição PUT.
            Exemplo: {'nome': 'Palmas TO', 'uf': '29',} - Onde '29' é o ID da UF Tocantins.

            id_registro (String): ID do registro a ser atualizado pela requisição.
            Exemplo: '5765'.

        Returns: String com o JSON do retorno da requisição.

        """
        self.set_campos(campos)
        conexao = self.conexao_put(recurso, self.get_campos(), id_registro)
        dados = conexao.text

        return dados


    def delete(self, recurso, id_registro):
        """

        Args:
            recurso (String): Nome do recurso que deseja acessar, normalmente o nome do formulário no IXCSoft.
            Exemplo: 'cidade'.

            id_registro (String): ID do registro a ser excluído pela requisição.
            Exemplo: '5765'.

        Returns: String com o JSON do retorno da requisição.

        """
        conexao = self.conexao_delete(recurso, id_registro)
        dados = conexao.text

        return dados
