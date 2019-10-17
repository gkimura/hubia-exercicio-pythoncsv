import numpy as np
import sys

def fastread (arquivoPath):
	
	arquivo = None

	dados = list()

	try:
		
		arquivo = open(arquivoPath, "r")
		
		dados = arquivo.readlines() # cast list()
		
		
	except IOError as e:
		print(e.args)

		return None

	
	arquivo.close()

	return list(  map(lambda linha: linha.split(";"),  dados ) )


# lambda = *void


def verificarVazio(x):
	return x == "Sem Informações" or x == ""


def limpa(dataFrame):
	aux = list()
	for linha in dataFrame:
		aux.append( list(filter( verificarVazio ,  linha ) ) )
		
	return list( map(len, aux) )


def meanlimpa(dataFrame):
	return np.mean (limpa(dataFrame))


def transpose(dataFrame):
	return np.matrix(dataFrame).transpose().tolist()

def inicio_fim_tax(dados):
	return dados[0].index("Filo"), dados[0].index("Especie")

def nivel_tax(dados):
	aux = {}
	init,fim = inicio_fim_tax(dados)	
	print(init,fim)
	for i, line in enumerate(dados):
		for ind in range(init,fim+1):
			if verificarVazio(line[ind]):
				aux[i]= dados[0][ind-1]
				break 
		aux[i] = dados[0][ind]
	return aux

def filtro_estados(dados, filtro, valor):
	colunaEstados =  dados[0].index(filtro)

	return ( list ( filter ( lambda x: x[colunaEstados] == valor , dados) ))
	

#def localidade():



if __name__ == "__main__":
	
	filename = "portalbio_export_16-10-2019-14-39-54.csv"
	dados = fastread(filename)
	transposta = transpose(dados)
	#print(meanlimpa(transposta))
	#print(nivel_tax(dados))
	
	#filtro  = input("filtro: (estado/especie/ameaca) ")
	#valor = input("valor: ")
	#print(filtro_estados(dados,filtro,valor))

	
	



