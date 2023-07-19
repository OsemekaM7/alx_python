i = range(100)
for i in range(100):
    if i <99: 
        print("{:02d}".format(i), end=",")
        i +=1
    else:
        print("{:02d}".format(i), end="\n")

