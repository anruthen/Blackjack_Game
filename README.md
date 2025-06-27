# 🃏 Blackjack in Python

A simple text-based Blackjack game implemented in Python, playable in the terminal.

---

## 📌 Project Description

This is a console Blackjack game where you play against a virtual dealer. The goal is to reach 21 points without going over. The game follows standard Blackjack rules, including Ace value adjustment and dealer behavior.

---

## 🎮 Game Rules

|                         | Player                            | Dealer (Computer)                    |
|-------------------------|------------------------------------|--------------------------------------|
| Starting Cards          | 2 cards                            | 2 cards (1 face-down)                |
| Ace Handling            | 11 or 1 (automatically adjusted)   | 11 or 1 (automatically adjusted)     |
| Objective               | Get as close to 21 as possible     | Must draw until reaching at least 17 |
| Blackjack               | 21 with two cards = automatic win  | If both get 21 → draw                |
| Over 21 (Bust)          | Automatic loss                     | Player wins if dealer busts          |

---

## ✅ Features

- [x] Score calculation with Ace value flexibility
- [x] Dealer logic: hits until 17
- [x] Blackjack detection (two-card 21)
- [x] Real-time status display
- [x] Final result evaluation
- [x] Option to replay multiple rounds
- [x] Terminal clearing between rounds

---

## 🧠 Function Overview

```python
draw_card()        # Returns a random card
calculate()        # Calculates the current score, adjusts Ace if needed
check_blackjack()  # Checks for initial Blackjack
show_status()      # Displays current hand and score
show_final()       # Displays final hands and scores
end_result()       # Determines the game result
