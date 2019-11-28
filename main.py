from functions import *

acoes_Validas = ['MSFT', 'GOGL', 'AMZN', 'TSLA']

option = int(input('Entre ação: '))
for i in range(0, 4):
    if i == option:
        acao = acoes_Validas[i]

#TODO
# Adicionar uma interface com 4 botões para selecionar as ações validas


if acao not in acoes_Validas:
    print('Essa ação não é valida. ') #A principio é só pra testes


plot(acao, 'GOOGLE')
"""
comprar, vender = analiseMedia(acao)
if comprar == True:
   print('Compre')
elif vender == True:
   print('Venda')
else:
   print('Não faça nada, é incerto.')
"""