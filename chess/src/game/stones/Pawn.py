import numpy as np

from chess.src.game.stones.Stone import Stone
from chess.src.agents.Agent import Agent


class Pawn(Stone):

    def __init__(self, id: int,  player: Agent, coord: np.ndarray, status: str):
        super().__init__(id, player, coord ,status)

    def get_possible_moves(self, board: np.ndarray):
        possible_moves = []
        x, y = self.coord

        dir = 1 if self.start_row < 2 else -1
        if not self.moved and board[x + dir * 2 , y] == 0 and board[x + dir * 1, y] == 0:
            possible_moves += [{"old_coord": self.coord, "new_coord": self.coord  + dir * np.array([2, 0])}]
        if board[x + dir * 1, y] == 0:
            possible_moves += [{"old_coord": self.coord, "new_coord": self.coord + dir * np.array([2, 0])}]


