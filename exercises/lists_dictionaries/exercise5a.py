alist = ["aaa", "bbb", "ccc", "ddd", "eee"]
blist = ["111", "222", "333", "444", "555"]
newlist = []

print(f"Η πρώτη λίστα είναι η:   {alist}")
print(f"Η δεύτερη λίστα είναι η: {blist}", end="\n\n")

blist.reverse()
newlist = list(zip(alist, blist))

print(f"Η νέα λίστα είναι η: {newlist}")