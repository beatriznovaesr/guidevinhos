import flet as ft
from model import Model
from kmeans import Kmeans

kmeans = Kmeans()
model = Model()
class Controller:
    def __init__(self):
        pass
    
    def cadastra_vinho(self, nome_cadastro, uva_cadastro, safra_cadastro, categoria_cadastro, descricao_olfativa, descricao_degustativa, harmonizacao_cadastro):
        model.envia_cadastro_vinho(nome_cadastro, uva_cadastro, safra_cadastro, categoria_cadastro, descricao_olfativa, descricao_degustativa,
                      harmonizacao_cadastro)
        
    def busca_vinhos(self, pesquisa):
        resultado = model.envia_pesquisa(pesquisa)
        return resultado
    
    def cadastra_usuario(self, nome_cadastro, usuario_cadastro, senha_cadastro, dlg_confirma_cadastro, mensagem_erro, page):
        resultado = model.envia_cadastro_usuario(nome_cadastro, usuario_cadastro, senha_cadastro) 
        if resultado.get("sucesso"): 
            dlg_confirma_cadastro(page)
        else:
            mensagem_erro.value = resultado.get("mensagem", "Erro")
            mensagem_erro.update()

    def autenticacao(self,usuario_cadastro, senha_cadastro, handle_routes, mensagem_erro, page):
        resultado = model.envia_autenticacao(usuario_cadastro, senha_cadastro)
        if resultado.get("sucesso"):  
            page.go("/inicial")  
        else:
            mensagem_erro.value = resultado.get("mensagem", "Erro")
            mensagem_erro.update()
    
    def handle_click(self, usuario, vinho_id, e):
        if e.control.selected == False:
            model.envia_favorito(usuario, vinho_id)
        else:
            model.exclui_favorito(usuario, vinho_id)
        e.control.selected = not e.control.selected
        e.control.update()

    def verificar_estado_fav_icon(self, usuario, vinho_id):
        resultado = model.busca_estado_fav(usuario, vinho_id)
        return resultado
          
    def busca_lista_favoritos(self, usuario):
        resultado = model.busca_lista_favoritos(usuario)
        return resultado
        
    def busca_sugeridos(self, usuario, exibe_sugeridos, page):
        vinhos = model.busca_vinhos()
        favoritos = model.busca_lista_kmeans(usuario)
        self.sugeridos = kmeans.lista_dados(favoritos, vinhos)
        if self.sugeridos is not None:
            exibe_sugeridos(page)
        
    def retorna_sugeridos(self):
        return self.sugeridos
    
    def envia_comentario(self, usuario, vinho_id, comentario):
        model.envia_comentario(usuario, vinho_id, comentario)
    
    def retorna_comentarios(self, vinho_id):
        resultado = model.retorna_comentarios(vinho_id)
        return resultado
    
  
