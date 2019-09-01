import abc
import numpy as np
import copy

from chess.src.agents.Agent import Agent


class Stone(abc.ABC):

    def __init__(self, id: int,  player: Agent, coord: np.ndarray, status: str):
        self.id = id
        self.player = player
        self.start_row = coord[0]
        self._coord = coord
        self.status = status
        self.removed = False
        self.directions = []
        self.board_size = 8
        self.moved = False

    @property
    def coord(self):
        return self._coord

    @coord.setter
    def coord(self, coord):
        self.moved = True
        self._coord = coord

    @abc.abstractmethod
    def get_possible_moves(self, board: np.ndarray):
        """
        implements the move rule set of checkers, since the possible moves are depended of the status of the chosen
        stone (whether its normal or a check)
        :param board:
        :return:
        """
        pass


def _check_if_position_on_board(coord: tuple, board_size: int):
    """
    checks whether coordinates are inside of board
    :param coord:
    :param board_size:
    :return:
    """
    in_row = coord[0] in range(board_size)
    in_col = coord[1] in range(board_size)
    return in_row and in_col
