import pyautogui
import time
import pandas

pyautogui.PAUSE = 1
# print(pyautogui.size())

# pyautogui.click -> Clicar
# pyautogui.press -> pressionar tecla
# pyautogui.write -> inserir textp
# pyautogui.hotkey -> atalho de teclado (ctrl, C)
# pyautogui.scroll -> rolagem do mouse

# Abrir o sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("firefox") 
pyautogui.press("enter") 

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") 
pyautogui.press("enter") 

# Pausa o código por tempo determinado
time.sleep(1)

# Fazer login
pyautogui.click(x=2669, y=398) # Email
pyautogui.write("aoba@aoba.com") 
pyautogui.click(x=2711, y=499) # Senha
pyautogui.write("aoba@123") 
pyautogui.press("enter") 
time.sleep(1)

# Importar a base de dados de podutos
tabela = pandas.read_csv(r"D:\Backup\Documents\Backend\hashtag\jornada-python\aula_1\produtos.csv")
def next_input(input_txt): 
	pyautogui.press("tab") 
	text = str(input_txt)
	pyautogui.write(text if text != "nan" else "")

# Cadastrar 1 produto
for linha in tabela.index:
	# Produto
	codigo = tabela.loc[linha, "codigo"]
	pyautogui.click(x=2672, y=290) 
	pyautogui.write(str(codigo)) 

	marca = tabela.loc[linha, "marca"]
	next_input(marca)

	tipo = tabela.loc[linha, "tipo"]
	next_input(tipo)

	categoria = tabela.loc[linha, "categoria"]
	next_input(categoria)

	preco_unitario = tabela.loc[linha, "preco_unitario"]
	next_input(preco_unitario)

	custo = tabela.loc[linha, "custo"]
	next_input(custo)

	obs = tabela.loc[linha, "obs"]
	next_input(obs)

	pyautogui.press("enter") 


# Repetir até acabar todoso os produtos