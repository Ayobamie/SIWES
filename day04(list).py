
#Python list
#In python, list can be treated like an array
#List operations
#-> append, remove, loop, search, copy, count
#-> extend, index, pop, reverse, sort
# How to declare a list
# Note: In python ,list can store values of multiple
# datatypes
mylist = [ 1, 43, 34, 4, 18, 90, 3.142, "jerry", True]
print(len(mylist))
print(mylist)
print("after appending")
print("after removing")
mylist.remove(3.142)
print(mylist)
mylist.pop()
print(mylist)
mylist.pop(1)
print(mylist)
mylist.insert(1,"new logo")
print(mylist)
mylist[3] = 333
print(mylist)
newlist = mylist.copy()
print(newlist)
newlist.reverse()
print(newlist)
newlist.extend([False, "day",34])
print(newlist)
names = ['uswat', 'aishat', 'cynthia', 'raphael', 'gift']
print(names[0:3])
print(names[2:])
print(names[-2])

#looplist = ['busayo', 30, 3.98, 'F', True]
for i in "busayo":
    print(i)
    
#conditional statement in python
#conditional statement are used to evaluate a
#condition and execute a command if the condition
#is true or not
#Types ->
#if
#tenary
# if statement




