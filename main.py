import csv
import os

os.system('clear')
os.system('rm -rf ./script.txt')

input_file = "source.csv"
outputfile = "script.txt"
string = ""
with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Type'] == "subnet":
            name = str(row['Name'])
            address = str(row['Network'])
            current_string = "config firewall address\nedit " + name + "\nset subnet " + address + "\n"
            string += current_string

outfile = open(outputfile, 'w')
outfile.write(string)
outfile.close()