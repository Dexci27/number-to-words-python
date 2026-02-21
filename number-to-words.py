print('                      NUMBER TO WORDS')
while True :
	num = input('Enter a number : ')
	try :
		num = int(num)
	except :
		while type(num) != int :
			print('YOU WROTE THE NUMBER WITH STRING, PLEASE TRY AGAIN')
			num = input('Enter a number : ')
			try :
				num = int(num)
			except :
				pass
				

	num = str(num)
	#Name of the numbers in word
	letter_0 = 'zero'
	letter_1 = 'one'
	letter_2 = 'two'
	letter_3 = 'three'
	letter_4 = 'four'
	letter_5 = 'five'
	letter_6 = 'six'
	letter_7 = 'seven'
	letter_8 = 'eight'
	letter_9 = 'nine'
	letter_1_to_9 = [letter_1, letter_2, 		letter_3, letter_4, letter_5, letter_6, letter_7, letter_8, letter_9]
	letter_10 = 'ten'
	letter_11 = 'eleven'
	letter_12 = 'twelve'
	letter_13 = 'thirteen'
	letter_14 = 'fourteen'
	letter_15 = 'fifteen'
	letter_16 = 'sixteen'
	letter_17 = 'seventeen'
	letter_18 = 'eighteen'
	letter_19 = 'nineteen'
	letter_11_to_19 = [letter_11, letter_12, letter_13, letter_14, letter_15, letter_16, letter_17, letter_18, letter_19]
	letter_20 = 'twenty'
	letter_30 = 'thirty'
	letter_40 = 'fourty'
	letter_50 = 'fifty'
	letter_60 = 'sixty'
	letter_70 = 'seventy'
	letter_80 = 'eighty'
	letter_90 = 'ninety'
	letter_10_to_90 = [letter_10, letter_20, letter_30, letter_40, letter_50, letter_60, letter_70, letter_80, letter_90] 
	letter_100 = 'hundred'
	letter_1000 = 'thousand'
	letter_1_to_99 = [letter_10]
	a = 0
	for i in letter_1_to_9 :
		letter_1_to_99.insert(a, i)
		a += 1
	for i in letter_11_to_19 :
			letter_1_to_99.append(i)
	letter_1_to_99.append(letter_20)
	a = 0
	for i in range(9) :
			letter_1_to_99.append(f'{letter_20} {letter_1_to_9[a]}')
			a += 1
	letter_1_to_99.append(letter_30)
	a = 0
	for i in range(9) :
			letter_1_to_99.append(f'{letter_30} {letter_1_to_9[a]}')
			a += 1
	letter_1_to_99.append(letter_40)
	a = 0
	for i in range(9) :
			letter_1_to_99.append(f'{letter_40} {letter_1_to_9[a]}')
			a += 1
	letter_1_to_99.append(letter_50)
	a = 0
	for i in range(9) :
			letter_1_to_99.append(f'{letter_50} {letter_1_to_9[a]}')
			a += 1
	letter_1_to_99.append(letter_60)
	a = 0
	for i in range(9) :
			letter_1_to_99.append(f'{letter_60} {letter_1_to_9[a]}')
			a += 1
	letter_1_to_99.append(letter_70)
	a = 0
	for i in range(9) :
			letter_1_to_99.append(f'{letter_70} {letter_1_to_9[a]}')
			a += 1
	letter_1_to_99.append(letter_80)
	a = 0
	for i in range(9) :
			letter_1_to_99.append(f'{letter_80} {letter_1_to_9[a]}')
			a += 1
	letter_1_to_99.append(letter_90)
	a = 0
	for i in range(9) :
			letter_1_to_99.append(f'{letter_90} {letter_1_to_9[a]}')
			a += 1
	letter_100_to_999 = [f'{letter_1} {letter_100}']
	a = 0
	for i in range(99) :
		letter_100_to_999.append(f'{letter_1} {letter_100} and {letter_1_to_99[a]}')
		a += 1
	letter_100_to_999.append(f'{letter_2} {letter_100}')
	a = 0
	for i in range(99) :
		letter_100_to_999.append(f'{letter_2} {letter_100} and {letter_1_to_99[a]}')
		a += 1
	letter_100_to_999.append(f'{letter_3} {letter_100}')
	a = 0
	for i in range(99) :
		letter_100_to_999.append(f'{letter_3} {letter_100} and {letter_1_to_99[a]}')
		a += 1
	letter_100_to_999.append(f'{letter_4} {letter_100}')
	a = 0
	for i in range(99) :
		letter_100_to_999.append(f'{letter_4} {letter_100} and {letter_1_to_99[a]}')
		a += 1
	letter_100_to_999.append(f'{letter_5} {letter_100}')
	a = 0
	for i in range(99) :
		letter_100_to_999.append(f'{letter_5} {letter_100} and {letter_1_to_99[a]}')
		a += 1
	letter_100_to_999.append(f'{letter_6} {letter_100}')
	a = 0
	for i in range(99) :
		letter_100_to_999.append(f'{letter_6} {letter_100} and {letter_1_to_99[a]}')
		a += 1
	letter_100_to_999.append(f'{letter_7} {letter_100}')
	a = 0
	for i in range(99) :
		letter_100_to_999.append(f'{letter_7} {letter_100} and {letter_1_to_99[a]}')
		a += 1
	letter_100_to_999.append(f'{letter_8} {letter_100}')
	a = 0
	for i in range(99) :
		letter_100_to_999.append(f'{letter_8} {letter_100} and {letter_1_to_99[a]}')
		a += 1
	letter_100_to_999.append(f'{letter_9} {letter_100}')
	a = 0
	for i in range(99) :
		letter_100_to_999.append(f'{letter_9} {letter_100} and {letter_1_to_99[a]}')
		a += 1
	letter_1_to_999 = []
	for i in letter_1_to_99 :
		letter_1_to_999.append(i)
	for i in letter_100_to_999 :
		letter_1_to_999.append(i)
	letter_1_to_999.insert(0, ' ')
	
	
	#Name of the numbers from 0 to 90
	if '0' in num and len(num) == 1 :
		print(letter_0)
	if '1' in num and len(num) == 1 :
		print(letter_1)
	if '2' in num and len(num) == 1 :
		print(letter_2)
	if '3' in num and len(num) == 1 :
		print(letter_3)
	if '4' in num and len(num) == 1 :
		print(letter_4)
	if '5' in num and len(num) == 1 :
		print(letter_5)
	if '6' in num and len(num) == 1 :
		print(letter_6)
	if '7' in num and len(num) == 1 :
		print(letter_7)
	if '8' in num and len(num) == 1 :
		print(letter_8)
	if '9' in num and len(num) == 1 :
		print(letter_9)
	if '10' in num and len(num) == 2 :
		print(letter_10)
	if '11' in num and len(num) == 2 :
		print(letter_11)
	if '12' in num and len(num) == 2 :
		print(letter_12)
	if '13' in num and len(num) == 2 :
		print(letter_13)
	if '14' in num and len(num) == 2 :
		print(letter_14)
	if '15' in num and len(num) == 2 :				print(letter_15)
	if '16' in num and len(num) == 2 :
		print(letter_16)
	if '17' in num and len(num) == 2 :
		print(letter_17)
	if '18' in num and len(num) == 2 :
		print(letter_18)
	if '19' in num and len(num) == 2 :
		print(letter_19)
	if '20' in num and len(num) == 2 :
		print(letter_20)
	if '30' in num and len(num) == 2 :
		print(letter_30)
	if '40' in num and len(num) == 2 :
		print(letter_40)
	if '50' in num and len(num) == 2 :
		print(letter_50)
	if '60' in num and len(num) == 2 :
		print(letter_60)
	if '70' in num and len(num) == 2 :
		print(letter_70)
	if '80' in num and len(num) == 2 :
		print(letter_80)
	if '90' in num and len(num) == 2 :
		print(letter_90)	


	#Name of the numbers from 21 to 99
	if len(num) == 2 :
		x = int(num[1]) - 1
		if num[0] == '2' and num[1] != '0' :
			print(f'{letter_20} {letter_1_to_9[x]}')
		if num[0] == '3' and num[1] != '0' :
			print(f'{letter_30} {letter_1_to_9[x]}')
		if num[0] == '4' and num[1] != '0' :
			print(f'{letter_40} {letter_1_to_9[x]}')
		if num[0] == '5' and num[1] != '0' :
			print(f'{letter_50} {letter_1_to_9[x]}')
		if num[0] == '6' and num[1] != '0' :
			print(f'{letter_60} {letter_1_to_9[x]}')
		if num[0] == '7' and num[1] != '0' :
			print(f'{letter_70} {letter_1_to_9[x]}')
		if num[0] == '8' and num[1] != '0' :
			print(f'{letter_80} {letter_1_to_9[x]}')
		if num[0] == '9' and num[1] != '0' :
			print(f'{letter_90} {letter_1_to_9[x]}')


	#Name of the numbers from 100 to 999
	if len(num) == 3 :
		y = 1
		z = 0
		a = int(num[1]) - 1
		b = int(num[2]) - 1
		for i in range(9) :
			if str(y) in num[0] and num[1] == '0' and num[2] == '0' :
				print(f'{letter_1_to_9[z]} {letter_100}')
			elif str(y) in num[0] and num[1] == '0' and num[2] != '0' :
				print(f'{letter_1_to_9[z]} {letter_100} and {letter_1_to_9[b]}')
			elif str(y) in num[0] and num[1] != '0' and num[2] == '0' :
				print(f'{letter_1_to_9[z]} {letter_100} and {letter_10_to_90[a]}')
			elif str(y) in num[0] and num[1] == '1' and num[2] != '0' :
				print(f'{letter_1_to_9[z]} and {letter_11_to_19[b]}')
			elif str(y) in num[0] and num[1] != '0' and num[2] != '0' :
				print(f'{letter_1_to_9[z]} {letter_100} and {letter_10_to_90[a]} {letter_1_to_9[b]}')
			y += 1
			z += 1


#Name of numbers from 1,000 to  999,999
	if len(num) > 3 and len(num) < 7 :
		if len(num) == 4 :
			a = int(num[0]) 
		elif len(num) == 5 : 
			a = int(num[0] + num[1]) 
		elif len(num) == 6 :
			a = int(num[0] + num[1] + num[2]) 
		x = 0
		num_thousand = []
		for i in range(a) :
			x += 1
		num_thousand = f'{letter_1_to_999[x]} thousand'
		b = int(num[-3] + num[-2] + num[-1])
		y = 0
		for i in range(b) :
			y += 1
		num_hundred = letter_1_to_999[y] 
		if num[-1] == '0' and num[-2] == '0' and num[-3] == '0' :
			print(num_thousand)
		elif num[-1] == '0' and num[-2] != '0' :
			y = 0
			print(f'{num_thousand} and {num_hundred}')
		elif num[-1] == '0' and num[-2] == '0' :
			y = 0
			print(f'{num_thousand} and {num_hundred}')
		elif num[-1] != '0' :
			y = 0
			for i in range(b) :
				y += 1
			num_hundred = letter_1_to_999[y]	
			print(f'{num_thousand} {num_hundred}')
	
	
	#Name of numbers from 1,000,000 to 999,999,999
	if len(num) > 6 and len(num) < 10 :
		if len(num) == 7 :
			a = int(num[0]) 
		elif len(num) == 8 : 
			a = int(num[0] + num[1])
		elif len(num) == 9 :
			a = int(num[0] + num[1] + num[2])
		x = 0
		num_million = []
		for i in range(a) :
			x += 1
		num_million = f'{letter_1_to_999[x]} million'
		b = int(num[-6] + num[-5] + num[-4])
		y = 0
		for i in range(b) :
			y += 1
		num_thousand = f'{letter_1_to_999[y]} thousand'
		c = int(num[-3] + num[-2] + num[-1])
		z = 0
		for i in range(c) :
			z += 1
		num_hundred = letter_1_to_999[z]
		if num[-1] == '0' and num[-2]== '0' and num[-3] == '0' and num[-4] == '0' and num[-5] == '0' and num[-6] == '0':
			print(num_million)
		elif num[-6] != '0' or num[-5] !='0' or num[-4] != '0' :
			print(f'{num_million} {num_thousand} {num_hundred}')
		elif num[-3] == '0' and num[-2] != '0' or num[-1] != '0' :
			print(f'{num_million} and {num_hundred}')
		elif num[-1] != '0' or num[-2] != '0' or num[-3] != '0' :
			print(f'{num_million} {num_hundred}')
	
	
	#Name of numbers from 1,000,000,000 to 999,999,999,999
	if len(num) > 9 and len(num) < 13 :
		if len(num) == 10 :
			a = int(num[0]) 
		elif len(num) == 11 : 
			a = int(num[0] + num[1])
		elif len(num) == 12 :
			a = int(num[0] + num[1] + num[2])
		x = 0
		for i in range(a) :
			x += 1
		num_billion = f'{letter_1_to_999[x]} billion'
		b = int(num[-9] + num[-8] + num[-7])
		y = 0
		for i in range(b) :
			y += 1
		num_million = f'{letter_1_to_999[y]} million'
		c = int(num[-6] + num[-5] + num[-4])
		z = 0
		for i in range(c) :
			z += 1
		num_thousand = f'{letter_1_to_999[z]} thousand'
		d = int(num[-3] + num[-2] + num[-1])
		a = 0
		for i in range(d) :
			a += 1
		num_hundred = letter_1_to_999[a]
		if num[-1] == '0' and num[-2] == '0' and num[-3] == '0' and num[-4] == '0' and num[-5] == '0' and num[-6] == '0' and num[-7] == '0' and num[-8] == '0' and num[-9] == '0' :
			print(num_billion)
		elif num[-9] == '0' and num[-8] == '0' and num[-7] == '0' and num[-6] == '0' and num[-5] == '0' and num[-4] == '0' and num[-3] == '0' :
			print(f'{num_billion} and {num_hundred}')
		elif num[-9] == '0' and num[-8] == '0' and num[-7] == '0' and num[-6] == '0' and num[-5] == '0' and num[-4] == '0' :
			print(f'{num_billion} {num_hundred}')
		elif num[-9] == '0' and num[-8] == '0' and num[-7] == '0' :
			print(f'{num_billion} {num_thousand} {num_hundred}')
		elif num[-1] == '0' and num[-2] == '0' and num[-3] == '0' and num[-4] == '0' and num[-5] == '0' and num[-6] == '0' :
			print(f'{num_billion} {num_million}')
		elif num[-1] == '0' and num[-2] == '0' and num[-3] == '0' :
			print(f'{num_billion} {num_million} {num_thousand}')
		else :
			print(f'{num_billion} {num_million} {num_thousand} {num_hundred}')
	
	
	if len(num) > 12 :
		print('We are sorry but numbers above 1 trillion are not yet available, ask the developer to add')