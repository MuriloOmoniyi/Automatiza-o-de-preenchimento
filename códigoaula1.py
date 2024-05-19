#Anotar o passo a passo
#1- abrir o sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

#para instalar as bibliotecas: pip install 'pyautogui'(pyautogi é o nome da biblioteca muda dependendo da biblioteca)
import pyautogui #import é para importar a bibloteca para o código
import time


pyautogui.PAUSE = 0.7 #um delay para cada comando

#pyautogui.click -> clicar com o mouse 
    #pyautogui.click(x=75, y=546, clicks=2) -> aqui ele vai clicar 2 vezes na quela posição (pode ser quantas vezes quiser)
    #pyautogui.click(x=131, y=83, button="right") -> aqui voce vai clicar com o botão direito na determinada posição
#pyautogui.write -> escrever um texto 
#pyautogui.press -> pressionar uma tecla do teclado
#pyautogui.hotkeys -> apertar um conjunto de teclas (Ctrl C, Ctrl V, Alt Tab, e etc)
#pyautogui.drag -> ele serve para clicar e arrastar o mouse
#pytonautogui.moveTo -> ele serve para só mover o mouse, ele não clica segura e arrasta que nem o drag
#pyautogui.scroll -> ele serve para dar um scroll, numero positivo scroll para cima, número negativo scroll para baixo

#abrir o navegador(edge)
pyautogui.press("win");
pyautogui.write("edge");
pyautogui.press("enter");

#entra no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login");
pyautogui.press("enter");

#aqui pode ser qe demore alguns segundos para carregar o site (por causa da internet)
time.sleep(2);

#2- fazer login
pyautogui.click(x=724, y=489)
pyautogui.write("muriloomoniyi@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.click(x=949, y=706)

time.sleep(2);

#3-abrir/importar a base de dados de produtos pra cadastrar
# pip install pandas numpy openpyxl
#pandas.read_csv -> isso serve para ler uma base de dados, você pode escolher qual o tipo de arquivo, exel,jsom, no caso é csv
#para ler a gente usa variáveis, nesse caso vamos usar a variável tabela, ela fica fora de parenteses e aspas, ela ta sendoo usada para guardar as informações da leitura do pandas
#o comando tabulas transforma pdf em pandas
import pandas as pd

tabela = pd.read_csv("produtos.csv")


#4-cadastrar um produto
for linha in tabela.index:
    #tabela.index -> é para analisar as linhas da tabela
    #tabela.columns -> é para analisar as colunas de uma tabela
    #tabela.loc[linha,coluna] -> é para achar uma parte expecifica de uma tabela

    codigo = tabela.loc[linha,"codigo"]

    #clicar no campo do código do produto
    pyautogui.click(x=700, y=344)
    #preencher o código
    pyautogui.write(codigo)
    #passar para o próximo campo
    pyautogui.press ("tab")

    #preencher a marca
    pyautogui.write(tabela.loc[linha,"marca"])
    #passar para o próximo campo
    pyautogui.press ("tab")

    #preencher o tipo
    pyautogui.write(tabela.loc[linha,"tipo"])
    #passar para o próximo campo
    pyautogui.press ("tab")

    #preencher a categoria
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    #passar para o próximo campo
    pyautogui.press ("tab")

    #preencher o preço unitário
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    #passar para o próximo campo
    pyautogui.press ("tab")

    #preencher o custo do produto
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    #passar para o próximo campo
    pyautogui.press ("tab")

    obs = (str(tabela.loc[linha,"custo"]))
    if obs != "nan":
        #preencher as obs
        pyautogui.write
    #passar para o próximo campo
    pyautogui.press ("tab")
    #clicar em enviar
    pyautogui.press ("enter")
    #ele tem que dar um scroll para cima para poder começar de novo
    pyautogui.scroll(2000)

#5- repetir isso tudo até acabar a lista

 