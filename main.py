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
        address = str(row['address'])
        mask = str(row['mask'])
        if mask == "None":
            current_string = "config firewall address\nedit " + address + "\nset comment comment\nset subnet " + address + "/32\nnext\nend\n\n"
        else:
            current_string = "config firewall address\nedit " + address + "m" + mask + "\nset comment comment\nset subnet " + address + "/" + mask + "\nnext\nend\n\n"
        string += current_string

outfile = open(outputfile, 'w')
outfile.write(string)
outfile.close()