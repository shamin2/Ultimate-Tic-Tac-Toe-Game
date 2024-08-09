from unittest import TestCase
import json
import os
import persistance
import user
import game
import shelve


class TestUserPersistance(TestCase):
    test_filepath = 'users.json'
    invalid_filepath = '/invalid/path/users.json'


    def setUp(self):
        # Setup test environment before each test
        self.user1 = user.User("john")
        self.user1.wins = 1
        self.user1.losses = 2
        self.user1.draws = 3
        self.user2 = user.User("jane")
        self.user2.wins = 4
        self.user2.losses = 5
        self.user2.draws = 6

        self.users = [
            {"username": self.user1.username, "wins": self.user1.wins, "losses": self.user1.losses, "draws": self.user1.draws},
            {"username": self.user2.username, "wins": self.user2.wins, "losses": self.user2.losses, "draws": self.user2.draws}
        ]
        with open(self.test_filepath, 'w') as file:
            json.dump({"users": self.users}, file)


    def tearDown(self):
        if os.path.exists(self.test_filepath):
            os.remove(self.test_filepath)


    def test_store_user_information_success(self):
        # Attempt to store a new user
        persistance.store_user_information(self.user1, filepath=self.test_filepath)

        # Verify the user was stored along with all attributes
        with open(self.test_filepath, 'r') as file:
            data = json.load(file)
            stored_user = next((u for u in data['users'] if u['username'] == self.user1.username), None)

            self.assertIsNotNone(stored_user)
            self.assertEqual(stored_user['username'], self.user1.username)
            self.assertEqual(stored_user['wins'], self.user1.wins)
            self.assertEqual(stored_user['losses'], self.user1.losses)
            self.assertEqual(stored_user['draws'], self.user1.draws)

    def test_store_user_information_fail(self):
        with self.assertRaises(Exception):
            persistance.store_user_information(self.user1, filepath=self.invalid_filepath)

    #
    def test_update_stored_user_information_success(self):
        # Create an updated user object; assume we're updating wins, losses, and draws
        updated_user = user.User("john")
        updated_user.wins = 2
        updated_user.losses = 3
        updated_user.draws = 4
        persistance.update_stored_user_information(updated_user, filepath=self.test_filepath)


        # Verify the user's information was updated in the file
        with open(self.test_filepath, 'r') as file:
            data = json.load(file)
            updated_info = next((u for u in data['users'] if u['username'] == updated_user.username), None)

            self.assertIsNotNone(updated_info)
            self.assertEqual(updated_info['wins'], updated_user.wins)
            self.assertEqual(updated_info['losses'], updated_user.losses)
            self.assertEqual(updated_info['draws'], updated_user.draws)


    def test_update_stored_user_information_fail(self):
        nonexistent_user = user.User("nonexistent_user")

        persistance.delete_user_information(nonexistent_user)
        with self.assertRaises(ValueError):
            persistance.update_stored_user_information(nonexistent_user)

    def test_load_stored_user_information_success(self):
        user_info = persistance.load_stored_user_information(self.user1.username, filepath=self.test_filepath)
        expected_info = [self.user1.wins, self.user1.losses, self.user1.draws]
        self.assertEqual(user_info, expected_info)
    #
    #
    def test_load_stored_user_information_fail(self):
        user_info = persistance.load_stored_user_information("nonexistent_user", filepath=self.test_filepath)
        expected_default = [0, 0, 0]  # Assuming function returns [0, 0, 0] if user not found
        self.assertEqual(user_info, expected_default)
    #

    def test_is_user_in_storage_success(self):
        result = persistance.is_user_in_storage(self.user1.username, filepath=self.test_filepath)
        self.assertTrue(result)
    #
    def test_is_user_in_storage_fail(self):
        result = persistance.is_user_in_storage("nonexistent_user", filepath=self.test_filepath)
        self.assertFalse(result)
    #
    def test_delete_user_information_success(self):
        result = persistance.delete_user_information(self.user1, filepath=self.test_filepath)
        self.assertTrue(result)

        # Verify the user was actually deleted from the file
        with open(self.test_filepath, 'r') as file:
            data = json.load(file)
            user_exists = any(user for user in data['users'] if user['username'] == self.user1.username)
            self.assertFalse(user_exists)
    #
    def test_delete_user_information_fail(self):
        # Create a user instance that does not exist in the file
        nonexistent_user = user.User("nonexistent_user")

        # Test attempting to delete this non-existent user's information
        result = persistance.delete_user_information(nonexistent_user, filepath=self.test_filepath)
        result = persistance.delete_user_information(nonexistent_user, filepath=self.test_filepath)
        self.assertFalse(result)  # Expect False since the user does not exist


class TestGamePersistance(TestCase):


    def setUp(self):
        self.file_for_testing = "gameTest"
        self.game_object = game.Game()
        self.user1 = user.User("Max")
        self.user2 = user.User("John")

    def tearDown(self):
        for ext in ['.db', '.bak', '.dat', ',dir']:

            if os.path.exists(self.file_for_testing + ext):
                os.remove(self.file_for_testing + ext)

            if os.path.exists('games' + ext):
                os.remove('games' + ext)

            if os.path.exists('users.json'):
                os.remove('users.json')

    def test_store_game_with_session_success(self):
        game_sessions = [self.game_object, self.user1, self.user2]
        key = self.game_object.gameId

        # Attempt to store the game session
        persistance.store_game_with_session(game_sessions, key, filepath=self.file_for_testing)

        # Verify the game session is stored
        with shelve.open(self.file_for_testing) as db:
            self.assertIn(key, db)

    def test_store_game_with_session_fail(self):
        persistance.store_game_with_session("a", "2", filepath=self.file_for_testing)

        # Verify the game session is stored
        with shelve.open(self.file_for_testing) as db:
            self.assertNotIn("1", db)


    def test_return_all_games_with_sessions_success(self):
        expected_games = {
            self.game_object.gameId: [self.game_object, self.user1, self.user2],
        }

        with shelve.open(self.file_for_testing) as db:
            for key, value in expected_games.items():
                db[key] = value

        returned_games = persistance.return_all_games_with_sessions(filepath=self.file_for_testing)

        for key, value in expected_games.items():
            self.assertEqual(expected_games[key][0].gameId, returned_games[key][0].gameId)


    def test_return_all_games_with_sessions_fail(self):
        # Not sure how this test would work
        pass

    def test_is_gameId_in_storage_success_true(self):
        test_key = self.game_object.gameId
        test_value = [self.game_object, self.user1, self.user2]

        with shelve.open(self.file_for_testing) as db:
            db[test_key] = test_value

        result = persistance.is_gameId_in_storage(test_key, filepath=self.file_for_testing)
        self.assertTrue(result, f"Expected True for game ID '{test_key}' in storage.")

    def test_is_gameId_in_storage_success_false(self):
        test_key = "non_existing_game"

        with shelve.open(self.file_for_testing) as db:
            if test_key in db:
                del db[test_key]

        result = persistance.is_gameId_in_storage(test_key, filepath=self.file_for_testing)
        self.assertFalse(result, f"Expected False for game ID '{test_key}' not in storage.")

    def test_is_gameId_in_storage_fail(self):
        # Not sure how this test would work
        pass