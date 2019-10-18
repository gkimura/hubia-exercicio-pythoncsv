import numpy as np
from opencage.geocoder import OpenCageGeocode

key = '09aadb1b1d8840acacfa0fcece0acb13'
geocoder = OpenCageGeocode(key)

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

def tax_init_end(data):
	return data[0].index("Filo"), data[0].index("Especie")

def tax_level(data):
	aux = {}
	init,end = tax_init_end(data)	
	print(init,end)
	for i, line in enumerate(data):
		for ind in range(init,end+1):
			if isEmpty(line[ind]):
				aux[i]= data[0][ind-1]
				break 
		aux[i] = data[0][ind]
	return aux

def filters(data, filtertype, value):
	column =  data[0].index(filtertype)
	return ( list ( filter ( lambda x: x[column] == value , data) ))
	

#def localidade():



if __name__ == "__main__":
	
	filename = "portalbio_export_16-10-2019-14-39-54.csv"
	data = read_file(filename)
	transpost = transpose(data)
	""" 
	print(mean_empty(transpost))
	print(tax_level(data))

	# Exemplo : Filtro "Estado/Provincia" Valor: PE
	filtertype  = input("filter: (estado/especie/ameaca) ")
	value = input("valor: ")
	print(filters(data,filtertype,value))
	"""
	print(geocoder.reverse_geocode(44,-1))

	
	



