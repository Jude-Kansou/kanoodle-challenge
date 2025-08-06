# puzzle/env.py  ── Kanoodle Gymnasium wrapper (v2.1)
"""Lightweight, masked Kanoodle environment compatible with Stable‑Baselines 3.

Key features
------------
1. **Binary grid observation** – converts `'.'` → 0, piece letters → 1.
2. **Invalid‑action mask** in `info["action_mask"]` (Gymnasium‑RFC style).
3. **Reward shaping** – `+α` per new square, big `solve_bonus` on completion,
   `invalid_penalty` for illegal/redundant moves.
"""
from __future__ import annotations

from typing import List, Tuple, Dict, Any
import numpy as np
import gymnasium as gym
from gymnasium import spaces

from .board import Board

Action = Tuple[str, int, int, int]  # (piece_name, orient_id, row, col)


class KanoodleEnv(gym.Env):
    metadata = {"render_modes": ["human"]}

    # ------------------------------------------------------------------
    def __init__(
        self,
        reward_alpha: float = 0.1,
        solve_bonus: float = 10.0,
        invalid_penalty: float = -1.0,
        render_mode: str | None = None,
    ) -> None:
        super().__init__()

        # Core engine
        self.board: Board = Board()
        self.empty_sym: str = self.board.EMPTY
        self.piece_names: List[str] = list(self.board.pieces.keys())

        # Reward knobs
        self._alpha = reward_alpha
        self._bonus = solve_bonus
        self._penalty = invalid_penalty

        # Pre‑compute catalogue of every in‑bounds placement.
        self.actions: List[Action] = self._enumerate_actions()

        # Gym spaces
        self.action_space = spaces.Discrete(len(self.actions))
        self.observation_space = spaces.Dict(
            {
                "grid": spaces.MultiBinary((self.board.rows, self.board.cols)),
                "available": spaces.MultiBinary(len(self.piece_names)),
            }
        )

        self.render_mode = render_mode

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _enumerate_actions(self) -> List[Action]:
        acts: List[Action] = []
        for name in self.piece_names:
            piece = self.board.pieces[name]
            for o_id, (h, w) in enumerate(piece.bounding_boxes):
                for r in range(self.board.rows - h + 1):
                    for c in range(self.board.cols - w + 1):
                        acts.append((name, o_id, r, c))
        return acts

    def _binary_grid(self) -> np.ndarray:
        """Convert char grid → 0/1 NumPy array."""
        return np.array(
            [[0 if cell == self.empty_sym else 1 for cell in row] for row in self.board.grid],
            dtype=np.int8,
        )

    def _obs(self) -> Dict[str, np.ndarray]:
        grid = self._binary_grid()
        available = np.array(
            [0 if n in self.board.placed else 1 for n in self.piece_names],
            dtype=np.int8,
        )
        return {"grid": grid, "available": available}

    def _action_mask(self) -> np.ndarray:
        """Return mask as **np.int8** (Gymnasium requirement)."""
        mask_bool = np.zeros(len(self.actions), dtype=bool)
        for idx, (n, o, r, c) in enumerate(self.actions):
            if n in self.board.placed:
                continue
            piece = self.board.pieces[n]
            if self.board.can_place(piece.orientations[o], r, c):
                mask_bool[idx] = True
        return mask_bool.astype(np.int8)

    def _is_solved(self) -> bool:
        return not any(cell == self.empty_sym for row in self.board.grid for cell in row)

    # ------------------------------------------------------------------
    # Gym API
    # ------------------------------------------------------------------
    def reset(
        self,
        *,
        seed: int | None = None,
        options: Dict[str, Any] | None = None,
    ):
        super().reset(seed=seed)
        self.board = Board()  # fresh grid
        obs = self._obs()
        info = {"action_mask": self._action_mask()}
        return obs, info

    def step(self, action: int):
        name, o_id, r, c = self.actions[action]

        before = sum(cell != self.empty_sym for row in self.board.grid for cell in row)
        reward = 0.0
        terminated = False
        truncated = False  # not used

        if name in self.board.placed:
            reward = self._penalty  # piece reused
        elif self.board.can_place(self.board.pieces[name].orientations[o_id], r, c):
            self.board.place(name, o_id, r, c)
            after = before + self.board.pieces[name].size  # faster than recount
            reward = (after - before) * self._alpha
            if self._is_solved():
                reward += self._bonus
                terminated = True
        else:
            reward = self._penalty  # illegal placement

        obs = self._obs()
        info = {"action_mask": self._action_mask()}
        return obs, reward, terminated, truncated, info

    # ------------------------------------------------------------------
    def render(self):
        if self.render_mode == "human":
            print(self.board)
        return self._binary_grid()

    def close(self):
        pass
