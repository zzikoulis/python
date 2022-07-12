alist = [1, 'one', 2, ('a','b','c'), ['!', '@', '%']]
rlist = []

print(f"Η αρχική λίστα είναι η: {alist}", end="\n\n")

for i in range(len(alist) - 1, -1, -1):
    rlist.append(alist[i])

print(f"Η ανάποδη λίστα είναι η: {rlist}")



