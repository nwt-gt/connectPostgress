from csv import reader
import csv
import re
import sys

inputFileName = sys.argv[2]
print(inputFileName)
outputFileName = sys.argv[1]
print(outputFileName)

opened_file = open(inputFileName)
read_file = reader(opened_file)
data = list(read_file)
opened_file.close()
data = data[1:]

firstName = []
lastName = []
pricelist = []
above_100 = []
for name,price in data:
    names =re.split('(?<!,)\s' , name)
    if "Dr." in  names or "Mr." in names: 
        firstName.append(names[1])
        lastName.append(names[2])
    elif name in (None,""):
        continue
    else:
        firstName.append(names[0])
        lastName.append(names[1])
        
    pricelist.append(price.lstrip("0"))

for price in pricelist:
    if float(price) > 100:
        above_100.append(True)
    else:
        above_100.append(False)

rows = zip(firstName,lastName,pricelist,above_100)
results_list = list(rows)
print(results_list[0])
print(type(results_list))

csvfile=open(outputFileName,'w', newline='')
obj=csv.writer(csvfile)
obj.writerows([("firstName","lastName","price","Over_100")])
obj.writerows(results_list)
csvfile.close()
