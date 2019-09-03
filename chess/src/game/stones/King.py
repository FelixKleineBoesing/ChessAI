import numpy as np
import itertools

from chess.src.game.stones import diagonal_movements, horizontal_movements
from chess.src.game.stones.Stone import Stone
from chess.src.agents.Agent import Agent
from chess.src.game.stones.Stone import _check_if_position_on_board


class King(Stone):

    def __init__(self, id: int,  player: Agent, coord: np.ndarray, status: str, value: int):
        super().__init__(id, player, coord ,status, value)

    def get_possible_moves(self, board: np.ndarray):
        possible_moves = []
        x, y = self.coord

        directions = np.array(horizontal_movements + diagonal_movements)
        for direction in directions:
            x1, y1 = self.coord + direction
            if _check_if_position_on_board((x1, y1)):
                if np.sign(board[x1, y1]) != np.sign(board[x, y]) or board[x1, y1] == 0:
                    
        return possible_moves
