import http.client
import json
import collections
from seq import Seq

PORT = 80
SERVER = 'rest.ensembl.org'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

conn = http.client.HTTPConnection(SERVER, PORT)
conn.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

r1 = conn.getresponse()

print("Response received: {} {}\n".format(r1.status, r1.reason))

data = r1.read().decode("utf-8")

response = json.loads(data)
sequence = Seq(response['seq'])

pop = collections.Counter(sequence.strbases).most_common(1)[0]
popbase = pop[0]

#Printing the information
print("The sequence is: {}".format(sequence.strbases))
print("FRAT1 gene's length is: ", sequence.len())
print("Number of total thymine bases is :", sequence.count('T'))
print('The most popular base is: {}'.format(popbase))
print('Percentage of the most popular base,{}, is {} %'.format(popbase, sequence.perc(str(popbase))))
print ('Percentage of G:', sequence.perc('G'), '%')
print ('Percentage of A:', sequence.perc('A'), '%')
print ('Percentage of C:', sequence.perc('C'), '%')
print ('Percentage of T:', sequence.perc('T'), '%')



