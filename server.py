from bottle import Bottle, request, redirect
from html_templating import Templator
import game
import persistance
import user

games = persistance.return_all_games_with_sessions()


class ArchBottle(Bottle):
    def __init__(self):
        """ Initializes routing for server """
        super().__init__()
        self.route("/", method="GET", callback=self.homepage)
        # Route for handling form submission
        self.route("/options", method="POST", callback=self.handle_name_submission)
        self.route("/options", method="GET", callback=self.options_page)
        self.route("/create_game", method="POST", callback=self.create_game)
        self.route("/wait_for_player/<game_id>", method="GET", callback=self.wait_for_player)
        self.route("/join_game", method="POST", callback=self.join_game)
        self.route("/game", method="GET", callback=self.game)
        self.route("/game", method="POST", callback=self.make_move)
        self.route("/to_options", method="POST", callback=self.to_options)

    @classmethod
    def homepage(cls):
        """ Returns the home page
        Return:
            HTML page for username entry (str)
        """
        return Templator.main_page()

    @classmethod
    def handle_name_submission(cls):
        """Creates a User object associated with the username entered, redirects to create/join game page"""
        # Extract the name from the form
        user_name = request.forms.get('name')
        # Here you would typically create a user object and session ID
        new_user = user.User(user_name)  # Assuming this is where you also generate a session ID

        # Redirect to /options with the session_id as a query parameter
        # This assumes you want to show options or a confirmation page
        redirect(f'/options?session_id={new_user.session_id}')

    @classmethod
    def options_page(cls):
        """ Returns the create/join game page, populated with the user's name and stats
        Return:
            HTML page for creating/joining game (str)
        """
        session_id = request.query.get('session_id')

        # Here, you might look up session-specific data based on session_id
        # For demonstration, we're just passing the session_id to the template
        return Templator.game_options_page(session_id=session_id, user_o=user.sessions[session_id])

    @classmethod
    def create_game(cls):
        """ Creates a new game, redirects to either game page or options menu """
        # Handle game creation logic here
        new_game = game.Game()
        session_id = request.forms.get('session_id')

        games[new_game.gameId] = [new_game, user.sessions[session_id],
                                  None]  # 'games' would be a global or shared store

        persistance.store_game_with_session(games[new_game.gameId], key=new_game.gameId)
        # After creating the game, redirect to a game page, or back to options with a message
        redirect(f"/wait_for_player/{new_game.gameId}?session_id={session_id}")

    @classmethod
    def wait_for_player(cls, game_id):
        """ Waits until a player joins the match. Returns a waiting page if no one has joined, otherwise redirects to
        game page.

        Returns:
            HTML waiting page if other player is yet to join (str)
        """
        session_id = request.query.session_id
        game_info = games.get(game_id, None)

        if game_info:  # Check if game_info structure matches our expectation
            if game_info[1] is not None and game_info[2] is not None:
                # Both players have joined, redirect to the game page
                redirect(f"/game?session_id={session_id}&game_id={game_id}")
            else:
                # Waiting for the second player, refresh this page
                return f'''
                        <html>
                            <head>
                                <meta http-equiv="refresh" content="5"; url=/wait_for_player/{game_id}?session_id={session_id}" />
                            </head>
                            <body style="background-color: rgb(149, 77, 77); display: flex; justify-content: center; align-items: center;">
                                <div style="text-align: center; font-size: 24px; color: rgb(9, 8, 8);">
                                    <p>Waiting for the second player to join</p>
                                    <p style="font-size: 32px; font-weight: bold;">Game ID: {game_id}</p>
                                    <p>This page will automatically refresh every 5 seconds.</p>
                                </div>
                            </body>
                        </html>
                    '''
        else:
            # Game not found scenario
            return "Game not found."

    @classmethod
    def join_game(cls):
        """ Adds a player to a game. Returns a message to the player if no game was found, otherwise redirects them

        Returns:
            A response to the player if no game was found (str)
        """
        game_id = request.forms.get('game_id')
        session_id = request.forms.get('session_id')

        # Check if game exists
        if game_id in games.keys():
            game_instance, player1, player2 = games[game_id]

            # Assign session_id to player1 or player2 if slot is empty
            if player1 is None:
                games[game_id][1] = user.sessions[session_id]
                persistance.store_game_with_session(games[game_id], key=game_id)

                # First player joining, wait for second player
                redirect(f"/wait_for_player/{game_id}?session_id={session_id}&game_id={game_id}")

            elif player2 is None:
                games[game_id][2] = user.sessions[session_id]
                persistance.store_game_with_session(games[game_id], key=game_id)

                # Second player joined, proceed to game
                redirect(f"/wait_for_player/{game_id}?session_id={session_id}&game_id={game_id}")

            elif player1.username == user.sessions[session_id].username:
                games[game_id][1] = user.sessions[session_id]
                persistance.store_game_with_session(games[game_id], key=game_id)

                redirect(f"/game?session_id={session_id}&game_id={game_id}")

            elif player2.username == user.sessions[session_id].username:
                games[game_id][2] = user.sessions[session_id]
                persistance.store_game_with_session(games[game_id], key=game_id)

                redirect(f"/game?session_id={session_id}&game_id={game_id}")

            else:
                # Game is already full
                return "Game is full. Please join a different game or create a new one."
        else:
            # Game ID does not exist
            return "Game not found. Please check the Game ID and try again."

    @classmethod
    def game(cls):
        """ Returns the game page in response to a GET request

        Return:
            HTML page for the board if game is ongoing (str)
            HTML page for the match over screen if game is over (str)
        """
        # grab data from URL
        session_id = request.query.get('session_id')
        game_id = request.query.get('game_id')

        if user.sessions[session_id].username == games[game_id][1].username:
            you = user.sessions[games[game_id][1].session_id].username
            other_player = games[game_id][2].username
        else:
            you = user.sessions[games[game_id][2].session_id].username
            other_player = games[game_id][1].username

        g = games[game_id][0]

        # if game is ended, return match result page
        if g.is_ended():
            return cls.end_game(g.winner, games[game_id][1], games[game_id][2], session_id)
        # return the board page
        return Templator.board_page(g, session_id=session_id)

    @classmethod
    def make_move(cls):
        """ Processes the result of a POST request, applying the given move the game board if it is a legal move.

        Returns:
            The updated HTML page of the game board if the game is ongoing (str)
            The match result HTML page if the game is over (str)
        """
        session_id = request.query.get('session_id')
        game_id = request.query.get('game_id')

        g = games[game_id][0]

        if user.sessions[session_id].username == games[game_id][1].username:
            you = user.sessions[games[game_id][1].session_id].username
            other_player = games[game_id][2].username
            # No point attempting move if it is other player's turn
            if g.current_player == 2:
                return Templator.board_page(g, session_id=session_id)
        else:
            you = user.sessions[games[game_id][2].session_id].username
            other_player = games[game_id][1].username
            # No point attempting move if it is other player's turn
            if g.current_player == 1:
                return Templator.board_page(g, session_id=session_id)

        small_row = int(request.forms['smallRow'])
        small_col = int(request.forms['smallCol'])
        board_row = int(request.forms['bigRow'])
        board_col = int(request.forms['bigCol'])

        # Calls the make_move() method from game.py if the game is not ended
        if g.winner is None:
            try:
                g.make_move(small_row - 1, small_col - 1, board_row - 1, board_col - 1)
            # ValueError being raised means that the attempted move was invalid
            except ValueError:
                return Templator.board_page(g, session_id=session_id)

        # Returns game result is the game is a draw
        if g.winner == 0:
            games[game_id][1].add_draw()
            games[game_id][2].add_draw()
            return cls.end_game(0, games[game_id][1], games[game_id][2], session_id)

        # Returns game result if player 1 won
        elif g.winner == 1:
            games[game_id][1].add_win()
            games[game_id][2].add_loss()
            return cls.end_game(1, games[game_id][1], games[game_id][2], session_id)

        # Returns game result if player 2 won
        elif g.winner == 2:
            games[game_id][2].add_win()
            games[game_id][1].add_loss()
            return cls.end_game(2, games[game_id][1], games[game_id][2], session_id)

        # default case where game is ongoing, return the board page
        else:
            return Templator.board_page(g, session_id=session_id)

    @classmethod
    def end_game(cls, result: int, player1: user.User, player2: user.User, session_id: int):
        """ Returns the match result page

        Args:
            result: 0 for draw, 1 or 2 for win (int)
            player1: player 1 User object (User)
            player2: player 2 User object (User)
            session_id: session id to be embedded in page (int)

        Returns:
            HTML page for match result page (str)
        """
        return Templator.game_result_page(result, player1, player2, session_id)

    @classmethod
    def to_options(cls):
        """ Routes the page back to the options page, keeping the same session id"""

        session_id = request.query.get('session_id')
        redirect(f'/options?session_id={session_id}')


# driver code to run server
if __name__ == "__main__":
    host = "localhost"
    serverPort = 8080
    arch_server = ArchBottle()
    arch_server.run(host=host, port=serverPort, debug=True)
