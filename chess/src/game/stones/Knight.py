import numpy as np

from chess.src.game.stones.Stone import Stone
from chess.src.agents.Agent import Agent
from chess.src.game.stones.Stone import _check_if_position_on_board


class Queen(Stone):

    def __init__(self, id: int,  player: Agent, coord: np.ndarray, status: str, value: int):
        super().__init__(id, player, coord ,status, value)

    def get_possible_moves(self, board: np.ndarray):
        possible_moves = []
        x, y = self.coord

        directions = 
        if not self.moved and board[x + direc * 2 , y] == 0 and board[x + direc * 1, y] == 0:
            possible_moves.append({"old_coord": self.coord, "new_coord": self.coord  + direc * np.array([2, 0])})

        if board[x + direc * 1, y] == 0:
            possible_moves.append({"old_coord": self.coord, "new_coord": self.coord + direc * np.array([2, 0])})

        xl, yl = self.coord + np.array([direc * 1, 1])
        xr, yr = self.coord + np.array([direc * 1, -1])
        if _check_if_position_on_board((xl, yl)):
            if np.sign(board[xl, yl]) != np.sign(board[x, y]) and board[xl, yr] != 0:
                possible_moves.append({"old_coord": self.coord, "new_coord": np.array([xl, yl])})
        if _check_if_position_on_board((xr, yr)):
            if np.sign(board[xr, yr]) != np.sign(board[x, y]) and board[xr, yr] != 0:
                possible_moves.append({"old_coord": self.coord, "new_coord": np.array([xr, yr])})

        return possible_moves