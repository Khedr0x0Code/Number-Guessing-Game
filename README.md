<div align="center">

# 🎮 Number Guessing Game

A dark-themed desktop guessing game built with **Python** and **Tkinter** — guess the secret number between 1 and 100 before you run out of tries!

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>

---

## ✨ Features

- 🌙 **One Dark-style theme** — carefully chosen palette (`#282c34` background, `#abb2bf` text, `#61afef` accents)
- 🎯 Secret number between **1–100**, **7 guesses** per round
- 🟢🟡 Higher/lower feedback with color cues (green for win `#98c379`, red for loss `#e06c75`)
- 🖱️ **Button hover effects** via `Enter`/`Leave` event bindings (raised → sunken relief)
- 🔄 **Play Again** button appears only after a round ends — resets state instantly
- 🧵 Threading for non-blocking UI animations
- ✅ Input validation with user-friendly error feedback

## 🚀 Run It

```bash
# Tkinter ships with the Python standard library — no pip installs needed
python game.py
```

*Note: on Debian/Ubuntu you may need `sudo apt install python3-tk` first.*

## 🎮 How to Play

1. A secret number between **1 and 100** is generated.
2. Type your guess and hit **Guess**.
3. Feedback tells you if you're too high or too low.
4. You have **7 attempts** — beat the game before running out!
5. Hit **Play Again** to restart with a fresh number.

## 🏗️ Implementation Notes

- Single `NumberGuessingGame` class encapsulating all state and UI
- `random.randint(1, 100)` for the secret; per-round state fully reset on replay
- Event-driven hover styling through `widget.bind()` instead of static configs
- Clean separation of game logic (`guess()`, `reset_game()`) and presentation

## 📁 Structure

```
game.py   # The entire game — one file, standard library only
```

## 🤝 Contributing

Ideas: difficulty levels (range/attempts), score persistence, keyboard Enter-to-submit. PRs welcome!
