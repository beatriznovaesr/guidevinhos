from database import DB

database = DB()
class Model:
    
    def __init__(self):
        pass
        

    def envia_cadastro_vinho(self, nome_cadastro, uva_cadastro, safra_cadastro, categoria_cadastro, descricao_olfativa, descricao_degustativa,
                      harmonizacao_cadastro):
        database.salva_vinhos(nome_cadastro, uva_cadastro, safra_cadastro, categoria_cadastro, descricao_olfativa, descricao_degustativa,
                      harmonizacao_cadastro)
    
    def envia_pesquisa(self, pesquisa):
        resultado = database.busca_vinhos(pesquisa)
        return resultado
    
    def envia_cadastro_usuario(self, nome_cadastro, usuario_cadastro, senha_cadastro):
        resultado = database.salva_usuario(nome_cadastro, usuario_cadastro, senha_cadastro)
        return resultado
    
    def envia_autenticacao(self, usuario_cadastro, senha_cadastro):
        resultado = database.autenticacao(usuario_cadastro, senha_cadastro)
        return resultado
    
    def envia_favorito(self, usuario, vinho_id):
        database.salva_favorito(usuario, vinho_id)
    
    def exclui_favorito(self, usuario, vinho_id):
        database.exclui_favorito(usuario, vinho_id)
    
    def busca_estado_fav(self, usuario, vinho_id):
        resultado = database.verificar_vinho_favorito(usuario, vinho_id)
        return resultado
    
    def busca_lista_favoritos(self, usuario):
        resultado = database.busca_lista_favoritos(usuario)
        return resultado
    
    def busca_lista_kmeans(self, usuario):
        resultado = database.busca_lista_kmeans(usuario)
        return resultado
    
    def busca_vinhos(self):
        resultado = database.busca_todos_vinhos()
        return resultado
    
    def envia_comentario(self, usuario, vinho_id, comentario):
        database.salva_comentario(usuario, vinho_id, comentario)
        print('chegou no model')
    
    def retorna_comentarios(self, vinho_id):
        resultado = database.retorna_comentarios(vinho_id)
        return resultado
