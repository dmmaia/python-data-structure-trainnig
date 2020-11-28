array = ['one', 'two', 'three', 'four']

i = len(array)-1
indice = 0
for a in array:
  temp = array[i]
  array[i] = a
  array[indice] = temp
  i -= 1
  indice += 1
  if i <= indice:
    break


print(array)


  