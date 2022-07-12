import copy
initial_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
keys_list = ["b", "d"]
new_dict = {}

print(f"Το αρχικό λεξικό είναι το: {initial_dict}")
print(f"Η λίστα με τα κλειδιά προς αφαίρεση είναι η: {keys_list}", end="\n\n")

def remove_from_dictionary(initial_dict, keys_list):
    deep_copy_list = copy.deepcopy(initial_dict)
    
    for key in keys_list:
        deep_copy_list.pop(key)
    
    return deep_copy_list

print(f"Το λεξικό μετά την αφαίρεση των κλειδιών είναι το: {remove_from_dictionary(initial_dict, keys_list)}")
