f = open('./input.txt','r')
s = f.readlines()
f.close()
to_sum = []

for line in s:
  mini = 0
  maxi = 0
  linearray = line.split()
  print (linearray)
  for num in linearray:
    if (mini == 0) and (maxi == 0):
      mini,maxi = int(num), int(num)
    if int(num) < mini:
      mini = int(num)
    if int(num) > maxi:
      maxi = int(num)
  print('Min: '+str(mini)+' - Max: '+str(maxi)+' - Diff: '+str(maxi-mini))
  to_sum.append(maxi-mini)

print(to_sum)    

total = 0
for num in to_sum:
  total = total + (int(num))

print(total)    