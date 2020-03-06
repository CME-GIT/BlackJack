#!/usr/bin/env python3

import BlackJack_Main as main
import print_functions as pf


def Game():
	
	#_StartValues
	endgame=False
	Deck=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']*4
	dealer_hand=[]
	player_hand=[]
	print(f'You have {Credits["bank"]}$')


	#_place bet
	while True:
		bet_input=input('place bet:	')
		if not bet_input.isdigit():
				print('please enter a number')
				continue

		if int(bet_input)>int(Credits["bank"]):
				print(f'you cant spend more than {Credits["bank"]}$')
				continue

		
		Credits['bet']=int(bet_input)
		break

		


	#_Hand out first 2 cards
	dealer_hand=main.first_play(dealer_hand,Deck)
	player_hand=main.first_play(player_hand,Deck)
	player_points=main.count_cards(player_hand)

	print('\n Dealer Hand:')
	pf.DisplayDealerHidden(dealer_hand)

	print(' Your Hand:')
	print(pf.DisplayCards(player_hand))

    #BlackJack!
	if player_points==21:
		if player_points==main.count_cards(dealer_hand):
			print('\n Dealer Hand:')
			print(pf.DisplayCards(dealer_hand))	

			print(' Your Hand:')
			print(pf.DisplayCards(player_hand))
			print(f'The House drew a Blackjack as well, bet moves to next round')
			dealer_hand=main.first_play(dealer_hand,Deck)
			player_hand=main.first_play(player_hand,Deck)
			player_points=main.count_cards(player_hand)
			print('\n Dealer Hand:')
			pf.DisplayDealerHidden(dealer_hand)
			print(' Your Hand:')
			print(pf.DisplayCards(player_hand))

			
			endgame=True
		else:
			print(f'Blackjack! You won {Credits["bet"]} $. You own : : {Credits["bank"]}')
			endgame=True

	#_Game
	while endgame==False:
		
		#_Players Choice
		Choice=input('\n [1]Hit [2]stand [3] Fold or [4] Split?  \n\n ')	
		if Choice not in ('1','2','3','4'):
			print ('\n please enter a valid choice to continue')
			continue
		
	#_[1] Hit
		if Choice=='1':
			
			player_hand.append(Deck.pop())
			print(pf.DisplayCards(player_hand))
			player_points=main.count_cards(player_hand)
			if player_points>=21:
					main.result('',player_points,Credits)
					endgame=True

			while endgame==False:
				c_hit=input('[1]Hit or [2]Stand ? ')
				if c_hit not in ('1','2'):
					print ('\n please enter a valid choice to continue')
					continue
				if c_hit=='1':
					player_hand.append(Deck.pop())
					print(pf.DisplayCards(player_hand))
					player_points=main.count_cards(player_hand)
					print (player_points)
					if player_points>=21:
						main.result('',player_points,Credits)
						break
					continue
				
				if c_hit=='2':
					
					dealer_hand=main.dealer_play(dealer_hand,Deck)
					print(pf.DisplayCards(dealer_hand))
					print(pf.DisplayCards(player_hand))
					player_points=main.count_cards(player_hand)
					dealer_points=main.count_cards(dealer_hand)
					main.result(dealer_points,player_points,Credits)
					break
			break
	#_[2] Stand
		if Choice=='2':
			dealer_hand=main.dealer_play(dealer_hand,Deck)
			print(pf.DisplayCards(dealer_hand))
			print(pf.DisplayCards(player_hand))
			player_points=main.count_cards(player_hand)
			dealer_points=main.count_cards(dealer_hand)
		
			main.result(dealer_points,player_points,Credits)
			break
	#_[3]Fold
		if Choice=='3':
			print(f'Fold, you got {int(Credits["bet"])/2}$ back')
			print (Credits['bank'])
			Credits['bank']=int(Credits['bank'])+ (int(Credits["bet"])/2)
			print(f'You own : {Credits["bank"]}')
			break
	#_[4]Split
		if Choice=='4':
			#_check if split is possible
			if player_hand[0]!=player_hand[1]:
				print('you need a pair to split.')
				continue
			if int(Credits['bet'])*2>int(Credits['bank']):
				print('not enough funds to double the bet.')
				continue

			else:
			#Split Decks and Add one card
				DeckA=[]
				DeckB=[]
				Da_list=[]
				Db_list=[]
				printline=''
				Credits['bet']=int(Credits['bet'])*2
				print(f'bet doubled to {Credits["bet"]}')
				
				DeckA.append(player_hand[0])
				DeckB.append(player_hand[1])
				DeckA.append(Deck.pop())
				DeckB.append(Deck.pop())
				
				#build Print String for split
				Da_list=pf.DisplayCards(DeckA).split('\n')
				Db_list=pf.DisplayCards(DeckB).split('\n')
				for line in range(0,7):
					if line>0 and line<6:
						storageline=Da_list[line] + '| ' +  Db_list[line]
						printline+=storageline + '\n'
					else:
						storageline=Da_list[line] + '  ' +  Db_list[line]
						printline+=storageline + '\n'
				
				#dealer round
				dealer_hand=main.dealer_play(dealer_hand,Deck)
				dealer_points=main.count_cards(dealer_hand)
				
				#_print cards
				print('\n Dealer Hand:')
				print(pf.DisplayCards(dealer_hand))

				print('\n Your Hand:')
				print (printline)
				DeckAValue=main.count_cards(DeckA)
				DeckBValue=main.count_cards(DeckB)
				if DeckAValue>DeckBValue and DeckAValue<22:
					main.result(dealer_points,DeckAValue,Credits)
					break

				if DeckBValue>DeckAValue and DeckBValue<22:
					main.result(dealer_points,DeckBValue,Credits)
					break
				if DeckAValue==DeckBValue:
					main.result(dealer_points,DeckAValue,Credits)
					break



#_GAME
Credits={'bank':100, 'bet':0}
print('Welcome to the table!')


while True:
	Game()
	#question restart
	while True:
		Choice=input('\n [1]continue game [2]Leave table  \n\n ')	
		if Choice not in ('1','2'):
			print ('\n please enter a valid choice to continue')
			continue
		else:
			break
	if Choice=='1':
		if Credits['bank']<=0:
			print("You're broke!,Goodbye")
			break
		else:
			continue
	else:
		break		
	

		
