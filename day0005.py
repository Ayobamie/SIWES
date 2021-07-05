u_word = input('enter a sentence: ').lower()
count = 0
for letter in u_word:
    #if letter in 'aeiou':
        
        vowel_list = [letter for letter in u_word if letter in 'aeiou']
        print(f'the number of vowels in [{u_word}] is {count}')
        count += 1 
        
