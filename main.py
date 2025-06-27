import art
import random
deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    return random.choice(deck_of_cards)

def calculate(cards):
    score = sum(cards)
    for i in range(len(cards)):
        if score > 21 and cards[i] == 11:
            cards[i] = 1
            score = sum(cards)
    return score

def show_status(cards_player, score_player, cards_pc):
    print(f"Your cards: {cards_player}, current score: {score_player}")
    print(f"Computer's first card: {cards_pc[0]}")
    return

def show_final(cards_player, score_player, cards_pc, score_pc):
    print(f"Your final hand: {cards_player}, final score: {score_player}")
    print(f"Computer's final hand: {cards_pc}, final score: {score_pc}")
    return

def check_blackjack(score_player, score_pc):
    if score_player == 21 and score_pc == 21:
        print("Both got Blackjack! It's a draw!")
        return True
    elif score_player == 21:
        print("Blackjack! You win! Congratulations!")
        return True
    elif score_pc == 21:
        (print("PC got Blackjack! You lose"))
        return True
    return False

def end_result(cards_player, score_player, cards_pc, score_pc):
    show_final(cards_player, score_player, cards_pc, score_pc)
    if score_player > 21:
        print("You went over. You lose!")
    elif score_pc > 21:
        print("PC went over. You win!")
    elif score_player == score_pc:
        print("It's a draw!")
    elif score_player > score_pc:
        print("You win! Congratulations!")
    elif score_player < score_pc:
        print("You lose. Better luck next time.")
    return


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y"

while play:
    print("\n" *25)
    print(art.logo)
    player_cards = []
    pc_cards = []
    for i in range(2):
        player_cards.append(draw_card())
        pc_cards.append(draw_card())
    player_score = calculate(player_cards)
    pc_score = calculate(pc_cards)
    if check_blackjack(player_score, pc_score):
        play = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower() == "y"
        continue
    show_status(player_cards, player_score, pc_cards)
    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y"
    while another_card and player_score < 21:
        player_cards.append(draw_card())
        player_score = calculate(player_cards)
        show_status(player_cards, player_score, pc_cards)
        if player_score < 21:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y"
    while pc_score < 17 and player_score < 22:
        pc_cards.append(draw_card())
        pc_score = calculate(pc_cards)

    end_result(player_cards, player_score, pc_cards, pc_score)

    play = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower() == "y"
