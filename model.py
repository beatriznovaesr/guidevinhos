from database import DB

class Model:
    
    def __init__(self):
        self.database = DB()

    def envia_cadastro_vinho(self, nome_cadastro, uva_cadastro, safra_cadastro, categoria_cadastro, descricao_olfativa, descricao_degustativa,
                      harmonizacao_cadastro):
        self.database.salva_vinhos(nome_cadastro, uva_cadastro, safra_cadastro, categoria_cadastro, descricao_olfativa, descricao_degustativa,
                      harmonizacao_cadastro)
    
    def envia_pesquisa(self, pesquisa):
        resultado = self.database.busca_vinhos(pesquisa)
        return resultado
    
    def envia_cadastro_usuario(self, nome_cadastro, usuario_cadastro, senha_cadastro):
        resultado = self.database.salva_usuario(nome_cadastro, usuario_cadastro, senha_cadastro)
        return resultado
    
    def envia_autenticacao(self, usuario_cadastro, senha_cadastro):
        resultado = self.database.autenticacao(usuario_cadastro, senha_cadastro)
        return resultado
    
    def envia_favorito(self, usuario, vinho_id):
        self.database.salva_favorito(usuario, vinho_id)
    
    def exclui_favorito(self, usuario, vinho_id):
        self.database.exclui_favorito(usuario, vinho_id)
    
    def busca_estado_fav(self, usuario, vinho_id):
        resultado = self.database.verificar_vinho_favorito(usuario, vinho_id)
        return resultado
    
    def busca_lista_favoritos(self, usuario):
        resultado = self.database.busca_lista_favoritos(usuario)
        return resultado
    
    def busca_lista_kmeans(self, usuario):
        resultado = self.database.busca_lista_kmeans(usuario)
        return resultado
    
    def busca_vinhos(self):
        resultado = self.database.busca_todos_vinhos()
        return resultado
    
    def envia_comentario(self, usuario, vinho_id, comentario):
        self.database.salva_comentario(usuario, vinho_id, comentario)
    
    def retorna_comentarios(self, vinho_id):
        resultado = self.database.retorna_comentarios(vinho_id)
        return resultado
