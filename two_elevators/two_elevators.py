

num = int(input(""))

for i in range(num):
    len, query= input("").split()
    len = int(len)
    query = int(query)

    arr = input("").split()

    odd_count = 0
    even_count = 0

    for i in arr:
        if(int(i)%2 == 0):
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    
    for i in range(query):
        a,b = input("").split()

        a = int(a)
        b = int(b)


            






