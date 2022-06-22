while True:
    try:
        loops_number = int(input("Παρακαλώ εισάγετε έναν θετικό ακέραιο αριθμό επαναλήψεων: "))
        if loops_number <= 0:
            print("Παρακαλώ εισάγετε θετικό αριθμό και όχι αρνητικό ή μηδέν!")
            print()
            continue
        break
    except ValueError:
        print("Παρακαλώ εισάγετε μόνο θετικό ακεραίο ΑΡΙΘΜΟ και όχι χαρακτήρες!")
        print()

print("\nΟ συνολικός αριθμός επαναλήψεων είναι: {}".format(loops_number))

for i in range(1, loops_number + 1):
    print("Τρέχων αριθμός: {}\tΠροηγούμενος αριθμός: {}\tΤο άθροισμα τους: {}"
    .format(i, i - 1, 2 * i -1))