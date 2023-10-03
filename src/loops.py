#For loop practice
#question:Your little brother has just learned multiplication tables in school. Today he has learned tables of 6 and 7. 
# Help him memorise both the tables by printing them using for loop.

# Write your code here
print("Table of 6:")
for i in range(11):
    print('6 *',i,"=",6*i)
print("Table of 7:")
for i in range(11):
    print('7 *',i,"=",7*i)

#while loop practice

#question:The following is a list of animals in a National Zoo. Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
#Your brother needs to write an essay on the animals whose names are made of 7 letters. 
# Help him find those animals through a while loop and create a separate list of such animals.

# Write your code here
animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
new = []
i = 0
while (i< len(animals)):
    j = animals[i]
    if(len(j) == 7):
        new.append(j)
    i = i+1
print(new)
