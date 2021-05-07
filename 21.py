import random

card_list = [2,3,4,5,6,7,8,9,10]

def my_queue():
	
	random.shuffle(card_list)
	print(f"Your card: {card_list[0]}")
	my_sum = card_list [0]
	while my_sum < 22:
		answer = input("Do you want to add card? yes/no ")
		if answer == 'yes':
			random.shuffle(card_list)
			my_sum += card_list[0]
			print(f"Your next card: {card_list[0]}\nYou reach: {my_sum}")
	
		elif answer == 'no':
			return my_sum
			print(f"Your nest card: {card_list[0]}\nYou reach: {my_sum}")

		else:
			print("Please print 'yes' or 'no'")

	return my_sum

def dealer_queue():

	random.shuffle(card_list)
	deal_sum = card_list[0]
	while deal_sum < 22:
		if deal_sum < 17:
			random.shuffle(card_list)
			deal_sum += card_list[0]
		else:
			answer = random.randint(1, 2)
			if answer == 1:
				random.shuffle(card_list)
				deal_sum += card_list[0]
				print(f"Dealer reach: {deal_sum}")
			
			else:
				print(f"Dealer reach: {deal_sum}")
				return deal_sum
		
	return deal_sum
			

answer_for_play = input("Do you want to play Blackjack? yes/no ")
while answer_for_play == 'yes':
	
	my_result = my_queue()
	deal_result = dealer_queue()

	if my_result > 21 and deal_result < 22:
		print("You fail......")

	elif deal_result > 21 and my_result < 22:
		print("Congratulations!!! You win!!!")

	elif my_result == deal_result and my_result < 22 and deal_result < 22:
		print("Draw!!!")

	elif my_result > deal_result and my_result < 22 and deal_result < 22:
		print("Congratulations!!! You win!!!")

	elif my_result < deal_result and my_result < 22 and deal_result < 22:
		print("You fail......")	

	else:
		print("You both fail...")

	answer_for_play = input("Do you want to play Blackjack? yes/no ")