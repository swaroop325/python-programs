str=input()
def most_repeated_letters(word_1):
  x = 0
  z = 0
  for letter in word_1:
    y = word_1.count(letter[0:])
    if y > z:
      z = y
    x += 1
    return z

print most_repeated_letters('str')