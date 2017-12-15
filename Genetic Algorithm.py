#ECC4303 AI project from 
# 179435 CHOO HONG YEE
# 176555 CHANG JIT SHENG

import random
import string
import itertools
import operator
from collections import OrderedDict

# initialize array
array_dec = []
array_bin = []
new_array_bin = []
fitness_value_array = []
paired_array_bin = []
even_array_bin = []
odd_array_bin = []
new_array_dec = []
value_of_x = []
dictionary={}
new_fitness_value_array = []
TRIALS = 50
highest_fv =0
counts=0
stable_count=0


if __name__ == "__main__":
    value_of_x = random.sample(range(0, 31), 10)
    for i in value_of_x:
        b = bin(i)[2:].zfill(5)  # convert decimal into binary
        array_bin.append(b)  # append the bin into an array
        new_array_bin.append(b)
        new_array_dec.append(i)

    for trials in range(TRIALS):

        if stable_count>5:
            quit()

        print("array_bin")
        print(array_bin)
        print("new_array_bin")
        print(new_array_bin)
        print("new_array_dec")
        print(new_array_dec)


        fitness_value_array=[]
        for i in new_array_dec:
            x = i  # parse data into new variable to be use in equation
            fitness_value = (x ** 3) - 60 * (x ** 2) + (900 * x) + 100  # calculate fitness value
            fitness_value_array.append(fitness_value)  # create array with fitness value
            dictionary = dict(zip(fitness_value_array, new_array_bin))  # create dictionary with fitness value and array bin


        print(fitness_value_array)
        print(dictionary)
        # sort fitness value array
        fitness_value_array = sorted(fitness_value_array, reverse=True)
        print(fitness_value_array)

        if highest_fv<fitness_value_array[0]:
            highest_fv = fitness_value_array[0]
            TRIALS+=1
            stable_count = 0

        elif highest_fv==fitness_value_array[0]:
            stable_count+=1

        else:
            stable_count=0
            counts+=1


        # sort dictionary
        dictionary = sorted(dictionary.items(), key=operator.itemgetter(0), reverse=True)

        # get value of binary based on fitness value
        x=0
        for key, value in dictionary:
            new_array_bin[x]=value
            x+=1

        print(dictionary)
        print(highest_fv)
        print(counts)
        print("new_array_bin")
        print(new_array_bin)
        # create 2 new arrays in knowing the arrangement of binary number descending order
        for i in range(0, 10):
            if i % 2 == 0:
                even_array_bin.append(new_array_bin[i])
            else:
                odd_array_bin.append(new_array_bin[i])

        x = 0  # initiate variable
        for i in range(0, 5):
            first = even_array_bin[i]  # take value from 2 arrays
            second = odd_array_bin[i]
            pc = random.uniform(0, 1)  # generate pc
            if pc > 0.8:  # if greater than pc will do crossover
                pos = int(random.randint(0, 4))
                crossover = first
                first = first[:pos] + second[pos] + first[pos + 1:]
                second = second[:pos] + crossover[pos] + second[pos + 1:]
                even_array_bin[i] = first  # store into the 2 array
                odd_array_bin[i] = second

            else:
                print("not found")

            # generate pm for even array
            pm = random.uniform(0, 1)
            if pm < 0.001:
                pos = int(random.randint(0, 4))
                first[pos] != first[pos]
                first = first[:pos] + first[pos] + first[pos + 1:]
                even_array_bin[i] = first
                print("mutation:")
                print(first)

            # generate pm for odd array
            pm = random.uniform(0, 1)
            if pm < 0.001:
                pos = int(random.randint(0, 4))
                second[pos] != second[pos]
                second = second[:pos] + second[pos] + second[pos + 1:]
                odd_array_bin[i] = second
                print("mutation:")
                print(second)

        # store into the main array
        for i in range(0,10):
            if i%2==0:
                new_array_bin[i] = even_array_bin[int(i/2)]
            elif i%2!=0:
                new_array_bin[i] = odd_array_bin[int((i-1)/2)]


        # store latest binary value into decimal array
        for i in range(0, 10):
            new_dec = int(new_array_bin[i], 2)
            new_array_dec[i]=new_dec

        print("-----------------------------------------------")
        print("new_array_bin")
        print(new_array_bin)
        print("new_array_dec")
        print(new_array_dec)
        print(trials)
        print("----END--------------------------------------")




