# we can creat it easly as
x=list()
y=['a',2,'dog',3.14]
tuple=('man','woman',2)
z=list(tuple)
x.append(4)
print(x)            #this gives empty list
print(y)            #this gives us y
print(z)            #this will give us the tuple in list form



# we can also make list by using for loops
# ALSO called list comprehensions
# if we write the for loop inside the brackets
a=[the_number for the_number in range(8)]     #this will give you a number for every number it gets less than 8
print(a)
b=[x for any_number in range(8)]             #this will give you an empty list for every number it gets less than 8
print(b)
c=[y for any_number in range (3)]            #this will give you the value of y for every number it gets less than 3
print(c)
d=[the_number ** 2 for the_number in range(8)]
print(d)                                     #thsi will square the number for every number it gets less than 8

#

# now lets see how we insert an item in to a list
x=[2,5,9,4]
x.insert(2,'mama')      #   x.insert(the index you want to put it at , the thing you want to insert)
print(x)
# you can insert a list with in a list
x=[5,6,3,2]
x.insert(2,['a','m'])
print(x)

# POP (you can pop an item)
# if you just say pop it pops the last item by default
# if you put the index you want to pop it will do that for you
x=[2,6,7,9]
x.pop()                         # This just pops off the last item if you print x it just shows you the list with out 9
print(x)                        # This wont show you the number 9 (the number you popped) , (it shows you what it looks like after you pop it out)
print(x.pop())                  # This shows you or prints the number you popped and not the list
print(x.pop(0))                 # this shows you the number you popped with your index choice
print(x)                        # Noitice that only 6 is left in the list
# Remove
x=[1,3,5,3,4]
x.remove(3)                     # It only removes the first 3
print(x)

# Reverse
x=[1,2,3,4,5]
x.reverse()
print(x)

## Sort
x=[6,4,8,9]
x.sort()
print(x)
# Reverse Sort                  # Sorts in desending order
x=[5,3,8,6]
x.sort(reverse=True)
print(x)
print(x[2])                     # print using the index