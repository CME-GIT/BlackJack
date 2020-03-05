
#__Print Functions__##



def DisplayCards(cards):

	Card='''
 ____ 
|x   |
|    |
|   x|
 ---- 
 '''
	l_Card=''
	card_list=[]
	Individual_lines=[]
	cards_print=''

	#_replace x with Card Values

	for r in range(0,len(cards)):
		if cards[r]==10:
			l_Card=(Card.replace('x ','10'))
			l_Card=(l_Card.replace(' x','10'))
		else:	
			l_Card=(Card.replace('x',str(cards[r])))
		l_Card=l_Card.split('\n')
		card_list.append(l_Card)


	#formatting cards side by side

	for r in range(0,7):
		for r2 in range(0,len(card_list)):
		
			Individual_lines = card_list[r2]
		
			cards_print+=Individual_lines[r] +' '
		cards_print=cards_print +'\n'

	#cards_print=cards_print[:-6]
	
	return cards_print






def DisplayDealerHidden(cards):

	Card='''
 ____ 
|x   |___
|    |   |
|   x|   |
 ----	 |
     ----
 '''
	l_Card=''
	
	#_replace x with Card Values
	if cards[0]==10:
		l_Card=(Card.replace('x ','10'))
		l_Card=(l_Card.replace(' x','10'))
	else:
		l_Card=(Card.replace('x',str(cards[0])))
	return print(l_Card)



def test():
	cardlist=['A','4','3']
	l_Card=''
	card_list=[]
	cards_print=''
	Individual_lines=''

	Card2='''
   ____ 
x|
 |
 |
-
 

'''
	Card='''

 ____ 
|   x|
|    |
|x   |
 ---- 
 ''' 

	for r in range(0,len(cardlist)):
		if r==0:
			l_Card=Card
			l_Card=l_Card.split('\n')
			card_list.append(l_Card)
		else:
			l_Card=Card2
			l_Card=l_Card.split('\n')
			card_list.append(l_Card)		

	for r in range(0,7):
			for r2 in range(0,len(card_list)):
				
				if r2<=1:
					Individual_lines = card_list[r2]
					
					cards_print+= Individual_lines[r]	
			
				else:

					Individual_lines = card_list[r2]
					
					cards_print+= Individual_lines[r] +' '


			cards_print= cards_print +'\n'


	

	return cards_print