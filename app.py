#Passo a passo do projeto
#Passo 1: Entrar no sistema da empresa
    #linkdositedaempresa.com
    #pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5

#abrir o navegador

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

#espere um pouco

time.sleep(1)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#Dar uma pausa um pouco maior

time.sleep(3)

#Passo 2: Fazer Login

pyautogui.click(x=596, y=353)
pyautogui.write("emailgenerico@gmail.com")

#escrever a senha

pyautogui.press("tab")
pyautogui.write("suasenhaaqui")

#clicar no botão de logar

pyautogui.click(x=667, y=523)
time.sleep(3)

#Passo 3: Importar a base de dados
#pip install pandas numpy openpyxl

import pandas
tabela = pandas.read_csv("produtos.csv")

#Passo 4: Cadastrar 1 produto
#para cada linha da minha tabela

for linha in tabela.index:

    #clicar no primeiro campo

    pyautogui.click(x=467, y=238)

    #codigo do produto
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    #categoria
    #precisa transformar em string
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #preço
    #precisa transformar em string
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #custo
    #precisa transformar em string
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(tabela.loc[linha, "obs"])
    pyautogui.press("tab")

    #enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

#Passo 5: Repetir o processo de cadastro até acabar
        

