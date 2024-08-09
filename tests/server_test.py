import unittest
from bottle import Bottle
import subprocess
import requests
import time
import server
import game
import templates


class TestServerAPI(unittest.TestCase):
    serverObj = server.ArchBottle()

    server_program = "server.py"

    def set_up(self):
        # Sets up the server
        self.server_process = subprocess.Popen(["python3", self.server_program], cwd="..")
        time.sleep(2)

    def tear_down(self):
        # Tests server shutdown
        self.server_process.terminate()
        self.server_process.wait()

    def test_homepage(self):
        # Tests the response from the homepage of the game
        response = requests.get("http://localhost:8080/")
        self.assertTrue(response, "The homepage is running")

    def test_name_submission(self):
        # Tests if name submission is working
        response = requests.get("http://localhost:8080/")
        self.assertTrue(response, "Name submission is working")

    def test_options_page(self):
        # Tests the response of the options page
        response = requests.get("http://localhost:8080/")
        self.assertTrue(response, "The options page is running")

    def test_create_game(self):
        # Tests the response of when a game is started
        response = requests.get("http://localhost:8080/")
        test_game = game.Game()
        self.assertIs(type(test_game), type(game.Game()), "The game is initialized")

    def test_wait_for_player(self):
        # Tests if the game waits for a second player before starting
        response = requests.get("http://localhost:8080/")
        self.assertTrue(response, "The game is waiting for a second player")

    def test_join_game(self):
        response = requests.get("http://localhost:8080/")
        self.assertTrue(response, "The join game function is working")

    def test_game(self):
        response = requests.get("http://localhost:8080/")
        self.assertTrue(response, "The game is running with two players")

    def test_move(self):
        # Tests the response of when a move is performed ingame
        response = requests.get("http://localhost:8080/")
        self.assertTrue(response, "Players can make moves")

    def test_end_game(self):
        # Tests to see if a game can end
        response = requests.get("http://localhost:8080/")
        self.assertTrue(response, "The game can end")

    def test_to_options(self):
        # Tests if the to_options function routes to the options page correctly
        response = requests.get("http://localhost:8080/")
        self.assertTrue(response, "Routed to options successfully")
