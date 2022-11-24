word = input()

first = word[0]
last = word[len(word)-1]

double_e = word[1:len(word)-1] * 2

print(first + ''.join(double_e) + last)

# Alternative ways of splitting string into list of characters:
## 
## Unpacking
## [*word]
##
## List compressions
## list_of_letters = [char for char in word]
##
## Typecasting
## list(word)
## 
## Extend iterates over its input, expnads the list and adds each member.
## list_of_letters.extend(word)
##
## List slicing
## list_of_letters[:] = word
