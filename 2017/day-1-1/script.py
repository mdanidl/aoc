f = open('./input.txt','r')
s = f.read()
f.close()

to_sum = []
if s[0] == s[len(s)-1]:
  to_sum.append(s[0])

for i,c in enumerate(s):
  if i == 0:
    prev = c
    continue

  if prev == c:
    to_sum.append(c)

  prev = c  


total = 0
for num in to_sum:
  total = total + int(num)

print(total)