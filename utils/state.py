class PuzzleState:
    def __init__(self, board, parent=None, move="", g=0):
        """
        Initialize a puzzle state
        :param board: 3x3 list representing the puzzle
        :param parent: Parent state
        :param move: Move taken to reach this state
        :param g: Cost from start to this state
        """
        self.board = board
        self.parent = parent
        self.move = move
        self.g = g
        self.h = 0
        self.f = 0  # f = g + h (for A*)
    
    def __eq__(self, other):
        return self.board == other.board
    
    def __lt__(self, other):
        return self.f < other.f
    
    def __hash__(self):
        return hash(str(self.board))
    
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])
    
    def get_blank_position(self):
        """Find the position of the blank tile (0)"""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j
        return None
    
    def get_copy(self):
        """Return a deep copy of the board"""
        return [row[:] for row in self.board]
    
    def is_goal(self, goal_board):
        """Check if this state is the goal state"""
        return self.board == goal_board
