"""Testing CRUD with Python"""
from configparser import ConfigParser
import mysql.connector

class Conexao:
    """Class representing a Conection"""
    def __init__(self):
        """Method initialization"""
        __config = ConfigParser()
        __config.read('Config.ini')
        self.__host = __config["Database"]["host"]
        self.__database = __config["Database"]["database"]
        self.__user = __config["Database"]["user"]
        self.__password = __config["Database"]["password"]
        self.__bancoconexao = mysql.connector.connect(
            host=self.__host,
            database=self.__database,
            user=self.__user,
            password=self.__password,
            )
        self.__cursor = self.__bancoconexao.cursor()

    def inserir(self, nome_produto, valor):
        """Method insert in database"""
        comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
        self.__cursor.execute(comando)
        self.__bancoconexao.commit()  # Edita o banco de dado

    def deletarporid(self, idproduto):
        """Method delete in database"""
        comando = f'DELETE FROM vendas WHERE idvendas = {idproduto}'
        self.__cursor.execute(comando)
        self.__bancoconexao.commit()

    def visualizar(self, tabela):
        """Method visualization"""
        comando = f'SELECT * FROM {tabela}'
        self.__cursor.execute(comando)
        resultado = self.__cursor.fetchall()
        print(resultado)

    def atualizar(self, nome_produto, valor):
        """Method to update a product"""
        comando = f"UPDATE vendas SET valor = {valor} where nome_produto = '{nome_produto}'"
        self.__cursor.execute(comando)
        self.__bancoconexao.commit()

    def fecharconexao(self):
        """Method to close the connection"""
        self.__cursor.close()
        self.__bancoconexao.close()
