import persistance
from random import randint


class _Board:
    """ Private class to represent sub-boards"""

    def __init__(self):
        self.winner = None
        self._data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def is_ended(self) -> bool:
        """ Returns whether the board has been completed (won/drawn)"""
        return self.winner is not None

    def _check_for_end(self):
        # private method to check win condition
        pos = []
        for i in self._data:
            for j in i:
                pos.append(j)
        # return 0 in case of draw
        if pos.count(0) == 0:
            self.winner = 0
            return True
        return any((pos[a] == pos[b] == pos[c] and pos[a] != 0  # see attributions.md
                    for a, b, c in
                    [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]))

    def make_move(self, row: int, col: int, player: int):
        """ Places an X or O at the specified location

        Return:
            True if that move wins the game, otherwise false
        """
        # raise exception if params are invalid
        if player != 1 and player != 2:
            raise IndexError("Invalid player")
        if row > 2 or col > 2:
            raise IndexError("Invalid row or column index")

        # makes the move
        self._data[row][col] = player

        # checks if the game is won
        won = self._check_for_end()
        if won:
            self.winner = player
        return won

    def __str__(self):
        return str(self._data)

    def __getitem__(self, item):
        return self._data[item]


class Game:
    """ Public class used to represent the state of the overall game

        # see arch_applogic.md

        Make moves with make_move, which will return True when the given move ends the game and false otherwise

        Check the winner using the .winner attribute: None if game is ongoing, 0 if drawn,
        1 if player1 wins, 2 if player2 wins
    """

    def __init__(self):
        """ Constructor for Game objects

        """
        self.current_player = 1
        self.active_board = None
        self.main_board = [[_Board(), _Board(), _Board()], [_Board(), _Board(), _Board()],
                           [_Board(), _Board(), _Board()]]
        self.winner = None
        self._generate_game_id()

    def _generate_game_id(self):
        """Private method to generate gameID"""
        self.gameId = str(randint(1, 1000))

        while persistance.is_gameId_in_storage(self.gameId):
            self.gameId = str(randint(1, 1000))

    def make_move(self, row: int, col: int, board_row: int = None, board_col: int = None, player: int = None) -> bool:
        """ Fills in a single space on a specified board.

        board_row and board_col must be set to None unless the player is free to select a board
        (such as at the start of a match)
         Args:
             row: row of sub-board to place move
             col: col of sub-board to place move
             board_row: row of sub-board in main board (if left as None, uses current board row)
             board_col: col of sub-board in main board (if left as None, uses current board col)
             player: who's move it is, player 1 or player 2 (if left as none, uses current player)

        Raises:
            IndexError if coordinates are out of bounds
            ValueError if given parameters are invalid in some way

        Returns:
            True if game is over
            False otherwise
        """
        # raise exception if params are invalid
        if player != 1 and player != 2 and player is not None:
            raise ValueError("Invalid player")
        if row > 2 or col > 2 or row < 0 or col < 0:
            raise IndexError("Invalid row or column index")
        if board_row > 2 or board_col > 2 or board_row < 0 or board_col < 0:
            raise IndexError("Invalid row or column index")
        if (board_row is None or board_col is None) and self.active_board is None:
            raise ValueError("No board set, one must be supplied")
        if board_row is not None and board_col is not None:
            if self.active_board is not None and self.main_board[board_row][board_col] != self.active_board:
                raise ValueError("Invalid move - that is not the active board!")
        if (board_row is None and board_col is not None) or (board_row is not None and board_col is None):
            raise ValueError("Invalid board")

        # changes the active board if one was given, otherwise the currently active board remains the same
        if board_row is not None and board_col is not None:
            self.active_board = self.main_board[board_row][board_col]
        if player is None:
            player = self.current_player

        # validates the move, makes move if possible, raises error if space occupied
        if self.active_board[row][col] != 0:
            raise ValueError("Invalid move! Space already occupied")
        elif self.active_board.is_ended():
            raise ValueError("Invalid move! Board already won!")
        else:
            self.active_board.make_move(row, col, player=player)

        # reassigns the active board; if the expected board is won, then sets active board to None
        self.active_board = self.main_board[row][col]
        if self.active_board.is_ended():
            self.active_board = None

        # checks for winner, updates current_player and winner (if necessary)
        ended = self._check_for_end()
        if ended and self.winner != 0:
            self.winner = player
        else:
            if player == 1:
                self.current_player = 2
            else:
                self.current_player = 1

        # returns the state of the game (ended/not)
        return ended

    def reset(self):
        """ Resets the board to empty """
        for row in self.main_board:
            for board in row:
                board._data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def get_game_state(self):
        """ Returns the current state of the game board

        Returns:
            the contents of each sub-board, in order (list of lists)
        """
        state = []
        for row in self.main_board:
            for sub_board in row:
                board_data = []
                for sub_row in sub_board:
                    new_row = []
                    for i in sub_row:
                        new_row.append(i)
                    board_data.append(new_row)
                state.append(board_data)

        return state

    def is_ended(self) -> bool:
        """ Returns whether the board has been won
        Returns:
            True if won or drawn, False otherwise """
        return self.winner is not None

    def _check_for_end(self) -> bool:
        # private method to check win condition
        pos = []
        for i in self.main_board:
            for j in i:
                pos.append(j.winner)
        # return 0 to indicate draw
        if pos.count(None) == 0:
            self.winner = None
            return True
        ended = any(pos[a] == pos[b] == pos[c] and pos[a] is not None  # see attributions.md
                    for a, b, c in
                    [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)])
        if ended:
            self.winner = self.current_player
            return True
        return False
