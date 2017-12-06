f = open('./input.txt','r')
s = f.readlines()
f.close()
to_sum = []

for line in s:
  linearray = line.split()
  linearray = list(map(int, linearray))
  linearray = sorted(linearray,reverse=True)
  i = 1
  lgth = len(linearray)
  for l in linearray:
    to_div = linearray[i:lgth]
    print(linearray)
    print(to_div)
    for d in to_div:
      if l % d == 0:
        to_sum.append(l // d)

    i = i + 1    


print(to_sum)    
total = 0
for num in to_sum:
  total = total + num

print(total)    