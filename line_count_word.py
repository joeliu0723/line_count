def read_files(filename):
	lines = []
	with open(filename,'r',encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	allen_count = 0
	viki_count = 0
	p_count = 0
	p_count2 = 0
	for line in lines:
		s =line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			for m in (s[2:]):
				if m == '圖片':
					p_count +=1
				else:
					allen_count += len(m)			
		elif name == 'Viki':
			for n in (s[2:]):
				if n =='貼圖':
					p_count2 += 1
				else:
					viki_count += len(n) 
	print('Allen貼了',p_count,'張貼圖')
	print('Allen說了',allen_count,'個字')
	print('Viki貼了',p_count2,'張貼圖')
	print('Viki說了',viki_count,'個字')
		

lines = read_files('-LINE-Viki.txt')
convert(lines)