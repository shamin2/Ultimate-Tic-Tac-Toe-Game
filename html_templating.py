from game import Game
from user import User
from bottle import template


class Templator:
    """ A class with static methods for templating HTML pages"""

    @classmethod
    def main_page(cls):
        """Creates the main homepage.

        Returns:
            A complete HTML page for the homepage.
        """

        # returns the template with the welcome message
        home_page_template = template("templates/HomePage.html")
        return home_page_template

    @classmethod
    def board_page(cls, game: Game, session_id: int):
        """ Creates the board page

        Args:
            game: the game object to be used (Game)
            session_id: session_id to be embedded in page (int)

         Returns:
             A complete HTMl page of the game board with the data from the given game object (str)
        """

        # get data from given game
        raw_game_data = game.get_game_state()
        game_data = []
        # maps the data from the board into Xs and Os
        for i in raw_game_data:
            for j in i:
                for k in j:
                    if k == 1:
                        game_data.append("X")
                    elif k == 2:
                        game_data.append("O")
                    else:
                        game_data.append("")

        # finds the active board in order to highlight it
        b_values = []
        for i in range(0, 3):
            for j in range(0, 3):
                if game.main_board[i][j] == game.active_board:
                    b_values.append("50")
                else:
                    b_values.append("144")

        # populates the template with game_data
        board_page_template = template("templates/MainGamePage.html", game=game_data, session_id=session_id,
                                       game_id=game.gameId, highlight=b_values)
        return board_page_template

    @classmethod
    def game_result_page(cls, winner: int, player1: User, player2: User, session_id: int):
        """Creates the game result page.
a
        Args:
            winner: 0 for draw, 1 or 2 for win (int)
            player1: player 1 User object (User)
            player2: player 2 User object (User)
            session_id: session id to be embedded in page (int)

        Returns:
            A complete HTML page of the game result.
        """

        if winner == 0:
            game_result = "The game is a draw!"
        elif winner == 1:
            game_result = "{username} wins!".format(username=player1.username)
        else:
            game_result = "{username} wins!".format(username=player2.username)

        # The template function replaces {{end_game}} with the game_result variable's value
        game_result_template = template("templates/GameResult.html", end_game=game_result, session_id=session_id)
        return game_result_template

    @classmethod
    def game_options_page(cls, session_id: int, user_o: User):
        """ Returns the join/create game menu with the user data filled in
        Args:
            session_id: session_id to be used (int)
            user_o: User object to be displayed (User)

        Return:
            Join/create game HTML page with data from given user (str)
        """
        return template("templates/game_options.html", session_id=str(session_id), username=user_o.username,
                        wins=user_o.wins, losses=user_o.losses, draws=user_o.draws)




