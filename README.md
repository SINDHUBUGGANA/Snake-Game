
# 🐍 Snake Game - Pygame Edition

A fun and interactive **Snake Game** built using **Pygame**! This game includes **difficulty levels, sound effects, a high score system, and a main menu**.

---

## 🎮 Features
✅ **Main Menu** - Start or Quit the game.
✅ **Difficulty Levels** - Choose between **Easy, Medium, and Hard**.
✅ **High Score System** - Saves and loads the highest score.
✅ **Background Music** - Continuous in-game music.
✅ **Sound Effects** - Different sounds for **eating food** and **game over**.
✅ **Modular Code** - Cleanly structured with multiple files for **easy modification**.

---

## 📂 Project Structure
```
snake_game/
│── main.py              # Starts the game
│── menu.py              # Handles the main menu & difficulty selection
│── game.py              # Contains game logic
│── settings.py          # Stores configurations (colors, speeds, etc.)
│── assets/              # Folder for assets like sounds & images
│   ├── background_music.mp3
│   ├── eat.wav          # 🎵 Eating sound
│   ├── game_over.wav    # 💀 Game over sound
│── highscore.txt        # Stores the highest score
```

---

## 🚀 How to Run
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/snake_game.git
cd snake_game
```

### 2️⃣ **Install Dependencies**
Ensure you have Python & Pygame installed:
```bash
pip install pygame
```

### 3️⃣ **Run the Game**
```bash
python main.py
```

---

## 🎵 How to Add Custom Sounds
1. **Download `.wav` files** from sites like:
   - [Freesound](https://freesound.org/)
   - [Pixabay Sounds](https://pixabay.com/sound-effects/)
   - [Mixkit Sound Effects](https://mixkit.co/free-sound-effects/)
2. Rename them to:
   - `eat.wav` (Eating Sound)
   - `game_over.wav` (Game Over Sound)
3. **Place them in the `assets/` folder**

---

## 🛠️ Customization
Want to modify the game? Here’s how:
- Change **snake speed** in `settings.py` (`SPEEDS` dictionary).
- Adjust **colors** in `settings.py`.
- Add more **sound effects** in `game.py`.
- Modify the **main menu text** in `menu.py`.

---

## 🤝 Contributing
Feel free to fork the repo and submit pull requests for improvements! 🚀

---

## 📜 License
This project is open-source under the **MIT License**.

Happy coding! 🎮🐍


