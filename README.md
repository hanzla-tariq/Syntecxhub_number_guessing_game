# 🎯 Number Guessing Game

A fun **command-line Number Guessing Game** built with Python. The player selects a difficulty level, and the program generates a random number within a specified range. Keep guessing until you find the correct number while tracking your best score!

---

## ✨ Features

- 🎮 Three difficulty levels
- 🎲 Random number generation
- 📊 Tracks the number of attempts
- 🏆 Maintains the best score during the session
- ✅ Input validation
- 🔄 Play multiple rounds
- ⚠️ Handles invalid inputs gracefully

---

## 📋 Requirements

- 🐍 Python 3.x
- 📦 No external libraries required (uses Python's built-in `random` module)

---

## 🚀 How to Run

1. Make sure **Python 3** is installed on your system.
2. Download or clone this repository.
3. Open a terminal or command prompt.
4. Navigate to the project folder.
5. Run the program:

```bash
python number_guessing_game.py
```

> **Note:** If your system uses `python3` instead of `python`, run:

```bash
python3 number_guessing_game.py
```

---

## 🎮 Difficulty Levels

| Level | Number Range |
|-------|--------------|
| 🟢 Easy | 1 – 20 |
| 🟡 Normal | 1 – 100 |
| 🔴 Difficult | -100 – 100 |

---

## 💻 Example Gameplay

```text
---Number Guessing Game---

Select level
1. Easy
2. Normal
3. Difficult

Enter Choice: 2

Enter number to guess (1 to 100): 50
Too low. Try a higher number

Enter number to guess (1 to 100): 75
Too high. Try a lower number

Enter number to guess (1 to 100): 68
Congratulations! You guessed it.

You have won in 3 attempts.
Best Score: 3

Do you want to play again (y,n): n

Your Best Score: 3
Goodbye!
```

---

## 📁 Project Structure

```text
Number-Guessing-Game/
│
├── number_guessing_game.py
└── README.md
```

---

## ⚙️ Functions

| Function | Purpose |
|----------|---------|
| `validate_guess()` | 🎯 Validates user guesses, provides hints, and counts attempts |
| `main()` | 🎮 Controls game flow, difficulty selection, score tracking, and replay option |

---

## 🛡️ Error Handling

The game safely handles:

- ⚠️ Invalid menu selections
- 🔢 Non-numeric input
- 📏 Numbers entered outside the selected range

---

## 🏆 Best Score

The game records your **best score** (minimum number of attempts) during the current session and displays it after each round.

---

## 🚀 Future Improvements

- ⏱️ Timer-based challenge mode
- ❤️ Limited number of lives
- 💾 Save best score permanently
- 🎵 Sound effects
- 🖥️ Graphical User Interface (GUI)
- 🌐 Multiplayer mode
- 💡 Hint system

---

## 👨‍💻 Author

**Muhammad Hanzla**

---

⭐ If you found this project useful, consider giving it a **star** on GitHub!
