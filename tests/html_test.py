from unittest import TestCase
from html_templating import Templator
from game import Game
from bottle import template
import user
import os


class TestGameBoard(TestCase):
    """ Tests for HTML templating module """
    def setUp(self):
        """ Initializes tests """
        # Gets the path to the templates directory
        root = os.path.dirname(__file__)
        self.templates_dir = os.path.join(os.path.dirname(root), 'templates')
        print(os.getcwd())

    def tearDown(self):
        """ Clean up from tests """
        for ext in ['.db', '.bak', '.dat', ',dir']:
            if os.path.exists('games' + ext):
                os.remove('games' + ext)

    def test_home_page(self):
        """ Tests the home/login page """
        correct_page = template(os.path.join(self.templates_dir, 'HomePage.html'))
        self.assertEqual(Templator.main_page(), correct_page)

    def test_board_page(self):
        """ Tests the main game board page """
        g = Game()
        mock_data = [""] * 81
        correct_page = template(os.path.join(self.templates_dir, 'MainGamePage.html'), game=mock_data, session_id=0,
                                    game_id=g.gameId, highlight = [144,144,144,144,144,144,144,144,144,144])
        os.chdir(os.path.dirname(self.templates_dir))
        self.assertEqual(Templator.board_page(g, 0), correct_page)

    def test_game_options_page(self):
        """ Tests the game options page """
        g = Game()
        u = user.User("test1")
        correct_page = template(os.path.join(self.templates_dir, 'game_options.html'), session_id=0, username="test1",
                                wins=0, losses=0, draws=0)
        self.assertEqual(Templator.game_options_page(0, u), correct_page)

    def test_game_results_page(self):
        """ Tests the game result page """
        u1 = user.User("test1")
        u2 = user.User("test2")
        correct_page = template(os.path.join(self.templates_dir, 'GameResult.html'), end_game="The game is a draw!", session_id=0)
        self.assertEqual(Templator.game_result_page(0, u1, u2, 0), correct_page)



