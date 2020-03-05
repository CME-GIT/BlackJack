
import random


def first_play(Hands,Deck):
 
    #__shuffle and draw
	for r in range(0,2):
 		random.shuffle(Deck)
 		Hands.append(Deck.pop())
				
	return Hands

def count_cards(User_hand):

	card_points=0

	#_calculate Points
	for r in range(0,len(User_hand)):
		
		if User_hand[r] in ('J','Q','K') :
			card_points+=10

		if User_hand[r] not in ('A','J','Q','K'):
			card_points+=User_hand[r]
	
	#_add Aces	
	if 'A' in User_hand:
		A_amount=User_hand.count('A')
		print (A_amount)
		for r in range(0,A_amount):
				if card_points<=10:
					card_points+=11
				else:
					card_points+=1




	return(card_points)

def dealer_play(Dealer,Deck):
	CountCards=count_cards(Dealer)
	while CountCards<17:
		Dealer.append(Deck.pop())
		CountCards=count_cards(Dealer)
	else:
		return Dealer

def result(Dealer,User,Credits):
	if Dealer == '':
		Dealer=0

	bank=int(Credits['bank'])
	bet=int(Credits['bet'])

	while True:
		if User>21:
			
			Credits['bank']= bank - bet
			print (f'You went above 21.  MINUS {Credits["bet"]}$')
			break

		if Dealer > 21:
			Credits['bank']= bank + bet
			print(f'Game Won! The House went above 21.  PLUS {Credits["bet"]}$')
			break

		if Dealer>User:
			Credits['bank']= bank - bet
			print (f'Game lost. The House wins with {Dealer}. MINUS {Credits["bet"]}$')
			break

		if Dealer<User:
			Credits['bank']= bank + bet
			if User==21:
				print(f'You hit 21!  + {Credits["bet"]}$ ')

			else:
				print(f'You won with {User}.  + {Credits["bet"]}$')
			
			break

		if Dealer==User:
			print('tie. bets are paid back.')
			break
	print(f'Total Credit : {Credits["bank"]}')