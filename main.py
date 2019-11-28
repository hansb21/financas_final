from functions import *
from menu import *

acoes_Validas = ['MSFT', 'GOGL', 'AMZN', 'TSLA']
nomes = ['Microsoft', 'Google', 'Amazon', 'Tesla']

menu = Menu(1366,768)
menu.open()
if menu.run():
	option = menu.getStonks()
	for i in range(0, 4):
		if i == option:
			acao = acoes_Validas[i]
			nome = nomes[i]
	plot(acao, nome)
