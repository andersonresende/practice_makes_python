
word = raw_input('Put one word: ')
letters_lst = []
for letter in word:
    if letter in 'aeiou':
        letters_lst.append('ub'+letter)
    else:
        letters_lst.append(letter)
print ''.join(letters_lst)

