import csv
t1 = open('/home/andre/Documents/nova_dica.csv', 'r')
t2 = open('/home/andre/Documents/nova_dica_2.csv', 'r')
fileone = t1.readlines()
filetwo = t2.readlines()
t1.close()
t2.close()

outFile = open('/home/andre/Documents/reult.csv', 'w')
x = 0
for i in fileone:
    if i != filetwo[x]:
        outFile.write(filetwo[x])
    x += 1
outFile.close()