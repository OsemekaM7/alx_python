for i in range(0, 10):
        for j in range(i + 1, 10):
            combination = str(i) + str(j)
            if int(combination)<89:
                print("{}".format(combination), end=", ")
            else:
                print("{}".format(combination), end="\n")
