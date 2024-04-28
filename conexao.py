"""Testing CRUD with Python"""
import mysql.connector


class Conexao:
    """Class representing a Conection"""
    __bancoconexao = mysql.connector.connect(
        host='localhost',
        database='dbteste',
        user='root',
        password='masterkey',
    )
    __cursor = __bancoconexao.cursor()

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
