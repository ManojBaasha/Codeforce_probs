
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

maxs1 = max(individual_calories)
individual_calories.remove(maxs1)
maxs2 = max(individual_calories)
individual_calories.remove(maxs2)
maxs3 = max(individual_calories)

print(maxs1+maxs2+maxs3)
    


# print(max)


