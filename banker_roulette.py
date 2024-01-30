import random
names = input("type the names: ")
names_list = names.split(", ")

rand_int = random.randint(0, len(names_list)-1)

print(names_list[rand_int])

