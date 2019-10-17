import numpy as np
import sys

def read_file (arquivoPath):
	
	arquivo = None
	dados = list()

	try:
		arquivo = open(arquivoPath, "r")
		dados = arquivo.readlines()
		
	except IOError as e:
		print(e.args)
		return None

	arquivo.close()

	return list(  map(lambda linha: linha.split(";"),  dados ) )

def isEmpty(x):
	return x == "Sem Informações" or x == ""

def nEmpty(dataFrame):
	aux = list()
	for linha in dataFrame:
		aux.append( list(filter( isEmpty ,  linha ) ) )
		
	return list(map(len,aux))

def mean_empty(dataFrame):
	return np.mean (nEmpty(dataFrame))


def transpose(dataFrame):
	return np.matrix(dataFrame).transpose().tolist()

def tax_init_end(dados):
	return dados[0].index("Filo"), dados[0].index("Especie")

def tax_level(dados):
	aux = {}
	init,fim = tax_init_end(dados)	
	print(init,fim)
	for i, line in enumerate(dados):
		for ind in range(init,fim+1):
			if isEmpty(line[ind]):
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
	data = read_file(filename)
	transpost = transpose(data)
	#print(mean_empty(transpost))
	print(tax_level(data))
	
	#filtro  = input("filtro: (estado/especie/ameaca) ")
	#valor = input("valor: ")
	#print(filtro_estados(data,filtro,valor))

	
	



