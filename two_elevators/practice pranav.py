for i in numbers:
    for j in numbers:
        if(str(len(i))== str(len(j)) and i!=j):
            len_num = len(str(i))
            count = 0
            i = str(i)
            j = str(j)
            for k in range(len_num):
                if(i[k] == j[k]):
                    count +=1

            if(count== len_num-1):
                print(i,j)


