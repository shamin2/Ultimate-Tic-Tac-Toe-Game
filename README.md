# Ultimate Tic-Tac-Toe

A browser game for two players. Rules found [here.](https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe#Rules)

To run, start the server by running [server.py](server.py) and connect to localhost using your web
browser of choice to begin playing. To better understand how to use the interface, check out the [user manual and video guide](docs/user_manual.md). Current features include:

- Creating and joining matches using game IDs.
- Fully playable ultimate tic-tac-toe. 
- Persistent user win/loss/draw statistics.
- Highlighting of the active game board.

### Sprint 1 final pull request deadline for code: 5:00 PM, March 16th, 2024
### Sprint 2 final pull request deadline for code: 8:30 PM, April 5th, 2024

## Architecture Overview

![UML diagram of project](docs/Images/arch_UMLDiagram.png)

## Modules

The code for this project is split into modules, linked below.

| Module                      | Documentation                               | Location                               | Tests                                                    | 
|-----------------------------|---------------------------------------------|----------------------------------------|----------------------------------------------------------|
| Server API                  | [arch_serverAPI.md](docs/arch-files/arch_serverAPI.md) | [server.py](server.py) | [server_test.py](tests/server_tests.py) |
| HTML Templating            | [arch_html.md](docs/arch-files/arch_html.md)           | [arch_html.py](html_templating.py)           | [html_test.py](tests/html_test.py)                       | 
| Game Logic                  | [arch_applogic.md](docs/arch-files/arch_applogic.md)   | [game.py](game.py)                     | [game_test.py](tests/game_test.py)                       |
| Persistent Storage          | [arch_store.md](docs/arch-files/arch_store.md)         | [persistance.py](persistance.py)       | [store_test.py](tests/store_test.py)                     |
| User and Session Management | [arch_user.md](docs/arch-files/arch_user.md)           | [user.py](user.py)                     | [user_test.py](tests/user_test.py)                       | 


HTML templates for the web page can be be found [here.](https://github.com/CS2005W24/term-project-teamd/tree/master/templates)

## Process

An outline of our full software development process can be found [here.](docs/process_model.md)

A history of meeting notes can be found [here.](docs/meeting_notes.md)

A history of code reviews can be found [here.](docs/code_reviews.md)

Code attributions can be found [here.](docs/attributions.md)

Our projects Kanban board is [here.](https://github.com/CS2005W24/term-project-teamd/projects?query=is%3Aopen)

Performance reviews can be found [here.](docs/performance_reviews.md)

User stories can be found [here.](docs/user_stories.md)

Concept to refactor project into a general framework can be found [here.](docGameFrame)

