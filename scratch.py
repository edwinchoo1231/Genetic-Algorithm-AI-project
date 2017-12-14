import random
import string
import itertools
import operator
from collections import OrderedDict

def get_random_pairs(numbers):
    # Generate all possible non-repeating pairs
    pairs = list(itertools.combinations(numbers, 2))

    # Randomly shuffle these pairs
    #random.shuffle(pairs)
    return pairs

#initialize array
array_dec=[]
array_bin=[]
new_array_bin=[]
fitness_value_array=[]
paired_array_bin=[]
even_array_bin=[]
odd_array_bin=[]

#initiallize dictionary
dictionary={11}

#generate random 10 numbers that do not duplicate
trial = random.sample(range(0, 31),10)
print(trial)

for i in trial:
    b= bin(i)[2:].zfill(5)          #convert decimal into binary
    array_bin.append(b)             #append the bin into an array
    x = i                           #parse data into new variable to be use in equation
    fitness_value = (x ** 3) - 60 * (x ** 2) + (900 * x) + 100          #calculate fitness value
    fitness_value_array.append(fitness_value)                   #create array with fitness value
    dictionary = dict(zip(fitness_value_array,array_bin))       #create dictionary with fitness value and array bin

print(array_bin)
print(fitness_value_array)
print(dictionary)

#sort fitness value array
fitness_value_array=sorted(fitness_value_array, reverse=True)
#sort dictionary
dictionary=sorted(dictionary.items(), key=operator.itemgetter(0),reverse=True)
#get value of binary based on fitness value
for key,value in dictionary:
    new_array_bin.append(value)

print("---------------------------------------")
print(fitness_value_array)
print(dictionary)
print(new_array_bin)

#create 2 new arrays in knowing the arrangement of binary number descending order
x=0
for i in range(0,10):
    if i%2==0:
        even_array_bin.append(new_array_bin[i])
    else:
        odd_array_bin.append(new_array_bin[i])

print (even_array_bin)
print (odd_array_bin)
print("---------------------------------------") #divider
x=0 #initiate variable
for i in range(0,5):
    first = even_array_bin[i] #take value from 2 arrays
    second = odd_array_bin[i]
    pc = random.uniform(0,1) #generate pc
    print (pc)
    if pc>0.8: #if greater than pc will do crossover
        pos = int(random.randint(0, 4))
        crossover = first
        first=first[:pos] + second[pos] + first[pos+1:]
        second=second[:pos] + crossover[pos] + second[pos+1:]
        even_array_bin[i] = first #store into the 2 array
        odd_array_bin[i] = second

    else:
        print("not found")
    pm = random.uniform(0,1) #generate pm for even array
    if pm<0.001:
        pos = int(random.randint(0, 4))
        first[pos] != first[pos]
        first = first[:pos] + first[pos] + first[pos + 1:]
        even_array_bin[i] = first
        print (first)
    pm = random.uniform(0, 1)  # generate pm for odd array
    if pm < 0.001:
        pos = int(random.randint(0, 4))
        second[pos] != second[pos]
        second = second[:pos] + second[pos] + second[pos + 1:]
        odd_array_bin[i] = second
        print(second)
    #store into the main array
    new_array_bin[x] = even_array_bin[i]
    new_array_bin[x + 1] = odd_array_bin[i]
    x += 2  # increament for main array (storing purposes)

print(even_array_bin)
print(odd_array_bin)
print(new_array_bin)