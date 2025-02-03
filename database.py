from bson.objectid import ObjectId
import bcrypt
from pymongo import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb+srv://beatriznovaesrocha:HDvvjxOXLLAzbDuw@cluster0.wucqs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


class DB:
    def __init__(self):
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.bd = self.client["bd"]
        vinhos = self.bd["vinhos"]
        usuarios = self.bd["usuarios"]

    def salva_vinhos(self, nome_cadastro, uva_cadastro, safra_cadastro, categoria_cadastro, descricao_olfativa, descricao_degustativa,
                      harmonizacao_cadastro):
        self.bd.vinhos.insert_one({"nome": nome_cadastro, 
                                   "uva": uva_cadastro, 
                                   "safra": safra_cadastro, 
                                   "categoria": categoria_cadastro,
                                   "descricao olfativa": descricao_olfativa, 
                                   "descricao degustativa": descricao_degustativa,
                                   "harmonizacao": harmonizacao_cadastro})
        
    def busca_vinhos(self, pesquisa):
        resultado = self.bd.vinhos.find({
                                        "$or":[
                                                {"nome": {"$regex": pesquisa, "$options": "i"}},
                                                {"uva": {"$regex": pesquisa, "$options": "i"}},
                                                {"safra": {"$regex": pesquisa, "$options": "i"}},
                                                {"categoria": {"$regex": pesquisa, "$options": "i"}},
                                                {"descricao olfativa": {"$regex": pesquisa, "$options": "i"}},
                                                {"descricao degustativa": {"$regex": pesquisa, "$options": "i"}},
                                                {"harmonizacao": {"$regex": pesquisa, "$options": "i"}},
                                                {"_id": {"$regex": pesquisa, "$options": "i"}}

                                             ]
                                       })
        return list(resultado)

    def salva_usuario(self, nome_cadastro, usuario_cadastro, senha_cadastro):
        if self.valida_usuario(usuario_cadastro) == 1:
            return {"sucesso": False, "mensagem": "Usuário já cadastrado"}
        else:
            salt = bcrypt.gensalt()
            senha=bcrypt.hashpw(senha_cadastro.encode('utf-8'), salt)
            self.bd.usuarios.insert_one({"nome": nome_cadastro,
                                        "user": usuario_cadastro,
                                        "senha": senha})
            return {"sucesso": True}

    def autenticacao(self, usuario_login, senha_login):
        resultado = self.bd.usuarios.find_one({"user": usuario_login}, {"senha": 1})
        if resultado:  
            senha_hash = resultado["senha"]  
            if bcrypt.checkpw(senha_login.encode('utf-8'), senha_hash):
                return {"sucesso": True}
            else:
                return {"sucesso": False, "mensagem": "Usuário ou senha incorretos"}
        else:
            return {"sucesso": False, "mensagem": "Usuário não cadastrado"}
    
    def valida_usuario(self, usuario_cadastro):
        resultado = self.bd.usuarios.find_one({"user": usuario_cadastro})
        if resultado:
            return 1 
        else: 
            return 0 

    def salva_favorito(self, usuario, vinho_id):
        vinho = self.bd.vinhos.find_one({"_id": ObjectId(vinho_id)})
        vinho_favoritado = {"_id": ObjectId(vinho_id), "nome": vinho["nome"], "categoria": vinho["categoria"],
         "safra": vinho["safra"], "uva": vinho["uva"]}

        self.bd.usuarios.update_one(
            {"user": usuario},
            {"$addToSet": {"vinhos_favoritos": vinho_favoritado}}  
        )
    
    def exclui_favorito(self, usuario, vinho_id):
        self.bd.usuarios.update_one(
        {"user": usuario}, 
        {"$pull": {"vinhos_favoritos": {"_id": ObjectId(vinho_id)}}} 
    )

    def verificar_vinho_favorito(self, usuario, vinho_id):
        print(f"Buscando vinho {vinho_id} para o usuário {usuario}")
        resultado = self.bd.usuarios.find_one(
            {
                "user": usuario,
                "vinhos_favoritos": {"$elemMatch": {"_id": ObjectId(vinho_id)}}
            }
        )
        return resultado is not None

    def busca_lista_favoritos(self, usuario):
        resultado = self.bd.usuarios.find_one({"user": usuario}, {"vinhos_favoritos": 1, "_id": 0})
        return [vinho["nome"] for vinho in resultado.get("vinhos_favoritos", [])]
    
    def busca_lista_kmeans(self, usuario):
        resultado = self.bd.usuarios.find_one({"user": usuario}, {"vinhos_favoritos": 1, "_id": 0})
        return resultado

    def busca_todos_vinhos(self):
        resultado = self.bd.vinhos.find()
        resultado = list(resultado)
        return resultado

    def salva_comentario(self, usuario, vinho_id, comentario):
        usuario = self.bd.usuarios.find_one({"user": usuario})
        comentario = {"usuario": usuario["user"], "nome": usuario["nome"], "comentario": comentario}

        self.bd.vinhos.update_one(
            {"_id": ObjectId(vinho_id)},
            {"$addToSet": {"comentarios": comentario}}  
        )
        print(comentario)
    
    def retorna_comentarios(self, vinho_id):
        resultado = self.bd.vinhos.find_one({"_id": ObjectId(vinho_id)}, {"comentarios": 1})
        return resultado
