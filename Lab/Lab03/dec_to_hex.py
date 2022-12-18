dec = int(input('Input Decimal: ')) 
Hex = ''
while(dec>-1) :
	while(dec > 0): 
		n_Hex = str(dec%16)  
		if n_Hex not in range(0,10) :
			if n_Hex == '10' :	n_Hex = str('A')
			if n_Hex == '11' :	n_Hex = str('B')
			if n_Hex == '12' :	n_Hex = str('C')
			if n_Hex == '13' :	n_Hex = str('D')
			if n_Hex == '14' :	n_Hex = str('E')
			if n_Hex == '15' :	n_Hex = str('F')
			Hex =  n_Hex + Hex
			dec = dec // 16
		print('Hex:',Hex) 
		dec = int(input('Input Decimal: ')) 
		Hex = ''

if dec == -1 :
  print('Good bye.')
