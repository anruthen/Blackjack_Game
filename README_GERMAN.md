# Tag 11 – Blackjack 🃏

Dieses Projekt ist ein Blackjack-Spiel für die Konsole, bei dem der Benutzer gegen den Computer (Dealer) spielt. Ziel ist es, möglichst nahe an 21 Punkte heranzukommen, ohne diese zu überschreiten. Das Spiel folgt den klassischen Blackjack-Regeln.

## Funktionen

- Vollständig interaktives Blackjack-Spiel im Terminal
- Der Dealer zieht automatisch Karten, bis er mindestens 17 Punkte erreicht
- Asse zählen je nach Spielsituation als 1 oder 11
- Erkennung von Blackjack
- Vergleich der Punktestände und Ausgabe des Ergebnisses
- Übersichtliche Benutzeroberfläche mit Punkteständen und finalen Händen
- Möglichkeit, das Spiel erneut zu starten

## Spielablauf

- Spieler und Computer erhalten jeweils zwei Karten aus einem virtuellen Deck.
- Der Spieler entscheidet, ob er weitere Karten ziehen möchte oder nicht.
- Der Computer zieht so lange Karten, bis er mindestens 17 Punkte erreicht hat.
- Wer 21 Punkte mit zwei Karten hat, erzielt einen Blackjack.
- Anschließend werden die Punktestände verglichen und das Ergebnis ausgegeben.

## Beispielausgabe
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

## Gelernt

- Strukturierung von Spiel-Logik
- Listenmanipulation und Kartenzieh-Logik
- Punkteberechnung mit dynamischer Ass-Wertung
- Funktionen mit Ein- und Ausgabeparametern
- Saubere Terminal-Ausgabe mittels `\n * 25` als "Clear-Screen"-Trick
- Umsetzung von Bedingungen und Schleifen zur Spiellogik
