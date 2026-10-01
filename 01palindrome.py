name = 'sas'
print(len(name))
rev = ''
for i in range(len(name) - 1, -1, -1):
  rev += name[i]

if (name == rev):
  print("Palindrome")
else:
  print("Not a palindrome")