import pandas as pd

file = pd.read_excel("Форма для преподавателей (Ответы).xlsx", index_col=0)
f = open("d.txt", "w")

for address in file.index:
    f.write ("--------------------------------------------\n")
    f.write (str(address))
    for column in file.columns:
        f.write (" \n")
        f.write ("---" + column + "\n")
        f.write (str(file[column][address]))
        print (str(file[column][address]))
    f.write (" \n")