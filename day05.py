secret = 8
guess_count = 0
guess_limit = 2
while(guess_count < guess_limit):
    guess_number = int(input("enter guess number: "))
    guess_count += 1
    if(secret == guess_number):
     print("you are right")
     break
    else:
     print("you are wrong")
     
                           
                       
                       
string = "tope is a nice girl"
lowercase = string.lower()
vowelcounts = {}
for vowel in "aeiou":
    count = lowercase.count(vowel)
    vowelcounts[vowel] = count
print(vowelcounts)

