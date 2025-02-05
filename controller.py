import flet as ft
from model import Model
from kmeans import Kmeans

class Controller:
    def __init__(self):
        self.kmeans = Kmeans()
        self.model = Model()
    
    def cadastra_vinho(self, nome_cadastro, uva_cadastro, safra_cadastro, categoria_cadastro, descricao_olfativa, descricao_degustativa, harmonizacao_cadastro):
        self.model.envia_cadastro_vinho(nome_cadastro, uva_cadastro, safra_cadastro, categoria_cadastro, descricao_olfativa, descricao_degustativa,
                      harmonizacao_cadastro)
        
    def busca_vinhos(self, pesquisa):
        resultado = self.model.envia_pesquisa(pesquisa)
        return resultado
    
    def cadastra_usuario(self, nome_cadastro, usuario_cadastro, senha_cadastro, mensagem):
        resultado = self.model.envia_cadastro_usuario(nome_cadastro, usuario_cadastro, senha_cadastro) 
        if resultado.get("sucesso"): 
            mensagem.value = "Cadastro realizado"
        else:
            mensagem.value = resultado.get("mensagem", "erro")
        mensagem.update()

    def autenticacao(self,usuario_cadastro, senha_cadastro, handle_routes, mensagem_erro, page):
        resultado = self.model.envia_autenticacao(usuario_cadastro, senha_cadastro)
        if resultado.get("sucesso"):  
            page.go("/inicial")  
        else:
            mensagem_erro.value = resultado.get("mensagem", "Erro")
            mensagem_erro.update()
    
    def envia_favorito(self, usuario, vinho_id, e):
        if e.control.selected == False:
            self.model.envia_favorito(usuario, vinho_id)
        else:
            self.model.exclui_favorito(usuario, vinho_id)

    def verificar_estado_fav_icon(self, usuario, vinho_id):
        resultado = self.model.busca_estado_fav(usuario, vinho_id)
        return resultado
          
    def busca_lista_favoritos(self, usuario):
        resultado = self.model.busca_lista_favoritos(usuario)
        return resultado
        
    def busca_sugeridos(self, usuario, exibe_sugeridos, page):
        vinhos = self.model.busca_vinhos()
        favoritos = self.model.busca_lista_kmeans(usuario)
        self.sugeridos = self.kmeans.lista_dados(favoritos, vinhos)
        if self.sugeridos is not None:
            exibe_sugeridos(page)
        
    def retorna_sugeridos(self):
        return self.sugeridos
    
    def envia_comentario(self, usuario, vinho_id, comentario):
        self.model.envia_comentario(usuario, vinho_id, comentario)
    
    def retorna_comentarios(self, vinho_id):
        resultado = self.model.retorna_comentarios(vinho_id)
        return resultado
    
  
