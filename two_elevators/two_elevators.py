
# Open a file: file
file = open('read.txt',mode='r')
 
# read all lines at once
all_of_it = file.read()


all_of_it = all_of_it.split('\n\n')
maxs = 0
individual_calories = []

for i in all_of_it:
    max_sum=0
    i = i.split()
    for j in i:
        max_sum = max_sum + int(j)
    individual_calories.append(max_sum)
    
    
#print(individual_calories)

for i in range(3):
    maxs = maxs + max(individual_calories)
print(maxs)
    


# print(max)


