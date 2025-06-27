# Day 11 - Blackjack 🃏

This project is a console Blackjack game that lets the user play against the computer (dealer). The goal is to reach 21 points without going over. The game follows standard Blackjack rules.

## Features

- Fully interactive terminal Blackjack game
- Dealer draws automatically until reaching at least 17
- Aces count as 1 or 11 depending on score
- Blackjack detection
- Score comparison and result announcement
- Clear user output with score updates and final hands
- Option to play again

## How It Works

- Each player gets two cards from a virtual deck.
- The user decides to draw more cards or hold.
- The dealer draws until reaching a score of 17 or higher.
- If either has 21 from two cards, it's a Blackjack.
- Final scores are compared and the result is printed.

## Example Output
```
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           

Your cards: [5, 2], current score: 7
Computer's first card: 10
Type 'y' to get another card, type 'n' to pass: y
Your cards: [5, 2, 10], current score: 17
Computer's first card: 10
Type 'y' to get another card, type 'n' to pass: n
Your final hand: [5, 2, 10], final score: 17
Computer's final hand: [10, 6, 10], final score: 26
PC went over. You win!
Do you want to play another game of Blackjack? Type 'y' or 'n':
```

## Skills Learned

- Game logic structuring
- List manipulation and card drawing logic
- Score calculation with dynamic Ace handling
- Functions with input/output
- Clean terminal output with `\n * 25` as a clear screen trick
- Implementing conditional logic and game loops
