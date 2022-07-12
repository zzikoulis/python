initial_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
tuple_for_extension = ("h", "i", "j")

print(f"Η αρχική λίστα είναι η:  {initial_list}")
print(f"Η πλειάδα που θα χρησιμοποιηθεί για επέκταση είναι η: {tuple_for_extension}", end="\n\n")

initial_list[2][1][2].extend(tuple_for_extension)

print(f"Η λίστα μετά την επέκταση είναι η:  {initial_list}")

