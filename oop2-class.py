import numpy as np
from opencage.geocoder import OpenCageGeocode

key = '09aadb1b1d8840acacfa0fcece0acb13'
geocoder = OpenCageGeocode(key)


class CSVFile():

	def __init__(self):
		self.arquivo = None
		self.data = list()

	def read_file(self,filePath):

		try: 
			f = open(filePath,"r")
			data = f.readlines()
			self.data = list(  map(lambda line: line.split(";"), data) )
			f.close()

		except IOError as e:
			print (e.args)			
			return None


	def transpose(self):
		return np.matrix(self.data).transpose().tolist()

	def empty_cell(self,cell):
		return cell=="Sem Informações" or cell == ""

	def number_empty_lines(self, transposed):
		aux = list()
		for line in transposed:
			aux.append(list(filter(self.empty_cell, line)))
		return list(map(len,aux))
		
	def mean_empty_lines(self):
		transposed = self.transpose() 
		return np.mean(self.number_empty_lines(transposed))
	

class Functions():
	
	def __init__(self, cfile):
		self.cfile = cfile
		self.data = self.cfile.data

	def tax_init_end(self):
		return self.data[0].index("Filo"), self.data[0].index("Especie")

	def tax_level(self):
		aux = {}
		init,end = self.tax_init_end()	
		
		for i, line in enumerate(self.data):
			for ind in range(init,end+1):
				if self.cfile.empty_cell(line[ind]):
					aux[i]= self.data[0][ind-1]
					break 
			aux[i] = self.data[0][ind]
		return aux	
	
	def filters(self,filtertype,value):
		column =  self.data[0].index(filtertype)
		return ( list ( filter ( lambda x: x[column] == value , self.data) ))



if __name__ == "__main__":
	
	filePath = "portalbio_export_16-10-2019-14-39-54.csv"
	cfile = CSVFile()
	cfile.read_file(filePath)
	#print(cfile.mean_empty_lines())

	func = Functions(cfile)
	#print(func.tax_level())

	print ("Example Filter: Estado/Provincia Value: PE")
	filtertype = input("Filter(Estado/Especie/Ameaca): ")
	value = input("Value: ")
	print(func.filters(filtertype,value))

	print(geocoder.reverse_geocode(44,-1))
	

	
	




		
