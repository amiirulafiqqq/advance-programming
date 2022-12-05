import csv

file = open ("TitanicSurvival.csv","r")
data = list(csv.reader(file, delimiter=","))

file.close()

#print(data[-1]) #cara keluar kan last data
#print(data[-10:-1]), cara range

Mrleo = data [-1]
Mrleo.append('good person') #nak tambah dekat element
Mrleo[4] = ('1st') #tukar fourth element ke '1st'

print(Mrleo)

