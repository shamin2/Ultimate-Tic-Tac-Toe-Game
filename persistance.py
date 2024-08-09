import json # Persistance for users will use JSON
import os.path
import shelve # Persistance for games will use shelve
import game


# User functions
def store_user_information(user_object, filepath="users.json"):
    """Stores user information into a JSON file.

    Args:
        user_object (User): The user object to store.
        filepath (str): The path to the JSON file where user data is persisted.
    """
    try:
        # Attempt to read the existing data from the file.
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                data = {"users": []}
                json.dump(data, f, indent=4)

        with open(filepath, 'r+') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                # If the file is empty and cannot be decoded, initialize `data`.
                data = {"users": []}

            # Convert the User instance to a dictionary manually.
            # This includes username, wins, losses, and draws attributes.
            user_data = {
                "username": user_object.username,
                "wins": user_object.wins,
                "losses": user_object.losses,
                "draws": user_object.draws
            }

            # Append the new user data.
            data['users'].append(user_data)

            # Move back to the start of the file to overwrite it.
            file.seek(0)
            file.truncate()

            # Write the updated data back into the file.
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error storing user information: {e}")
        raise


def update_stored_user_information(user_object, filepath='users.json'):
    """ This function updates information about a player

    Args:
        user_object: userObject to update information
        filepath: file for persistance

    Raises:
        raises error if failed to update properly
    """
    try:
        # Ensure the file is initially opened in read mode to load existing data
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                data = {"users": []}
                json.dump(data, f, indent=4)

        with open(filepath, 'r') as file:
            data = json.load(file)

        found = False
        # Update the relevant user's information if found
        print(data)
        for u in data['users']:
            if u['username'].lower() == user_object.username.lower():
                u['wins'] = user_object.wins
                u['losses'] = user_object.losses
                u['draws'] = user_object.draws
                found = True
                break
        print(found)
        if not found:
            raise ValueError(f"User {user_object.username} not found for update.")

        # Re-open the file in write mode to save the updates
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f"Error updating user information: {e}")
        raise


def load_stored_user_information(username, filepath='users.json'):
    """ Given a userObject returns their information, if they are in the User storage

    Args:
        username: name to look for object in storage
        filepath: file for persistance

    Raises:
        raises error if failed to load properly
    """
    try:
        with open(filepath) as file:
            data = json.load(file)
            # Use key access for dictionaries resulting from JSON parsing
            for user in data['users']:
                if user['username'].lower() == username.lower():
                    return [user['wins'], user['losses'], user['draws']]

            # Return default values if the user is not found
            return [0, 0, 0]
    except Exception as e:
        print(f"Error loading user information: {e}")
        raise ValueError


def is_user_in_storage(username, filepath='users.json'):
    """ returns if user is in storage

    Args:
         username: username of user
         filepath: file for persistance

    returns: Returns True if user is in storage
             Returns False if user is not in storage
    """
    try:
        if not os.path.exists(filepath):
            return False

        with (open('users.json') as file):
            data = json.load(file)
            for user in data['users']:
                if user['username'].lower() == username.lower():
                    return True

            return False    # return none if user is not found
    except Exception as e:
        print(f"Error loading user information: {e}")
        raise


def delete_user_information(user_object, filepath='users.json'):
    """ This function deletes the player from storage
    Args:
        user_object: to look for in storage and return info
        filepath: file for persistance

    Raises:
        raises error if failed to delete properly
    """
    try:
        user_deleted = False
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                data = {"users": []}
                json.dump(data, f, indent=4)

        with open(filepath, 'r+') as file:
            data = json.load(file)
            # Iterate over the users to find the match
            for i, user in enumerate(data['users']):
                if user['username'].lower() == user_object.username.lower():  # Access username attribute of userObject
                    del data['users'][i]  # Delete the user
                    user_deleted = True
                    break  # Exit loop after deleting the user

            if user_deleted:
                # Rewrite the file if a user was deleted
                file.seek(0)  # Move to the start of the file
                file.truncate()  # Truncate the file
                json.dump(data, file, indent=4)  # Write the updated data back to the file
                return True

        return False  # Return False if no user was deleted
    except Exception as e:
        print(f"Error deleting user information: {e}")
        raise


# Game persistance functions
def store_game_with_session(game_with_sessions, key, filepath='games'):
    """This function stores the game lists in persistance
    Args:
        game_with_sessions: game in a list with userobjects to store in persistance
        filepath: file for persistance

    Raises:
        raises error if failed to delete properly
    """

    try:
        with shelve.open(filepath) as db:
            db[key] = game_with_sessions

    except Exception as e:
        raise OSError("Failed to store the object") from e
    return


def return_all_games_with_sessions(filepath='games'):
    """This function returns all game lists from persistance
    Args:
        filepath: file for persistance
    Raises:
        raises error if failed to delete properly
    """

    games_dictionary = {}
    try:
        with shelve.open(filepath) as db:
            k_list = db.keys()

            for i in k_list:
                games_dictionary[i] = db[i]

        return games_dictionary

    except Exception as e:
        raise OSError("Failed to return items") from e


def is_gameId_in_storage(game_object_id, filepath='games'):
    """This function returns if a game_id is in storage

    Args: game_object_id: to look for the game in storage
          filepath: is the file path of storage

    Returns: False if game id is not in storage
            True if game id is in storage

    Raises: OSError if not passed in a string
    """

    try:
        with shelve.open(filepath) as db:

            klist = db.keys()
            if game_object_id not in klist:
                return False
            else:
                return True

    except Exception as e:
        raise OSError


def delete_game(game_object_id, filepath='games'):
    """ This function deletes a game from storage

    Args:
        game_object_id: deletes game with that id from storage
        filepath: is the file path of storage

    Raises:
        Raises an error if no game is found

    """
    try:

        with shelve.open(filepath) as db:
            klist = list(db.keys())

            if is_gameId_in_storage(game_object_id, filepath):
                del db[game_object_id]
            else:
                raise KeyError(f"No game found with ID {game_object_id}")

    except Exception as e:
        raise OSError

