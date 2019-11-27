from functions import *

acoes_Validas = ['MSFT', 'GOGL', 'AMZN', 'TSLA']

#TODO
# Adicionar uma interface com 4 botões para selecionar as ações validas
acao = 'AMZN'

if acao not in acoes_Validas:
    print('Essa ação não é valida. ') #A principio é só pra testes


plot(acao)