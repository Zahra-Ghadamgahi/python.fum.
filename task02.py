import random

def fill_list():
    n = int(input("Enter the length of the list: "))
    my_list= []

    while len(my_list) < n:
        random_number = random.randint(0,100)
        if random_number not in my_list:
            my_list.append(random_number)

    print(f"The list has been filled! list: {my_list}")

fill_list()
