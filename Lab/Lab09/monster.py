#monster
import numpy as np
X = np.random.RandomState(1) 
blood_start = int(input('Blood Start: '))


blood_human , blood_monster = blood_start , blood_start
turn = 1
human_died = False

while turn != 0 :

	if blood_human >0 and blood_monster > 0 :
		damage = 2*turn + 8
		action = input('Attack(a) or Heal(h): ')
		if(action == 'a') :
			blood_monster -= damage
			if (blood_monster <= 0) :	blood_monster =0
			turn += 1 
			print(f"Monster's HP left {blood_monster}")
		elif(action == 'h') :
			blood_human += 20 	
			turn = 1 
			print(f'Your HP left {blood_human}')
		blood_human -= 	X.randint(1, 40)
		if blood_monster == 0 : 
			print('You win.(^_^)')
			break
		elif blood_human <= 0 :	
			print("Monster's turn : Your HP left 0")
			print('You lose and die.(T_T)')
			break
		else :	print(f"Monster's turn : Your HP left {blood_human}")
