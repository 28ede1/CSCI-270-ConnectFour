"""
Web backend for ConnectFour Minimax AI.

Reuses the existing game logic (connectfour.py) and AI (players.py) unchanged.
The board is a 42-element 1D list, identical to the terminal version, so the
minimax AI ported over with zero changes to its behavior.

Run locally:
    uvicorn app:app --reload
Then open http://127.0.0.1:8000
"""
import os

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from connectfour import check_win_conditions, game_is_over, play_move
from players import initialize_my_player_fn

app = FastAPI(title="ConnectFour Minimax AI")

# Difficulty maps to minimax search depth (plies). Higher = stronger but slower.
AI_PLAYERS = {
    "easy": initialize_my_player_fn(num_plys=2),
    "medium": initialize_my_player_fn(num_plys=4),
    "hard": initialize_my_player_fn(num_plys=6),
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")


class MoveRequest(BaseModel):
    """Schema for the incoming JSON. Like Zod/Joi in Express: FastAPI rejects
    the request automatically if these constraints aren't met."""
    board: list[int] = Field(..., min_length=42, max_length=42)
    column: int = Field(..., ge=0, le=6)
    difficulty: str = "medium"


def result_for(board: list[int]) -> dict:
    """Build the game-state portion of a response for the given board."""
    winner = check_win_conditions(board)  # 0 = none yet, 1 = human, 2 = AI
    over = game_is_over(board)             # True if win or board full
    return {"board": board, "winner": winner, "game_over": over}


@app.post("/api/move")
def make_move(req: MoveRequest):
    """Apply the human's move (player 1), then respond with the AI's move (player 2)."""
    if req.difficulty not in AI_PLAYERS:
        raise HTTPException(status_code=400, detail="Invalid difficulty")

    board = list(req.board)

    # Validate the incoming board only contains 0/1/2.
    if any(cell not in (0, 1, 2) for cell in board):
        raise HTTPException(status_code=400, detail="Invalid board values")

    # Column must not be full.
    if board[req.column] != 0:
        raise HTTPException(status_code=400, detail="Column is full")

    # Human is player 1.
    play_move(board, 1, req.column)
    if game_is_over(board):
        return result_for(board)

    # AI is player 2 — this is your existing minimax, unchanged.
    ai_fn = AI_PLAYERS[req.difficulty]
    ai_col = ai_fn(board, 2)
    if ai_col is not None:
        play_move(board, 2, ai_col)

    return result_for(board)


# Serve the frontend (the HTML/JS board).
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def index():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))
