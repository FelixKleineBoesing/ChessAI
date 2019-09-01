import numpy as np

from chess.src.agents.Agent import Agent
from chess.src.game.GameHelpers import ActionSpace


class User(Agent):
    """
    This is only a placeholder for user input through rest interface
    """
    def decision(self, state_space: np.ndarray, action_space: ActionSpace):
        pass
