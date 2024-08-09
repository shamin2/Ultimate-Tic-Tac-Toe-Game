import unittest

import persistance
from user import User, sessions
import os


class TestUser(unittest.TestCase):

    def setUp(self):
        # Clear sessions and any existing user data before each test
        sessions.clear()

    def tearDown(self):
        if os.path.exists('users.json'):
            os.remove('users.json')

    def test_init_success(self):
        # Test object initialization with a valid username
        user = User("hololo")
        print(user.wins)
        print(user.losses)
        print(user.draws)
        self.assertEqual(user.username, "hololo")
        self.assertEqual(user.wins, 0)
        self.assertEqual(user.losses, 0)
        self.assertEqual(user.draws, 0)
        self.assertIsNotNone(user.session_id)

    def test_init_failure(self):
        # Test object initialization with an invalid username
        with self.assertRaises(ValueError):
            User("")  # Empty username should raise ValueError

    def test_create_session(self):
        # Test successful session creation
        user = User("test_user")
        session_id = user.session_id
        self.assertIsInstance(session_id, str)
        self.assertIn(session_id, sessions.keys())

    def test_create_session_unique(self):
        # Create session for first user
        user1 = User("user1")
        session_id_1 = user1.create_session()

        # Create session for second user
        user2 = User("user2")
        session_id_2 = user2.create_session()

        # Ensure both session IDs are unique
        self.assertNotEqual(session_id_1, session_id_2)

    def test_update_user_info(self):
        # Register a new user
        new_user = User("sh")
        # Making sure they start with 0's
        new_user.wins = 0
        new_user.losses = 0
        new_user.draws = 0
        # Simulate some game results
        new_user.add_win()
        new_user.add_loss()
        new_user.add_draw()

        # Check if user information is correctly updated
        user_info = persistance.load_stored_user_information(new_user.username)
        self.assertEqual(user_info, [1, 1, 1])  # Expecting 1 win, 1 loss, 1 draw

    def test_update_user_info_sessions(self):
        # Register a new user
        new_user = User("woo")
        new_user.check_registration()
        # Making sure they start with 0's
        new_user.wins = 0
        new_user.losses = 0
        new_user.draws = 0

        # Simulate some game results
        new_user.add_win()
        new_user.add_loss()
        new_user.add_draw()

        # Check if user information is correctly updated in sessions
        updated_user = sessions[new_user.session_id]
        self.assertEqual(updated_user.wins, 1)
        self.assertEqual(updated_user.losses, 1)
        self.assertEqual(updated_user.draws, 1)

    def test_check_registration_existing_user(self):
        # Test registration check for an existing user
        user = User("selina")
        user.add_win()
        user.add_draw()

        existing_user = User("selina")
        self.assertEqual(existing_user.wins, 1)
        self.assertEqual(existing_user.losses, 0)
        self.assertEqual(existing_user.draws, 1)

    def test_check_registration_new_user(self):
        # Test registration check for a new user
        # Create a new user object
        user = User("new_user")
        # Call check_registration to create new user
        user.check_registration()

        # Verify that the user's information is initialized with zeros
        self.assertEqual(user.wins, 0)
        self.assertEqual(user.losses, 0)
        self.assertEqual(user.draws, 0)


if __name__ == '__main__':
    unittest.main()
