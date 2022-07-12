alist = ["aaa", "bbb", "ccc", "ddd", "eee"]
blist = ["111", "222", "333", "444", "555"]
newlist = []

print(f"Η πρώτη λίστα είναι η:   {alist}")
print(f"Η δεύτερη λίστα είναι η: {blist}", end="\n\n")

for i in range(len(alist)):
    for j in range(len(blist)):
            newlist.append((alist[i], blist[j]))

print(f"Η νέα λίστα είναι η: {newlist}")