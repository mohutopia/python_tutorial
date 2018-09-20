"""
Pig Latin Translator from Codeacademy course
"""
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = ''
  # word[1:len(new_word)] is to slice the string without the first letter
  new_word = word[1:len(new_word)] + first + pyg
  print(new_word)
else:
  print('empty')