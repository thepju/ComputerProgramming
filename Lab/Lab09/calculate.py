#--------Check Indent First-----------
# class MyMath:
# 	def __init__(self) :
# 		self.pi = MyMath.pi(self)
# 	def is_even(self,num) :
# 		return num%2 == 0 
# 	def fac(self,num) :
# 		if num < 2 :	return 1
# 		else :	return num*MyMath.fac(self,num-1)
# 	def is_prime(self,num) :
# 		if num < 2 :	return False
# 		for i in range(2,num):
# 			if num%i == 0 :
# 				return False
# 		return True
# 	def divide_by(self,num,k) :
# 		if num%k == 0 :	return True
# 		else : return False
# 	def ten_to_bi(self,num) :
# 		bi = ''
# 		while num > 0 :
# 			bi = str(num%2) + bi
# 			num = num//2
# 		return bi
# 	def ten_to_oct(self,num) :
# 		oc = ''
# 		while num > 0 :
# 			oc = str(num%8) + oc
# 			num = num//8
# 		return oc
# 	def ten_to_sixteen(self,num) :
# 		sixteen = ''
# 		#ten_to_fifteen = ['','A','B','C','D','E','F']
# 		while num > 0 :
# 			if 	 num%16 == 10 : sixteen = 'A' + sixteen 
# 			elif num%16 == 11 :	sixteen = 'B' + sixteen
# 			elif num%16 == 12 :	sixteen = 'C' + sixteen
# 			elif num%16 == 13 :	sixteen = 'D' + sixteen
# 			elif num%16 == 14 :	sixteen = 'E' + sixteen
# 			elif num%16 == 15 :	sixteen = 'F' + sixteen
# 			else :	sixteen = str(num%16) + sixteen
# 			num = num//16
# 		return sixteen
# 	def int_to_roman(self,num) :
# 		roman = ['M','D','C','L','X','IX','V','IV','I']
# 		number = [1000,500,100,50,10,9,5,4,1]
# 		roman_num = ''
# 		i = 0
# 		while num > 0 :
# 			for j in range(num//number[i]):
# 				roman_num = roman_num + roman[i]
# 				num -= number[i]
# 			i += 1
# 		return roman_num
# 	def pi(self):
# 		res = 3
# 		l = 2
# 		for i in range(2,52):
# 			   r = l * (l+1) * (l+2)
# 			   res += 4 * (-1)**i / r
# 			   l += 2
# 		return res