import pyautogui
from time import sleep
import subprocess

#Define o diretório para abrir o arquivo
programa_cadastro = (r'C:/Users/aghas/Desktop/Freelancer/Automação Cadastro/exe.win-amd64-3.10/app.exe')
#Define o diretório para buscar os produtos
caminho_produtos = (r'C:/Users/aghas/Desktop/Freelancer/Automação Cadastro/produtos.txt')
#Abre o programa do cadastro
subprocess.Popen(programa_cadastro)
sleep(1)
usuario = ('nickolas')
senha = ('1234')
clique_produto = 619,527
clique_quantidade = 623,557
clique_preco = 616,591
#Cadastrar usuario
pyautogui.click(978,609, duration=0.5)
sleep(0.5)
pyautogui.write(usuario)
#Clique na senha e cadastro da senha
pyautogui.click(967,573,duration=0.5)
pyautogui.write(senha)
#Clique em registrar
pyautogui.click(894,610,duration=0.4)
#Clique no usuario e digita o usuario
pyautogui.click(962,542,duration=0.5)
pyautogui.write('nickolas')
sleep(0.5)
#Clique na senha e digita a senha
pyautogui.click(966,575,duration=0.5)
pyautogui.write('1234')
sleep(0.5)
#Clica em entrar
pyautogui.click(849,609,duration=0.5)
sleep(1)
#Lê o conteudo do arquivo .txt
with open(caminho_produtos, 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0] #Define a linha de produto antes da virgula
        quantidade = linha.split(',')[1] #Define a linha de quantidade antes da virgula
        preco = linha.split(',')[2] #Define a linha de preco depois da virgula
        pyautogui.click(clique_produto, duration=0.2) #Clica na aba de produtos e digita o item do produto
        pyautogui.write(produto)
        sleep(0.2)
        pyautogui.press('Tab') #Pressiona tab para pular para próxima aba de quantidade e repete o processo do produto
        pyautogui.write(quantidade)
        sleep(0.2)
        pyautogui.press('Tab') #Pressiona tab para pular para próxima aba de preço e repete o processo do produto
        pyautogui.write(preco)
        sleep(0.2)
        pyautogui.click(503,785, duration=0.2) #Clica na aba de enviar produto 
        sleep(0.2)

input('Digite enter para fechar')
