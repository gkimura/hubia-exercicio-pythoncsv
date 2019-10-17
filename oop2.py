import numpy as np

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
		print(linha)
		aux.append( list(filter( verificarVazio ,  linha ) ) )
		
	return list( map(len, aux) )


	
def meanlimpa(dataFrame):
	return np.mean ( limpa(dataFrame) )


def transpose(dataFrame):
	return np.matrix(dataFrame).transpose().tolist()


	
filename = "portalbio_export_16-10-2019-14-39-54.csv"
dados = fastread(filename)
transposta = transpose(dados) 
print(limpa(transposta))
