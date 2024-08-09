# Code Reviews
Some of these were conducted before the creation of this file. See meeting notes.

## Sprint 1

### March 8th, 2024

- Code reviewed Fadi's code for persistence. 
  - Minor readability improvements. Changes variable 'u' to 'username'
  - Will wait and see if code is inline with selina's user Module to accept pull request
  - Did not merge into master


### March 14th, 2024

- Reviewed Dylan's Code for game logic
  - Removed some extraneous print statements
  - Noted that the code could possibly be improved by better adhering to the DRY principle, but this is a minor concern
  - Accepted pull request to master branch.


- Reviewed Fadi's code for persistence
  - Needs is_user_in_storage function that returns true or false
  - Did not merge into master


- Reviewed Selina's code for User
  - register user function was not inline with other modules.
  - A rework was done where we create the user object and just check if that username has history.
  - Did not merge into master

### March 16th, 2024

- Reviewed Joel's code for the server API.
  - The row and column blocks were switched. Fixed that.
  - Fixed an issue where the server would not return the page to client. 
  - Fixed an issue with incorrect usage of is_ended()/winner from the game logic API
  - Noted that there are still some significant issues with this module, but accepted the merge to master in order to meet sprint 1 deadline.


- Reviewed Fadi's code for persistent storage.
  - Fixed inconsistency between variable names. All are now snake case.
  - Removed some unused imports
  - Accepted pull request to master
  

- Reviewed Selina's code for User
  - Code seems inline with what we discussed.
  - Accepted pull request to master
  

- Reviewed Shamin's HTML
  - Works correctly, accepted pull request to master branch

 
## Sprint 2

### March 20th, 2024

- Reviewed Fadi's code for persistence in branch user-persistance-functions. Consists of fixing some bugs where methods would fail if no .json file had been created.
  - All unit tests are passing.
  - Code is clear and readable.
  - No functionality is broken for other modules.
  - Accepted pull request.

- Reviewed Dylan's code for serverAPI and HTML templates in branch html_fix. Consists of fixing issues with the buttons on the webpage and addressing a bug where the server
would not return a page to the client.
  - All unit tests are passing.
  - Changes to serverAPI.py do not hurt readability of code.
  - No functionality is broken in other modules.
  - Accepted pull request.

*Note: we implemented a new strategy for code reviews, so from here code reviews are formatted differently.*

### March 25th, 2024

- Author: Fadi
  
- Module: Persistence

- Changes: Implemented methods to allow storing and loading of games. 
  
**Code Style**
  
-  DRY: Code is modular, does not violate DRY principle. 
  
-  SOLID/de-coupling: The module loosely coupled with the User and Game classes. It is singly responsible for persistence, and is easily extensible following SOLID principles.  
  
-  Formatting: Code follows the established conventions of our project. 
  
-  Documentation/docstrings: All methods have sufficient docstrings. 

**Functionality**
  
-  Are unit tests passing for this module?: Yes
  
-  Are unit tests passing for other modules?: Yes
  
-  Is the new functionality working properly?: Yes
  
-  Is all previous functionality working properly?: Yes
  
  Pull request status: Approved (#52)

  ### March 27th, 2024

- Author: Dylan, Shamin
  
- Module: HTML Templating, Server

- Changes: Created HTML templating module to populate HTML pages with game data. Server now uses this module instead of directly interacting with HTML.
  
**Code Style**
  
-  DRY: Each method is responsible for one webpage. 
  
-  SOLID/de-coupling: The templating module has no dependencies on other modules, so it is strongly de-coupled. It follows the single responsibility principle as the code is
  only responsible for populating HTML templates with data. The code follows SOLID principles. 
  
-  Formatting: Code follows the established conventions of our project. 
  
-  Documentation/docstrings: All methods have sufficient docstrings. 

**Functionality**
  
-  Are unit tests passing for this module?: Yes
  
-  Are unit tests passing for other modules?: Yes
  
-  Is the new functionality working properly?: Yes, the game is now displayed properly to the user. 
  
-  Is all previous functionality working properly?: Yes
  
  Pull request status: Approved (#55)

### April 1st, 2024

- Author: Selina
  
- Module: User 

- Changes: Added functionality for creating sessions and users. 
  
**Code Style**
  
-  DRY: No unnecessary repetition, each method is responsible for one thing. 
  
-  SOLID/de-coupling: This module strongly decoupled from the project. It's main dependency is persistence, from which it uses several public methods for saving user info. The code overall follows SOLID principles. 
  
-  Formatting: Code follows the established conventions of our project. 
  
-  Documentation/docstrings: All methods have sufficient docstrings. 

**Functionality**
  
-  Are unit tests passing for this module?: Yes
  
-  Are unit tests passing for other modules?: Yes
  
-  Is the new functionality working properly?: Yes.
  
-  Is all previous functionality working properly?: Yes
  
  Pull request status: Approved (#60)

  ### April 3rd, 2024

- Author: Fadi
  
- Module: Persistence, Server.

- Changes: Added persistence for games. Restructured server code to allow game resumption.  
  
**Code Style**
  
-  DRY: No unnecessary repetition, each method is responsible for one thing. 
  
-  SOLID/de-coupling: Persistence module remains strongly decoupled from the project. Server continues to follow SOLID principles. 

-  Formatting: Found a significant amount of obsolete commented-out code in serverAPI. Deleted this. 
  
-  Documentation/docstrings: All methods have sufficient docstrings. 

**Functionality**
  
-  Are unit tests passing for this module?: Yes
  
-  Are unit tests passing for other modules?: Some are failing for Server but they will be fixed. 
  
-  Is the new functionality working properly?: Yes
  
-  Is all previous functionality working properly?: Mostly, it will be fixed by tomorrow.
  
  Pull request status: Approved (#64)

### April 4th, 2024

- Author: Fadi, Dylan, Joel
  
- Module: Server, Templating, Game

- Changes: Finished restructuring of server. Updated HTML and templating to accomodate new features. Updated Game to enforce all rules of the game. Game is now fully playable!
  
**Code Style**
  
-  DRY: No unnecessary repetition.
  
-  SOLID/de-coupling: There is some strong coupling in Server, which handles some logic for determining whose turn it is. This should be changed to happen fully in Game, but
  will be left as-is for now. Coupling is otherwise weak and SOLID principles are followed. 

-  Formatting: Removed some extraneous print statements. Otherwise all is good. 
  
-  Documentation/docstrings: All methods have sufficient docstrings. 

**Functionality**
  
-  Are unit tests passing for this module?: Yes
  
-  Are unit tests passing for other modules?: Yes
  
-  Is the new functionality working properly?: Fixed an issue where player records would not updated after a match. Fixed an issue where player records were not being stored properly in persistence.
Noted that some issues likely remain surrounding persistence of user stats and usernames. 
  
-  Is all previous functionality working properly?: Yes
  
  Pull request status: Approved (#76)

  ### April 5th, 2024

- Author: Joel
  
- Module: Server

- Changes: Minor fixes for server and server unit tests
  
**Code Style**
  
-  DRY: No unnecessary repetition.
  
-  SOLID/de-coupling: Unchanged. Follows SOLID principles. 

-  Formatting: Up to the standards of our project. 
  
-  Documentation/docstrings: All methods have sufficient docstrings. 

**Functionality**
  
-  Are unit tests passing for this module?: Yes
  
-  Are unit tests passing for other modules?: Yes
  
-  Is the new functionality working properly?: Yes
  
-  Is all previous functionality working properly?: Yes
  
  Pull request status: Approved (#83)

  ### April 5th, 2024

- Author: Dylan, Shamin
  
- Module: HTML Templating

- Changes: Added highlighting of active board. Added new pages for login page and waiting page. 
  
**Code Style**
  
-  DRY: No unnecessary repetition.
  
-  SOLID/de-coupling: Templating is decoupled from the rest of the project. It is only dependent on the public APIs of Game and User to extract info. Follows SOLID principles. 

-  Formatting: Up to the standards of our project. 
  
-  Documentation/docstrings: All methods have sufficient docstrings. 

**Functionality**
  
-  Are unit tests passing for this module?: Yes
  
-  Are unit tests passing for other modules?: Yes
  
-  Is the new functionality working properly?: Yes
  
-  Is all previous functionality working properly?: Yes
  
  Pull request status: Approved (#88)

### April 5th, 2024

- Author: Selina
  
- Module: User

- Changes: Various tweaks and fixes. 
  
**Code Style**
  
-  DRY: No unnecessary repetition.
  
-  SOLID/de-coupling: Unchanged from before. Follows SOLID principles. 

-  Formatting: Up to the standards of our project. 
  
-  Documentation/docstrings: All methods have sufficient docstrings. 

**Functionality**
  
-  Are unit tests passing for this module?: Yes
  
-  Are unit tests passing for other modules?: Yes
  
-  Is the new functionality working properly?: Yes
  
-  Is all previous functionality working properly?: Yes
  
  Pull request status: Approved (#90, #95)

  ### April 5th, 2024

- Author: Fadi
  
- Module: Persistence

- Changes: Fixed bug relating to upper/lowercase usernames.
  
**Code Style**
  
-  DRY: Unchanged from before. 
  
-  SOLID/de-coupling: Unchanged from before. Follows SOLID principles. 

-  Formatting: Up to the standards of our project. 
  
-  Documentation/docstrings: All methods have sufficient docstrings. 

**Functionality**
  
-  Are unit tests passing for this module?: Yes
  
-  Are unit tests passing for other modules?: Yes
  
-  Is the new functionality working properly?: Yes
  
-  Is all previous functionality working properly?: Yes
  
  Pull request status: Approved (#92)

  



  

  

 

