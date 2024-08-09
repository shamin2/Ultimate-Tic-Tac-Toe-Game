import persistance
import random

# Keeping track of usernames and their sessions
sessions = {}


class User:
    """
    This class represents a user and keeps track of their information.
    """

    def __init__(self, username):
        """
        Initializes a new User instance.

        Args:
            username (str): The username of the user.
        """
        self.username = username
        self.wins = 0
        self.losses = 0
        self.draws = 0
        
        self.check_registration()  # Check registration and update attributes if necessary
        self.session_id = self.create_session()  # Create a session upon registration


    def check_registration(self):
        """
        Checks if a user with the given username exists and loads their information if it does.

        Returns:
            list: A list containing [wins, losses, draws] for the user.

        Raises:
            ValueError: if a blank name is given
        """
        if self.username == "":
            raise ValueError
        temp = persistance.is_user_in_storage(self.username)
        if temp is True:
            user_info = persistance.load_stored_user_information(self.username)
            self.wins, self.losses, self.draws = user_info
            return user_info
        else:
            persistance.store_user_information(self)
            self.wins, self.losses, self.draws = [0, 0, 0]
            return [0, 0, 0]

    def create_session(self):
        """
        Generates a session ID for the given user and adds it to the sessions dictionary.

        Returns:
            session_id (str): The generated session ID.
        """
        while True:
            session_id = str(random.randint(1, 9999))
            if session_id not in sessions.keys():
                sessions[session_id] = self
                return session_id

    def add_loss(self):
        """
        Increments the losses attribute by 1 and stores new info in persistent storage.
        """
        self.losses += 1
        sessions[self.session_id] = self
        persistance.update_stored_user_information(self)

    def add_draw(self):
        """
        Increments the draws attribute by 1 and stores new info in persistent storage.
        """
        self.draws += 1
        sessions[self.session_id] = self
        persistance.update_stored_user_information(self)

    def add_win(self):
        """
        Increments the wins attribute by 1 and stores new info in persistent storage.
        """
        self.wins += 1
        sessions[self.session_id] = self
        persistance.update_stored_user_information(self)
