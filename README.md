# ConnectFour Minimax AI w/ Alpha-Beta Pruning

A Connect Four AI that uses the minimax algorithm for optimal decision-making. Alpha-beta pruning improves efficiency by reducing the number of game states explored. Playable in the terminal, with an optional web version.

**Deployed Link** <https://connectfour-ai-production.up.railway.app/>

## Features

- Minimax algorithm with alpha-beta pruning for optimal decision making
- Custom evaluation function (offensive + defensive heuristics)
- Frontend - Backend implementation (Python, FastAPI, JavaScript, HTML, CSS)

## Project Structure

All source files live in the `starter/` directory.

- **connectfour.py**: Core Connect Four mechanics — board representation, move execution, and win-condition checks (rows, columns, diagonals). Also provides helpers for determining valid moves and whether the game has ended.
- **players.py**: All player implementations — the minimax AI (with alpha-beta pruning), a random baseline player, and a human player that takes terminal input. Also contains the evaluation function and scoring helpers.
- **play.py**: Game execution — interactive play (human vs AI) and automated tournaments for benchmarking players over many rounds.
- **test.py**: Unit tests for core game logic and helpers (move placement, win detection, evaluation utilities).

## Running the terminal game

```bash
cd starter
python3 play.py
```

Choose different player types inside `play.py`:
- `initialize_my_player_fn()` — minimax AI
- `random_player_fn` — random baseline
- `human_player_fn` — terminal input

```python
# Play a single game (human vs AI)
play_game(human_player_fn, ai_player_fn)

# Run a tournament (AI vs random, 100 rounds)
play_tournament(ai_player_fn, random_player_fn, 100)
```

Run the tests:

```bash
cd starter
python3 test.py
```

## Web version

An optional browser-based version wraps the same game logic and AI in a small
[FastAPI](https://fastapi.tiangolo.com/) server with an HTML/JS board — a work
in progress for learning web deployment. The game engine and minimax AI are
unchanged; the web layer only adds a thin API and frontend on top.

```bash
cd starter
python3 -m pip install -r requirements.txt
python3 -m uvicorn app:app --reload
```

Then open <http://127.0.0.1:8000>. Difficulty (easy/medium/hard) maps to
minimax search depth.

### Deployment (Railway)

The web version deploys to [Railway](https://railway.app) using the included
`starter/Procfile`. Because the app lives in `starter/` rather than the repo
root, you **must** set the service's **Root Directory** to `starter` (Settings →
Source → Root Directory) — otherwise the builder scans the root, finds no Python
files, and fails to detect the app. The Procfile already binds to `$PORT`, so no
code changes are needed.

## Notable design choices

* Board is represented as a 1D list of size 42 (index = `row * 7 + col`)
* During search, each candidate move is applied to a copy of the board to avoid mutating shared state across branches
* Opponent threats are penalized slightly more than the AI's own threats are rewarded → a more defensive AI
