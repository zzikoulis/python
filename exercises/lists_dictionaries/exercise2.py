alist = ["aaa", "bbb", "ccc", "ddd", "eee"]
blist = ["111", "222", "333", "444", "555"]
conlist = []

print(f"Η πρώτη λίστα είναι η:   {alist}")
print(f"Η δεύτερη λίστα είναι η: {blist}", end="\n\n")

for i in range(len(alist)):
    conlist.append(alist[i] + blist[i])

print(f"Η συνένωση των 2 παραπάνω λιστών είναι η: {conlist}")