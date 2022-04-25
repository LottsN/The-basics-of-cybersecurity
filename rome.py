message = 'vbqwyivxgshofjeiycfbu'
letters = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(letters)):
   translated = ''
   for symbol in message:
         num = letters.find(symbol)
         num = num - i
         if num < 0:
            num = num + len(letters)
         translated = translated + letters[num]
   print(translated)
