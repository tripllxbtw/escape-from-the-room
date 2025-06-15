# 🚪 Escape From The Room

## 🧩 Description

A simple text-based Python game where the player must find a way to escape from a locked room by interacting with objects and using logic.

---

## 🎯 Features

- 🗝️ Pick up a key
- 🔓 Unlock or crack the door
- 🏃 Leave the room in different ways
- 🧠 Text-based decision making
- 🔁 Infinite loop until correct actions are taken

---
## ▶️ How to Play

Run the game using Python:

---

🎮 Part 2 — Corridor Escape
In this part of the game, the player finds themselves in a corridor with multiple possible escape routes. The goal is to escape within 5 steps before getting caught by a monster.

🔑 Features:
- Multiple choices: break a window (but lose a step), escape via a door (requires finding 2 hidden keys), use a trapdoor, or find a secret door under the house.

- Hints: the player can read a note on the wall to find clues about where the keys are hidden.

- Step limit: the player has only 5 steps to escape; failing to do so results in being caught by the monster.

- Dynamic environment: each action can consume steps, and choices affect the outcome.

📌 Gameplay flow:
- The player chooses an option (1 to 5).

- Breaking the window hurts the player and uses up a step.

- Escaping through the door requires finding two keys (hidden in a drawer and under a rug).

- Using the trapdoor or the secret door under the house leads directly to escape.

- Reading the note gives hints but also uses up a step.

- The game ends in success if the player escapes in time or failure if the steps run out.

---

## ▶️ How to Play

Run the game using Python:

```bash
python running.py
python running-part2.py
