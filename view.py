import flet as ft
from bson.objectid import ObjectId
from controller import Controller
controller = Controller()

class View:
    def __init__(self):
        self.conteudo_dinamico = ft.Container()
        self.conteudo_dinamico_sugeridos = ft.Container()
        ft.app(self.main)
    
    def handle_routes(self, page: ft.Page):
        page.clean()  

        if page.route == "/cadastro":
            self.pagina_cadastro(page)
        elif page.route == "/inicial":
            self.pagina_inicial(page)
        elif page.route == "/perfil":
            self.pagina_perfil(page)
        elif page.route == "/login":  
            self.pagina_login(page)
        else:
            self.pagina_login(page)

        page.update() 
    
    def handle_tap(self, e):
      self.barra_busca.open_view()
    
    def handle_submit(self, e):
        pesquisa = self.barra_busca.value
        self.resultado = controller.busca_vinhos(pesquisa)
        self.lv.controls.clear()
        for vinho in self.resultado:
            self.lv.controls.append(ft.ListTile(
                        title=ft.Text(vinho.get("nome")),   
                        data= vinho,
                        on_click=lambda e, vinho=vinho: self.pagina_exibe_vinho(vinho, e.page)))
        
        self.barra_busca.update()

    def pagina_login(self, page: ft.Page):
        page.bgcolor="#000000"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        titulo_login = ft.Text(
                                value="Login",
                                size=40,  
                                color="#EEE6E7",  
                                weight=ft.FontWeight.BOLD,  
                                font_family="Arial",  
                                text_align="center"
                                )
        
        self.usuario_login =ft.TextField(
                                    label="Usuário", 
                                    label_style=ft.TextStyle(color="#EEE6E7"),
                                    focused_border_color="#EEE6E7",
                                    text_align="left",
                                    fill_color='#A3000000',
                                    color= "#EEE6E7",
                                    border_radius=30
                                    )
                            
        senha_login = ft.TextField(
                                    label="Senha", 
                                    label_style=ft.TextStyle(color="#EEE6E7"),
                                    focused_border_color="#EEE6E7",
                                    text_align="left",
                                    fill_color='#A3000000',
                                    color= "#EEE6E7",
                                    border_radius=30,
                                    password=True, 
                                    can_reveal_password=True
                                    )
        
        self.mensagem_erro = ft.Text("", color="#EEE6E7")

        botao_entrar = ft.ElevatedButton(
                                        text="ENTRAR",
                                        bgcolor="#A3000000",
                                        color="#EEE6E7",
                                        width=200,
                                        height=50,
                                        on_click=lambda e: controller.autenticacao(self.usuario_login.value, senha_login.value, 
                                        self.handle_routes, self.mensagem_erro, page)
                                        )
        
        botao_cadastro = ft.CupertinoButton(
                                            content=ft.Text("Cadastre-se", 
                                                            color="#EEE6E7",
                                                            style= ft.TextStyle(
                                                                                decoration=ft.TextDecoration.UNDERLINE
                                                                                )                   
                                                            ),
                                            on_click=lambda _: page.go("/cadastro")
                                            )

                                        
        container = ft.Container(
                                content=ft.Column([
                                                    titulo_login,
                                                    self.usuario_login,
                                                    senha_login,
                                                    self.mensagem_erro,
                                                    botao_entrar,
                                                    botao_cadastro 
                                                    ],
                                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                                    spacing=30
                                                ),
                                width=500,
                                height=500,
                                bgcolor="#5A0717",
                                border_radius=ft.border_radius.all(20),
                                padding=40
                                )
        
        page.add(
                ft.Column([
                            container
                            ],
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER
                            )
                )
    
    def pagina_cadastro(self, page: ft.Page):
        page.bgcolor="#000000"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        titulo_cadastro = ft.Text(
                                value="Cadastro",
                                size=40,  
                                color="#EEE6E7",  
                                weight=ft.FontWeight.BOLD,  
                                font_family="Arial",  
                                text_align="center"
                                )
        
        self.nome_cadastro = ft.TextField(
                                    label="Nome", 
                                    label_style=ft.TextStyle(color="#EEE6E7"),
                                    focused_border_color="#EEE6E7",
                                    text_align="left",
                                    fill_color='#A3000000',
                                    color= "#EEE6E7",
                                    border_radius=30
                                    )

        self.usuario_cadastro = ft.TextField(
                                        label="Usuário", 
                                        label_style=ft.TextStyle(color="#EEE6E7"),
                                        focused_border_color="#EEE6E7",
                                        text_align="left",
                                        fill_color='#A3000000',
                                        color= "#EEE6E7",
                                        border_radius=30
                                    )
        
        self.senha_cadastro = ft.TextField(
                                    label="Senha", 
                                    label_style=ft.TextStyle(color="#EEE6E7"),
                                    focused_border_color="#EEE6E7",
                                    text_align="left",
                                    fill_color='#A3000000',
                                    color= "#EEE6E7",
                                    border_radius=30
                                    )  
        
        mensagem_erro = ft.Text("", color="#EEE6E7")
        
        botao_cadastrar = ft.ElevatedButton(
                                            text="CADASTRAR",
                                            bgcolor="#A3000000",
                                            color="#EEE6E7",
                                            width=200,
                                            height=50,
                                            on_click=lambda e: controller.cadastra_usuario(self.nome_cadastro.value, self.usuario_cadastro.value, self.senha_cadastro.value, 
                                            self.dlg_confirma_cadastro, mensagem_erro, page)
                                        )
        
        container = ft.Container(
                                content=ft.Column([
                                                    titulo_cadastro,
                                                    self.nome_cadastro,
                                                    self.usuario_cadastro,
                                                    self.senha_cadastro,
                                                    mensagem_erro,
                                                    botao_cadastrar
                                                    ],
                                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                                    spacing=30
                                                ),
                                width=500,
                                height=500,
                                bgcolor="#5A0717",
                                border_radius=ft.border_radius.all(20),
                                padding=40
                                )
        
        page.add(
                ft.Column([
                            container
                            ],
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER
                            )
                )
    
    def dlg_confirma_cadastro(self, page: ft.Page):
        dlg = ft.AlertDialog(
        title=ft.Text("Cadastro realizado!"),
        on_dismiss=lambda _: page.go('/login')
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    def pagina_inicial(self, page: ft.Page):
        page.bgcolor = "#5A0717"
        page.vertical_alignment = ft.MainAxisAlignment
        page.horizontal_alignment = ft.CrossAxisAlignment

        self.lv = ft.ListView()
        self.barra_busca = ft.SearchBar(  
                                        bar_bgcolor="#A3000000",
                                        view_elevation=4,
                                        view_bgcolor="#EEE6E7",
                                        view_hint_text= "Busque por vinhos ou pratos",
                                        divider_color= "#A3000000",
                                        width=1200,
                                        on_submit=self.handle_submit,
                                        on_tap= self.handle_tap,
                                        controls=[self.lv]
                                        )   
                                    
        
        botao_perfil = ft.IconButton(
                                    icon=ft.cupertino_icons.PERSON_ALT_CIRCLE,
                                    icon_color="#A3000000",
                                    icon_size=60,
                                    tooltip="Acessar perfil",
                                    on_click=lambda _: page.go('/perfil')
                                    ) 



        container = ft.Container(
                                content=ft.Row([
                                                    self.barra_busca,
                                                    botao_perfil                                          
                                                ],
                                                spacing= 40
                                                )
                                
                                ) 
    
        page.add(ft.Column([
                            container,
                            self.conteudo_dinamico_sugeridos
                            ],
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.START,
                            expand=True,
                            scroll=ft.ScrollMode.ALWAYS
                            ))
        
        page.update()  
        controller.busca_sugeridos(self.usuario_login.value, self.exibe_sugeridos, page)

    def exibe_sugeridos(self, page: ft.Page):
        sugeridos = controller.retorna_sugeridos()
        lista_sugeridos = [
            ft.TextButton(
            text=sugerido.nome,
            style=ft.ButtonStyle(color="#FFFFFF"),
            on_click=lambda e, sugerido=sugerido._asdict(): 
                self.pagina_exibe_vinho(sugerido, e.page)
        )
        for sugerido in sugeridos.itertuples()
        ]

        self.conteudo_dinamico_sugeridos.content = ft.Column(
                                                controls=lista_sugeridos
                                                )
        self.conteudo_dinamico_sugeridos.update()
    
    def sessao_comentarios(self, page:ft.Page):
        comentario = ft.TextField(label="Deixe seu comentário", 
                                    label_style=ft.TextStyle(color="#EEE6E7"),
                                    focused_border_color="#EEE6E7",
                                    text_align="left",
                                    fill_color='#A3000000',
                                    color= "#EEE6E7",
                                    border_radius=30,
                                    multiline=True)
        
        botao_enviar_comentario = ft.ElevatedButton(text="Enviar",
                                                    bgcolor="#A3000000",
                                                    color="#EEE6E7",
                                                    width=300,
                                                    height=40,
                                                    on_click = lambda e: controller.envia_comentario(self.usuario_login.value, self.vinho_id, comentario.value)
                                                    )

        self.lista_comentarios = ft.ListView(expand=True, spacing=5, padding=10)
        self.atualizar_lista_comentarios(page)
        
        bs = ft.BottomSheet(
                            content = ft.Container(
                                                    content = ft.Column(controls=[comentario,
                                                                                botao_enviar_comentario,
                                                                                self.lista_comentarios])
                            )
        )

        return bs
    
    def atualizar_lista_comentarios(self, page:ft.Page):
        self.lista_comentarios.controls.clear()
        comentarios = controller.retorna_comentarios(self.vinho_id)
        lista_comentarios = comentarios.get('comentarios', []) 
        print('view',lista_comentarios)
        for c in lista_comentarios:
            self.lista_comentarios.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text(c['usuario'], weight="bold", size=14),
                        ft.Text(c['comentario'], size=12),
                    ], spacing=2),
                    padding=10,
                    ),
                    
                )

    def pagina_exibe_vinho(self, vinho, page: ft.Page):
        page.bgcolor = "#5A0717"
        page.horizontal_alignment = ft.CrossAxisAlignment
        cor_texto = "#EEE6E7"
        
        if "_1" in vinho:
                    vinho["_id"] = vinho.pop("_1")
        self.vinho_id = vinho.get('_id')
        estado_fav = controller.verificar_estado_fav_icon(self.usuario_login.value, vinho.get('_id'))
        bs = self.sessao_comentarios(page)

        vinhoDet = ft.Container (content=ft.Column([
                                                    ft.Text(f"\n  Nome: {vinho.get('nome')}", color=cor_texto),
                                                    ft.Text(f"  Categoria: {vinho.get('categoria')}", color=cor_texto),
                                                    ft.Text(f"  Safra: {vinho.get('safra')}", color=cor_texto),
                                                    ft.Text(f"  Descrição Olfativa: {vinho.get('descricao olfativa')}", color=cor_texto),
                                                    ft.Text(f"  Descrição Degustativa: {vinho.get('descricao degustativa')}", color=cor_texto),
                                                ], 
                                                    spacing=10),
                                                    width=800,
                                                    height=500,
                                                    bgcolor="#A3000000",
                                                    border_radius=30
                                                    
                                                
                                )
        harmonizacao = ft.Container (content=ft.Column([
                                                        ft.Text(f"\n  Harmonização: {vinho.get('harmonizacao')}", color=cor_texto)
                                                    ]),
                                    width=400,
                                    height=500,
                                    bgcolor="#A3000000",
                                    border_radius=30
                                    )
        
        botao_comentarios = ft.ElevatedButton(text="Visualizar Comentários",
                                            bgcolor="#A3000000",
                                            color="#EEE6E7",
                                            width=300,
                                            height=40,
                                            on_click=lambda e: page.open(bs)
                                            
                                            )
        
        botao_favoritar = ft.Container(content=ft.Column([
                                        ft.IconButton(
                                        icon=ft.cupertino_icons.HEART,
                                        icon_color="#A3000000",
                                        selected_icon=ft.cupertino_icons.HEART_FILL,
                                        selected_icon_color="#A3000000",
                                        selected= estado_fav,
                                        icon_size=40,
                                        tooltip="Favoritar vinho",
                                        on_click=lambda e: controller.handle_click(self.usuario_login.value, vinho.get('_id'), e)
                                    ) ]),
                                    height=500
        )
        
        conteudo_principal = ft.Row([vinhoDet,
                                    harmonizacao,
                                    botao_favoritar],
                                    spacing= 40,
                                    vertical_alignment= ft.MainAxisAlignment.START
                                )
        

        self.conteudo_dinamico_sugeridos.content = ft.Container(
                                                    content=ft.Column([
                                                                        conteudo_principal,
                                                                        botao_comentarios],
                                                    spacing= 20,
                                                    horizontal_alignment= ft.CrossAxisAlignment.CENTER)
                                                    
                                                    )
        
        page.add(self.conteudo_dinamico_sugeridos)
        self.conteudo_dinamico_sugeridos.update()

    def pagina_perfil(self, page: ft.Page):
        page.bgcolor = "#5A0717"
        page.vertical_alignment = ft.MainAxisAlignment
        page.horizontal_alignment = ft.CrossAxisAlignment 

        botao_pag_inicial = ft.ElevatedButton(
                                            text="Página Inicial",
                                            bgcolor="#A3000000",
                                            color="#EEE6E7",
                                            width=100,
                                            height=50,
                                            on_click=lambda _: page.go('/inicial')
                                            )
        
        botao_favoritos = ft.OutlinedButton(text="Favoritos",
                                            style=ft.ButtonStyle(
                                                                color="#EEE6E7"
                                                                ),
                                            on_click=self.pagina_favoritos
                                        )
        botao_adicionar_vinho = ft.OutlinedButton(text="Adicionar Vinho",
                                                style=ft.ButtonStyle(
                                                                        color="#EEE6E7"
                                                                    ),
                                                on_click=self.pagina_cadastro_vinho
                                                )
        botao_sair = ft.OutlinedButton(text="Sair",
                                    style=ft.ButtonStyle(
                                                            color="#EEE6E7"
                                                        ),
                                    on_click=lambda _: page.go('/login')
                                    )
        
        divisao = ft.Divider(height=9, thickness=3, color="#EEE6E7")

        container_inicial = ft.Container(
                                        content=ft.Row(
                                                        [botao_pag_inicial],
                                                        alignment= ft.MainAxisAlignment.END  
                                                        )
                                        )

        container_vertical = ft.Container(content=ft.Row([
                                                        botao_favoritos,
                                                        botao_adicionar_vinho,
                                                        botao_sair
                                                        ]
                                                        )                                      
                                        )  
        
        page.add(ft.Column([
                            container_inicial,
                            container_vertical,
                            divisao,
                            self.conteudo_dinamico
                        ])
                        
                )
        self.pagina_favoritos(None)
    
    def pagina_cadastro_vinho(self, page: ft.Page):
        nome_cadastro = ft.TextField( label="Nome", 
                                    label_style=ft.TextStyle(color="#EEE6E7"),
                                    focused_border_color="#EEE6E7",
                                    text_align="left",
                                    fill_color='#A3000000',
                                    color= "#EEE6E7",
                                    border_radius=30)
        
        uva_cadastro = ft.TextField(label="Uva", 
                                    label_style=ft.TextStyle(color="#EEE6E7"),
                                    focused_border_color="#EEE6E7",
                                    text_align="left",
                                    fill_color='#A3000000',
                                    color= "#EEE6E7",
                                    border_radius=30)
        
        safra_cadastro = ft.TextField(label="Safra", 
                                    label_style=ft.TextStyle(color="#EEE6E7"),
                                    focused_border_color="#EEE6E7",
                                    text_align="left",
                                    fill_color='#A3000000',
                                    color= "#EEE6E7",
                                    border_radius=30)
        
        categoria_cadastro = ft.TextField(label="Categoria", 
                                        label_style=ft.TextStyle(color="#EEE6E7"),
                                        focused_border_color="#EEE6E7",
                                        text_align="left",
                                        fill_color='#A3000000',
                                        color= "#EEE6E7",
                                        border_radius=30)
        
        descricao_olfativa = ft.TextField(label="Descrição Olfativa", 
                                        label_style=ft.TextStyle(color="#EEE6E7"),
                                        focused_border_color="#EEE6E7",
                                        text_align="left",
                                        fill_color='#A3000000',
                                        color= "#EEE6E7",
                                        border_radius=30,
                                        multiline=True)
        
        descricao_degustativa = ft.TextField(label="Descrição Degustativa", 
                                        label_style=ft.TextStyle(color="#EEE6E7"),
                                        focused_border_color="#EEE6E7",
                                        text_align="left",
                                        fill_color='#A3000000',
                                        color= "#EEE6E7",
                                        border_radius=30,
                                        multiline=True)
        
        harmonizacao_cadastro = ft.TextField(label="Sugestão de Harmonização ", 
                                            label_style=ft.TextStyle(color="#EEE6E7"),
                                            focused_border_color="#EEE6E7",
                                            text_align="left",
                                            fill_color='#A3000000',
                                            color= "#EEE6E7",
                                            border_radius=30,
                                            multiline=True)
        
        botao_salvar = ft.ElevatedButton( text="SALVAR",
                                        bgcolor="#A3000000",
                                        color="#EEE6E7",
                                        width=100,
                                        height=50,
                                        on_click=lambda e: controller.cadastra_vinho(
                                                                    nome_cadastro.value,
                                                                    uva_cadastro.value,
                                                                    safra_cadastro.value,
                                                                    categoria_cadastro.value,
                                                                    descricao_olfativa.value,
                                                                    descricao_degustativa.value,
                                                                    harmonizacao_cadastro.value
                                                                )
                                        )
        
        self.conteudo_dinamico.content = ft.Column([
                                                    nome_cadastro,
                                                    uva_cadastro,
                                                    safra_cadastro,
                                                    categoria_cadastro,
                                                    descricao_olfativa,
                                                    descricao_degustativa,
                                                    harmonizacao_cadastro,
                                                    botao_salvar
                                                ],
                                                scroll= ft.ScrollMode.ALWAYS,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.conteudo_dinamico.update()

    def pagina_favoritos(self, page: ft.Page):
        resultado = controller.busca_lista_favoritos(self.usuario_login.value)
        vinhos_favoritados = [ft.Text(value=vinho, color="#EEE6E7", size=18 ) for vinho in resultado]    
        self.conteudo_dinamico.content = ft.Column(controls=vinhos_favoritados)
        self.conteudo_dinamico.update()
        
    def main(self, page: ft.Page):
        page.on_route_change = lambda _: self.handle_routes(page)  
        page.go(page.route) 

