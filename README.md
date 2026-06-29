# Python DartBot (available at https://python-dartbot.onrender.com/)

A browser-based game of Cricket Darts where you can play against a computer-controlled opponent with three different difficulty levels. Click directly on the dartboard to record your throws, review or undo your selections, and submit your turn when you're satisfied. The bot will then take its turn before the game state updates in real time.

Currently this app is being hosted and deployed on Render using their free tier. As part of their free tier, the app will wind down after a period of inactivity. Due to this, there may be a Render loading screen when attempting to access the app, caused by Render reloading the application.

## Features
 - Interactive clickable dartboard
 - Three AI difficulty levels:
    - Easy
    - Medium
    - Hard
  - Undo individual dart throws before submitting
- Live cricket scoreboard
  - Animated bot turn narration
  - Automatic score tracking and win detection

## Tech Stack
Backend: Python, Flask
Frontend: HTML, CSS, JavaScript
Templating: Jinja2

## Screenshots
New Game

Choose your desired difficulty before starting a match.

<img width="1893" height="909" alt="f2a1ecd108ee25043779364a1fe4d87e" src="https://github.com/user-attachments/assets/e30d7924-fcd8-4963-a355-7a71e3c398b0" />






Game Start

The initial game board before either player has taken a turn.



<img width="1735" height="910" alt="1e74b3faa9ba2dc4677f85b999c00521" src="https://github.com/user-attachments/assets/8735f55a-b39b-4112-81f0-467ee4bbd5aa" />



Mid-Game

A match in progress showing the live scoreboard, current scores, and bot narration.

<img width="1864" height="910" alt="cd95ad7fe892737a6faff901b3e73199" src="https://github.com/user-attachments/assets/6e8d3488-488d-4fa1-8430-24a7b959ecce" />



## Running Locally

### Clone the repository:

git clone https://github.com/yourusername/python-dartbot.git

cd python-dartbot

### Create and activate a virtual environment:

python -m venv .venv

### Install the dependencies:

pip install -r requirements.txt

### Run the application:

python routes.py

### Then open your browser and navigate to:

http://127.0.0.1:16240 or http://localhost:16240

## Possible Future Improvements
- 501/301 implementation
- Additional AI strategies and more realistic accuracy simulation
- Player statistics and match history


