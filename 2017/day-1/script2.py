f = open('./input.txt','r')
s = f.read()
f.close()

to_sum = []

firstpart, secondpart = s[:len(s)//2], s[len(s)//2:]


for i,f in enumerate(firstpart):
  if f == secondpart[i]:
    to_sum.append(f)    

print(to_sum)

total = 0
for num in to_sum:
  total = total + (int(num)*2)

print(total)