import pandas as pd
from pandas import DataFrame
import zipcode

def txt_to_dict(file_name):
    f = open(file_name)
    L = f.readlines()
    column = L[0][3:-1]
    L = L[1:]
    data = {}

    #extract variable names from txt
    names = column.split('\t')
    for m in range(len(names)):
        if "zip" in names[m].lower():
            index = m
    for variable_name in names:
        data[variable_name] = []

    for i in range(len(L)):
        variable = L[i][:-1].split('\t')
        try:
            myzip = zipcode.isequal(variable[m])
            code = int(variable[m][0:3])
            if (len(variable[m]) == 5) & (199 < code < 205):
                state = "DC"
                print(state)
            elif (len(variable[m]) == 5) & (204 < code < 220):
                state = "MD"
            elif (len(variable[m]) == 5) & (479 < code < 500):
                state = "MI"
            elif (len(variable[m]) == 5) & (variable[m][0:3] == "276"):
                state = "NC"
            else:
                state = myzip.state
            for j in range(len(variable)):
                if j == m:
                    data[names[j]].append(state)
                else:
                    data[names[j]].append(variable[j])
        except:
            continue

    data_pd = DataFrame(data, columns=names)
    print (data_pd)
    return data_pd

def output(data, outfile):
    data.to_csv(outfile, index = False)

def main():
    file_name = input("Enter file name: ")
    outfile = input("Enter outfile name: ")
    data = txt_to_dict(file_name)
    output(data, outfile)

if __name__ == "__main__": main()
