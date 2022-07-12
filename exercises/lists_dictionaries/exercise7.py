from hashlib import new


alist = ["a", "b", "c", "d", "e"]
blist = [1, 2, 3, 4, 5]
newdict = {}

print(f"Η πρώτη λίστα είναι η:   {alist}")
print(f"Η δεύτερη λίστα είναι η: {blist}", end="\n\n")

for i in range(len(alist)):
    newdict[alist[i]] = blist[i]

print(f"Το λεξικό που προκύπτει από τις 2 λίστες είναι το: {newdict}")