#Given a list `given_list` and a number N, 
# create a new list that contains each number of `given_list` at most N times 
# without reordering. 
# For example if N = 2, and the input is [1,2,3,1,2,1,2,3], 
# you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, 
# and then take 3, which leads to [1,2,3,1,2,3].
# Hint: You may need to enumerate the list.
given_list = [1,2,3,1,2,1,2,3] 
number = 2
newlist = []
if number ==0:print ([])
elif number == 1:
    newlist = [*set(given_list)]
    print (newlist)
elif  number >= 2:
    for a in given_list:
        if given_list.count(a) > number:
           given_list.reverse()  
           given_list.remove(a)
           given_list.reverse()                      
    print (given_list)
  





