s = []
with open('3.txt','r',encoding = 'utf-8-sig') as f:
	for line in f:
		s.append(line.strip())

for i in s:
	n = i.split(' ')
	name = n[0][5:]
	time = n[0][:5]
print(name)
print(time)