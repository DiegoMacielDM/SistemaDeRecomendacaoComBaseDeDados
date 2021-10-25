from recomendacao import *
'''
print(euclidiana(avaliacoesUsuario, 'Pedro', 'Janaina'))
print("------------------")
print(euclidiana(avaliacoesFilme, 'Star Wars', 'Star Trek'))
print("------------------")
print(avaliacoesFilme['Star Wars'])
print("------------------")
print(getSimilares(avaliacoesUsuario, 'Pedro'))
print("------------------")
print(avaliacoesFilme, 'Star Wars')
print("------------------")
print(getRecomendacoes(avaliacoesUsuario, 'Leonardo'))
print("------------------")
print(getRecomendacoes(avaliacoesFilme, 'Star Trek'))

'''

base = carregaMovieLens()
print(getSimilares(base, '212'))
print("------------------")
print(getSimilares(base, '1'))
print("------------------")
print(getRecomendacoes(base, '212'))
print("------------------")
print(getRecomendacoes(base, '1'))
print("------------------")



