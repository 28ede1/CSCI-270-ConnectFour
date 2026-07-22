// The board is a 42-element list, exactly like the Python terminal version.
// Index = row * 7 + col. 0 = empty, 1 = human, 2 = AI.
let board = Array(42).fill(0);
let locked = false;       // prevents clicks while the AI is thinking or game is over
let difficulty = "medium";
let scoreYou = 0, scoreCpu = 0;

const boardEl = document.getElementById("board");
const statusEl = document.getElementById("status");
const difficultyEl = document.getElementById("difficulty");
const scoreYouEl = document.getElementById("scoreYou");
const scoreCpuEl = document.getElementById("scoreCpu");

const pad = (n) => String(n).padStart(2, "0");

// Build the 42 cells once.
for (let i = 0; i < 42; i++) {
  const cell = document.createElement("div");
  cell.className = "cell";
  cell.dataset.col = i % 7;              // clicking any cell drops in that column
  cell.setAttribute("role", "button");
  cell.setAttribute("tabindex", "0");
  cell.setAttribute("aria-label", `Column ${(i % 7) + 1}`);
  const col = i % 7;
  cell.addEventListener("click", () => onColumnClick(col));
  cell.addEventListener("keydown", (e) => {
    if (e.key === "Enter" || e.key === " ") { e.preventDefault(); onColumnClick(col); }
  });
  cell.addEventListener("mouseenter", () => setColHover(col, true));
  cell.addEventListener("mouseleave", () => setColHover(col, false));
  boardEl.appendChild(cell);
}

// Highlight the whole column on hover (drop-preview affordance).
function setColHover(col, on) {
  const cells = boardEl.children;
  for (let i = col; i < 42; i += 7) {
    cells[i].classList.toggle("col-hover", on);
  }
}

// Render the board. `dropIdx` gets a one-shot drop animation.
function render(dropIdx = -1) {
  const cells = boardEl.children;
  for (let i = 0; i < 42; i++) {
    const wasP = cells[i].classList.contains("p1") || cells[i].classList.contains("p2");
    cells[i].className = "cell" + (board[i] === 1 ? " p1" : board[i] === 2 ? " p2" : "");
    if (i === dropIdx && !wasP) {
      void cells[i].offsetWidth;         // reflow so the animation restarts
      cells[i].classList.add("drop");
    }
  }
  boardEl.classList.toggle("locked", locked);
}

// Lowest empty row index in a column, or -1 if full (mirrors play_move).
function landingIndex(b, col) {
  for (let row = 5; row >= 0; row--) {
    const idx = row * 7 + col;
    if (b[idx] === 0) return idx;
  }
  return -1;
}

function setStatus(winner, gameOver) {
  statusEl.className = "";
  if (winner === 1) {
    statusEl.textContent = "YOU WIN!"; statusEl.classList.add("win"); locked = true;
    scoreYou++; scoreYouEl.textContent = pad(scoreYou);
  } else if (winner === 2) {
    statusEl.textContent = "GAME OVER"; statusEl.classList.add("lose"); locked = true;
    scoreCpu++; scoreCpuEl.textContent = pad(scoreCpu);
  } else if (gameOver) {
    statusEl.textContent = "DRAW"; statusEl.classList.add("draw"); locked = true;
  } else {
    statusEl.textContent = "INSERT DISC";
  }
}

function setThinking() {
  statusEl.className = "thinking";
  statusEl.textContent = "CPU THINKING...";
}

async function onColumnClick(col) {
  if (locked) return;
  if (board[col] !== 0) return;          // column full

  locked = true;
  // Show the human's disc immediately for snappy feedback.
  const humanIdx = landingIndex(board, col);
  board[humanIdx] = 1;
  render(humanIdx);
  setColHover(col, false);
  setThinking();

  try {
    // fetch → API → response cycle. Send the pre-move board so the backend
    // stays the single source of truth (it applies the human move itself).
    const sent = board.slice();
    sent[humanIdx] = 0;
    const res = await fetch("/api/move", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ board: sent, column: col, difficulty }),
    });
    if (!res.ok) throw new Error((await res.json()).detail || "Request failed");

    const data = await res.json();       // { board, winner, game_over }
    // Find where the AI dropped (the newly-filled p2 cell) to animate it.
    let aiIdx = -1;
    for (let i = 0; i < 42; i++) if (data.board[i] === 2 && board[i] !== 2) aiIdx = i;
    board = data.board;
    render(aiIdx);
    setStatus(data.winner, data.game_over);
    if (!data.game_over) locked = false;
  } catch (err) {
    statusEl.className = "error";
    statusEl.textContent = "ERROR: " + err.message;
    locked = false;
  }
}

difficultyEl.addEventListener("click", (e) => {
  const btn = e.target.closest("button[data-value]");
  if (!btn) return;
  if (btn.dataset.value === difficulty) return;   // no change, keep the board
  difficulty = btn.dataset.value;
  for (const b of difficultyEl.children) {
    b.setAttribute("aria-pressed", String(b === btn));
  }
  resetGame();   // changing mode starts a fresh game
});

document.getElementById("reset").addEventListener("click", resetGame);

// Clear the board back to a fresh game.
function resetGame() {
  board = Array(42).fill(0);
  locked = false;
  render();
  statusEl.className = "";
  statusEl.textContent = "INSERT DISC";
}

render();
