"""Import the conection of database"""
import conexao


class Provisorio(conexao.Conexao):
    """Testing class"""
    pass


novaconexao = Provisorio()
# novaconexao.inserir('ovo20unidade', 22.30)
# novaconexao.deletarporid(9)
novaconexao.visualizar('estoque')
novaconexao.fecharconexao()
