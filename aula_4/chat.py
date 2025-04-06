import flet as ft

# Criar uma função principal para rodar o  app 
def main(pagina):
  titulo = ft.Text("BlackZap") 
  pagina.add(titulo)

  def websocket(msg): 
    texto = ft.Text(msg)
    chat.controls.append(texto)
    pagina.update()

  pagina.pubsub.subscribe(websocket)

  def enviar_mensagem(event):
    nome_usuario = caixa_nome.value
    texto_campo_mensagem = campo_enviar_mensagem.value
    msg = f"{nome_usuario}: {texto_campo_mensagem}"
    pagina.pubsub.send_all(msg)

    campo_enviar_mensagem.value = ""
    pagina.update()

  campo_enviar_mensagem = ft.TextField(label="Digite sua mensagem aqui")
  botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

  linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar_mensagem])

  chat = ft.Column()

  def entrar_no_chat(event):
    nome = caixa_nome.value
    print(f"Bem vindo, {nome}!")
    popup.open = False 
    pagina.remove(titulo)
    pagina.remove(botao)

    pagina.add(chat)
    pagina.add(linha_enviar)

    nome_usuario = caixa_nome.value
    msg = f"{nome_usuario} entrou no chat"
    pagina.pubsub.send_all(msg)
    # texto_msg = ft.Text(f"{nome_usuario} entrou no chat")
    # chat.controls.append(texto_msg)

    pagina.update()

  # criar popup 
  titulo_popup = ft.Text("Bem vindo")
  caixa_nome = ft.TextField(label="Digite o seu nome")
  botao_popup = ft.ElevatedButton("Entrar no chat", on_click=entrar_no_chat)

  popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

  def abrir_popup(event):
    pagina.dialog = popup
    popup.open = True
    pagina.update()
    print("Clicou")

  botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
  pagina.add(botao)
# Executra a função com flet
ft.app(main, view=ft.WEB_BROWSER)