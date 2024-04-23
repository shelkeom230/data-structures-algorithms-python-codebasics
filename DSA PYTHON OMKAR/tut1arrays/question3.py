#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function


max_number=int(input("enter a max range: "))
print([i for i in range(max_number) if i%2!=0])