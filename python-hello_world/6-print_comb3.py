# i = range(10)
# j = range(10)
# for i in range(10):
#     for j in range(10):
#         if i < 10: 
#             print("{:01d}{}".format(i,j), end=", ")
#         #     i +=1
#         # else:
#         #     print("{}{}".format(i,j), end="\n")

for i in range(0, 10):
        for j in range(i + 1, 10):
            combination = str(i) + str(j)
            if int(combination)<89:
                print("{}".format(combination), end=", ")
            else:
                print("{}".format(combination), end="\n")
