# HERE WE WILL TRY TO MAKE LIST USING FOR LOOP
import random

under_10=[x for x in range(10)]
print("under age of 10:"+ str(under_10))
# Get square value
squares=[x**2 for x in range(5)]
print("for every number in x the square of x: "+ str(squares))
# GET ODDS FOR EVERY NUMBER LESS THAN 10
odds=[x for x in range(10) if x%2 ==1]
print("odd numbers under 10=" +str(odds))
# Get all the numbers from a string
sentense="This senstense has 1 or 2 numbers lets just add more 8 and 26 to that "
nums=[x for x in sentense if x.isnumeric()]
print("The nums from the sentence:"+ str(nums))
print('the nums from the sentence joined:'+''.join(nums))
family=["girma","bekelech","kalkidan","getayawkal","yohannes"]
index=[k for k,v in enumerate(family) if v == "getayawkal"]
print("index of search is :",str(index))                                #you can use a comma or + sigh its the same("note"+str(index), or ("note",str(index)
## OK NOW WE ADD  GETAYAWKAL AND  KALKIDAN WE WILL PRINT THE THING AGAIN
## WE CAN PRINT THE INDEX WE WANT
fam=["girma","bekelech","kalkidan","getayawkal","yohannes"]
index=[k for k , v in enumerate(fam) if v=="getayawkal" or v=="kalkidan"]       #NOW WE HAVE TWO OUT PUTS
print("index of search:", str(index))
#print it by the index
print('index of search:'+ str(index[0]))
# DELETE AN ITEM FROM A LIST
letters=[x for x in 'abcdef']
# random.shuffle(letters)                   # This can shuffle it or you if you want
leters=[x for x in letters if x!='c']
print(letters,leters)
nums=[5,3,2,1,9,10,18]
new_list=[x if x%2 == 0  else x*10 for x in nums]       # if its divisible by to print the same no if not multiply by 10 and print
print (new_list)
