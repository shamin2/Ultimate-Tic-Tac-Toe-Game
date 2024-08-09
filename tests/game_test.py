from unittest import TestCase
from game import Game
import os


class TestGame(TestCase):
    """ A set of unit tests for the Game class

    Methods reset() and get_game_state() only have one test each as they are very simple and can't really 'fail' i.e.
    raise exceptions

    """
    def setUp(self):
        """ Initialize tests """
        self.game = Game()

    def tearDown(self):
        """ Clean up from tests """
        for ext in ['.db', '.bak', '.dat', ',dir']:
            if os.path.exists('games' + ext):
                os.remove('games' + ext)

    def test_make_move(self):
        """ Test for the make_move function """
        self.game.reset()
        state = self.game.get_game_state()
        player = self.game.current_player
        # tests that moves are applied
        self.game.make_move(1, 1, 1, 1)
        self.assertNotEqual(state, self.game.get_game_state())
        self.assertNotEqual(player, self.game.current_player)
        # tests that active board is moved correctly according to played moves
        self.assertEqual(self.game.main_board[1][1], self.game.active_board)

    def test_make_move_fail(self):
        """ Test for the make_move function error raises"""
        self.game.reset()
        # tests that invalid indexes raise error
        self.assertRaises(IndexError, self.game.make_move, 3, 3)
        # test that player must be 0-2
        self.assertRaises(ValueError, self.game.make_move, 0, 0, player=3)
        self.assertRaises(ValueError, self.game.make_move, 0, 0, player=-1)
        self.game.make_move(0, 0, 0, 0)
        # tests that double moves are invalid
        self.assertRaises(ValueError, self.game.make_move, 0, 0, 0, 0)
        # tests that active board rule are enforced
        self.assertRaises(ValueError, self.game.make_move, 0, 0, 1, 1)

    def test_reset(self):
        """ Test for the reset function """
        self.game.reset()
        state = self.game.get_game_state()
        self.game.make_move(1, 1, 1, 1)
        self.game.reset()
        self.assertEqual(state, self.game.get_game_state())

    def test_get_game_state(self):
        """ Tests for the get_game_state function """
        self.game.reset()
        contents = self.game.get_game_state()
        for i in contents:
            for j in i:
                for k in j:
                    self.assertEqual(0, k)

    def test_is_ended_false(self):
        """ Tests for the is_ended() function returning False """
        self.game.reset()
        self.game.winner = None
        self.assertEqual(False, self.game.is_ended())

    def test_is_ended_true(self):
        """ Tests for the is_ended() function returning True """
        self.game.reset()
        self.game.winner = 1
        self.assertTrue(self.game.is_ended)
        self.game.winner = 2
        self.assertTrue(self.game.is_ended)
        self.game.winner = 0
        self.assertTrue(self.game.is_ended)
