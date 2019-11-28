from functions import *

acoes_Validas = ['MSFT', 'GOGL', 'AMZN', 'TSLA']
nomes = ['Microsoft', 'Google', 'Amazon', 'Tesla']

option = int(input('Entre ação: '))
for i in range(0, 4):
    if i == option:
        acao = acoes_Validas[i]
        nome = nomes[i]

#TODO
# Adicionar uma interface com 4 botões para selecionar as ações validas


plot(acao, nome)
