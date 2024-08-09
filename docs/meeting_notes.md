# Meeting Notes Team D

## Feb 7th: assigned roles

| Module                   | Member | 
|--------------------------|--------|
| Request Routing/Response | Joel   |
| App logic                | Dylan  |
| Data Storage             | Fadi   |
| HTML Construction        | Shamin |
| User Info                | Selina |


## Feb 10th: Team Discussion
- Discussed all the markdown files that will be needed for assignment 1 and what will be included in them.
- Made sure all team members know about Umlet software, where the component diagrams will be made.
- Assigned Dylan as the person in charge of accepting pull requests if needed.
- Will be switching meeting note takers depending on availability.

## Feb 12th: Scrum Meeting
- **Scrum Master:** Dylan
- **Recorded By:** Fadi Baghdadi
- **Notes submitted on:** 12 Feb 2024
- **Venue:** Classroom
- **Source:** No recording
- **Time:** 2-2:50
- **Attendance:** Fadi, Selina, Joel, Dylan (Shamin was present at discord recap)
- **Agenda:** Ask professor about alot of different design desicions

Notes:
- We decided we are going to have a basic set up that involves loading old player specific games
- Discussed some of the fields that will be included in User info; player name, wins, losses, draws, last game played
- Discussed how Server module will import html construction
- Shared some code of Ultimate tic-tac-toe game implementation
- spoke with professor about some of the grading aspects expected of us for this assignment

## Feb 16, 2024
- **Scrum Master:** Selina
- **Recorded by:** Selina 
- **Notes submitted on:** Feb 17,2024  
- **Venue:** discord  
- **Source:** discord group chat 
- **Time:** 2-4pm  
- **Attendance:** Selina, Fadi, Dylan, Joel, Shamin
- **Agenda:** Task progress 

Notes:
- Discussed how user and persistance files should interact. 
- Decided not to implement password/login features yet. 
- Everyone will be using snake_case style for their code. Will merge all the uml diagrams tomorrow.

## Feb 28, 2024
- **Scrum Master:** Selina
- **Recorded by:** Selina 
- **Notes submitted on:** Feb 28,2024  
- **Venue:** class  
- **Source:** meeting in class 
- **Time:** 2-3pm  
- **Attendance:** Selina, Fadi, Dylan, Joel, Shamin
- **Agenda:** Task progress 

Notes:
- Examined the kanban board, didn't encounter any issues but made sure everyone knows how to use the issue tracker and the board.
- We will be using the html hidden field method for our session management. 
- Still have some questions to discuss with the professor on this class.
- Will assign individual tasks tomorrow

## Mar 1, 2024
- **Scrum Master:** Joel
- **Recorded by:** Shamin 
- **Notes submitted on:** Mar 1, 2024 
- **Venue:** Discord  
- **Source:** Voice call
- **Time:** 8-9pm  
- **Attendance:** Selina, Fadi, Dylan, Joel, Shamin
- **Agenda:** Assignment of tasks and filling out Kanban board with said tasks. A fair distribution of tasks among members
will be discussed, as it seems some development areas have a lot more tasks relating to them than other areas.

Assigned Tasks:
| Tasks                                        | Member      | 
|----------------------------------------------|--------     |
|Player registration                           | Selina      |
| Starting up a new game                       | Dylan/Joel  |
| Adding players to a game                     | Dylan/Joel  |
| Logging into a game                          | Selina/Joel |
| Making a move in a game                      |  Dylan/Joel       |
| Verifying a move in a game as valid          | Dylan       |
| Display of game during play                 | Shamin      |
| Management of a live game session            | Selina      |
| Checking other player's move                 | Shamin      |
| Determining the end of a game                | Joel/Dylan  |
| Recording a player's win/loss history | Fadi        |
| Displaying a player's win/loss history       | Shamin      | 

Notes:
- Assigned tasked to each team members
- Talked about the project progress
- Discussion about how the game will work by implementing all the tasks
- Shared personal opinions about the work
- We tried to assign each and every team members task by discussing in the meeting. Still there might be some changes further based on the availability and progress of everyone's task

## Mar 4th, 2024
- **Scrum Master:** Shamin
- **Recorded by:** Fadi
- **Notes submitted on:** Mar 4th,2024  
- **Venue:** class  
- **Source:** meeting in class 
- **Time:** 2-3pm  
- **Attendance:** Selina, Fadi, Dylan, Joel, Shamin
- **Agenda:** discuss different aspects of process model

Notes:
- Discussed the distinction between process and process model and what the contents of the related text file should include
- Discussed the need for a session ID, we decided we are going to have a simple sessions ID management that will help keep track of games
- Decided we are going to go over the entire process model with the professor next class
- Discussed the need to save games individually or save sessions, We decided not save sessions for this sprint
- Discussed the process of changing tasks around, We decided on requiring permission from the person who was originally assigned the task

## Mar 6th, 2024
- **Scrum Master:** Fadi
- **Recorded by:** Joel
- **Notes submitted on:** Mar 6th,2024  
- **Venue:** Discord  
- **Source:** Discord voice call
- **Time:** 8:10-8:50pm  
- **Attendance:** Selina, Fadi, Dylan, Joel, Shamin
- **Agenda:** Finalizing our process model. Encouraging use of issue tracker.

Notes:
- Discussed how we are going to write our process model. Decided that Fadi will finalize the document that will be
pushed to the master branch.
- Discussed how and when we will be using the issue tracker to address issues. Decided that we will be using it to document
every problem we have with our modules interacting, along with any other miscellaneous issues that may pop up.
- Decided that a new session will be created each time a player connects, instead of loading an "old" session. Existing
games can be loaded into these new sessions, as well as new games.
- Decided that when Fadi is done his current tasks, he will help Shamin with HTML templating. We decided it is a module that
will require additional help since we are having issues visualizing how it will interact with the server API and app logic.

## Mar 8th, 2024
- **Scrum Master:** Shamin
- **Recorded by:** Dylan
- **Notes submitted on:** Mar 8th,2024  
- **Venue:** Discord  
- **Source:** Discord voice call
- **Time:** 8:00-8:45pm  
- **Attendance:** Selina, Fadi, Dylan, Joel, Shamin
- **Agenda:** Code review for persistence module.

Notes: 
- Code review: Fadi gave a walkthrough of the persistence module to the team. We suggested minor improvements to the code that will be made before merging it into the master branch.
- Decided how User class will interact with persistence module for storing and loading user information.
- Opened a new issue relating to user.py.

## Mar 12th, 2024
- **Scrum Master:** Fadi
- **Recorded by:** Selina
- **Notes submitted on:** Mar 12th,2024  
- **Venue:** Discord  
- **Source:** Discord voice call
- **Time:** 5:00-7:00pm  
- **Attendance:** Selina, Fadi, Dylan, Joel, Shamin
- **Agenda:** Draft modules for each unit o code. Usual examination of kanban board and issue tracker.

Notes:
- Reviewed video 16 in class notes
- Discussed how to implement having two players playing from two different computers. Decided player2 will join the game using a session ID, created when player1 strats a game.
- We'll store sessions as dictionaries. 
- Had an idea of how to create the html using text boxes. Template will be reviewed when it is finished.
- Created a detailed process file (processDraft.md) of what we think each module should do.
- Progressing on some to do's (process model, register user).

## Mar 13th, 2024
- **Scrum Master:** Fadi
- **Recorded by:** Joel
- **Notes submitted on:** Mar 13th,2024  
- **Venue:** Discord  
- **Source:** Discord voice call
- **Time:** 8:45-9:15pm  
- **Attendance:** Selina, Fadi, Dylan, Joel, Shamin
- **Agenda:** Explain process of feeding information back and forth from user and HTML through serverAPI. Discuss changes to session management.

Notes:

- Decided that each user will have a session
- When a player logs in, a session is created for them
- When the first player logs in, then a template is returned with their name, an empty player 2 field, and an empty game
- Summarized: homepage -> input username -> pass to user.py -> information is saved and a user object is returned to serverAPI

## Mar 14th, 2024
- **Scrum Master:** Selina
- **Recorded by:** Fadi
- **Notes submitted on:** Mar 14th,2024  
- **Venue:** Discord  
- **Source:** Discord voice call
- **Time:** 8:30-9:15pm  
- **Attendance:** Selina, Fadi, Dylan, Joel, Shamin
- **Agenda:** Do some code reviews and discuss what's left to be done.

Notes:
- Did a code review for Dylans game logic files. Seems okay to accept the pull request.
- Code reviewed Selina's(User) and Fadi's(persistance) files. Found some inconsistancies between their functions. Discussed what needs to happen when a user is created. Found we need to create the user then check storage for peristance history associated with the user.They discussed how their code would communicate with another and will be making final changes tomorrow before our next meeting. where we will do another code review. 
- Dylan and joel discussed what how a player is supposed to make a move, to make sure they are still on the same page.
- Code reviewed Joel's server API code. Dylan game him some input on where to use gameLogics methods. We will be doing another code review tomorrow.

## Mar 16th, 2024
- **Scrum Master:** Dylan
- **Recorded by:** Selina
- **Notes submitted on:** Mar 16th,2024  
- **Venue:** Discord  
- **Source:** Discord voice call
- **Time:** 2:00-4:00pm  
- **Attendance:** Selina, Fadi, Dylan, Joel, Shamin
- **Agenda:** Final code reviews to accept PRs for sprint 1. Making sure everyone is done with
their documentation, and we're ready for submission.

Notes:
- Fixed minor issues and made sure everyone documents the major issues to be looked at in the next sprint.
- Created a code review file to better document the content of our reviews.
- The way server calls the templates doesn't seem to be working properly. Will be looked at later.
- A wrong function call was present in the server module from the game logic. Dylan identified and fixed it.
- Found a variable name in persistence.py that wasn't snake case, changed that for consistency.
- There were some unnecessary imports in persistence.py, we removed them.
- user and game modules look ready to be merged in master.
- merged all the PR's. The game is not fully functional as of now. It will be looked further into later and added to kanban board. 

## Mar 18th, 2024
- **Scrum Master:** Dylan
- **Recorded by:** Joel
- **Notes submitted on:** Mar 18th,2024  
- **Venue:** Class
- **Source:** Class meeting
- **Time:** 2:00-3:00pm  
- **Attendance:** Dylan, Joel
- **Agenda:** Discuss issues with the game not functioning properly, assess what is needed for Sprint 2.

Notes:
- The "tile-button" class in the MainGamePage.html file was set to hidden, this was fixed.
- Fixed the size of the buttons of the board.
- A templating module to add visual Xs and Os to the board is needed within html.py.
- Made an issue about other small problems in the HTML templates.
- Decided that getting the game working with the HTML templates is our first priority. After that we will focus on other features and tasks.
- Task assignment will have to be done on Wednesday, when all members are present.
- A couple of issues were raised within the project page about the aforementioned issues.

## Mar 20th, 2024
- **Scrum Master:** Joel
- **Recorded by:** Fadi
- **Notes submitted on:** Mar 20th,2024  
- **Venue:** Discord
- **Source:** Discord voice call
- **Time:** 8:30pm-9:30pm
- **Attendance:** Dylan, Joel, Fadi, Shamin, Selina
- **Agenda:** Discussed next tasks to be taken, and assignment 3 requirements. Usual review of tasks via KanBan Board and Issue Tracker

Notes:
- Code reviewed Dylans html_fix branch. summary of code review in Code-Reviews.md. Added to master.
- Discussed what user stories are. We decided we are going to be making up stories about how a feature came into implementation through a users comment. Will be asking professor about this next class.
- Code reviewed Fadi's persistance.py. He fixed some bugs where code would not work if users.json is not provided. Added to master. Summary of code review in Code-Reviews.md
- Decided all of us are going to participate in making the architectural document. each person is going to explain how they would refactor their code to fit the hypothetical.
- We will be asking professor more questions about how session management would work.
- Discussed that we need to implement a html templating file that displays state of game to user.
- Discussed server api not working properly when player plays in the same spot. Will be trying to figure out a work around. This is outlined in the issues.

## Mar 24th, 2024
- **Scrum Master:** Shamin
- **Recorded by:** Selina
- **Notes submitted on:** Mar 24th,2024  
- **Venue:** Discord
- **Source:** Discord voice call
- **Time:** 3pm-3.30pm
- **Attendance:** Selina, Dylan, Fadi, Shamin, Joel
- **Agenda:** Usual review of tasks via KanBan Board and Issue Tracker. Discuss fair distribution of tasks among group.
Consider if any process model elements need revision, addition or reduction for this sprint
Set deadlines for final code revisions, reviews and pull requests

Notes:
- Decided we'll have a game id implemented.
- Decided April 4th as the deadline for final code revisions and PRs.
- The task distribution seems fair among the members, added some to do's that we had in mind but were not on the kanban board.
- Reviewed the process model elements, no changes seem necessary for now, it will be looked into again after we have our feedback from sprint1.
- Discussed a layout to implement persistent storing and loading a game. Decided storing only one game and having a button that loads the latest saved game is the rough idea for now. Will discuss it with the professor as well.
- Opened an issue about X's and O's not displaying in the game. Dylan is currently working on it.


## Mar 25th, 2024
- **Scrum Master:** Joel
- **Recorded by:** Fadi
- **Notes submitted on:** Mar 25th,2024  
- **Venue:** Discord
- **Source:** Discord voice call
- **Time:** 9:30pm-10:30pm
- **Attendance:** Selina, Dylan, Fadi, Shamin, Joel
- **Agenda:** Go over Feedback and Code review game-persistance-functions as well as design discussions. Usual review of tasks via KanBan Board and Issue Tracker

Notes:
- Discussed with professor some inconsistencies in Feedback2. We did include a deadline for pull requests in the README.md It was said in the feedback that they couldn't fine it. It was also mentioned that we did not update our arch modules which is false. Some other inconsistencies were mentioned in the email sent by Selina. Professor said he will look over the email and reconsider.
- Changed the way code reviews work after we got the feedback from the professor. We now have a much more detailed template to use from now on called Code-Reviews-Template.md
- Code reviewed Fadi's game-persistance-functions. The code deals with how games are saved in persistance and also implemented a generate game id private funciton in game.py, which helps in getting a unique gameid for games. Pull request is accepted and a detailed code review added in Code-Reviews.md
- Found out that Fadi thought 'persistence' was spelled 'persistance'. An issue has been made and task is assigned.
- We discussed some layout options for how players are going to join each other games. We decided that we can have players create, join, or load games. We also decided that we are going to try different approaches on how this could work and discuss them in the next meeting.

- ## Mar 27th, 2024
- **Scrum Master:** Fadi
- **Recorded by:** Shamin
- **Notes submitted on:** Mar 27th,2024  
- **Venue:** Discord
- **Source:** Discord voice call
- **Time:** 9:15pm-10:15pm
- **Attendance:** Dylan, Fadi, Shamin, Joel, Selina
- **Agenda:** Go over templates and fair distribution of tasks among the team members. Usual review of tasks via KanBan Board and Issue Tracker

Notes:
- We went through Fadi's draft template that gives the session id for the game when the player enter theirs name. 
- Discussed some game features such as create game , join and branch related issue for. For the game ID, When a player enters their name it would generate a game id for the game and another player can join the same game using that game ID that was generated earlier by the othe player. Both of the players will see whom they are playing against. If one leaves, another can join the same game by using the same game ID. 
- We discussed how the sessions are going to work throughout the entire game. A player can have multiple session, but for one specific game there will be only one session ID
- Fadi and Joel both decided to work on the server API for the new template we are thinking about
- Shamin is going to do the templates
- Dylan is going to do the HTML templating
- Selina is going to change the way to store the session.
- Code reviewed Dylan's Html templating module and it worked fine. The board now responses with player's move by showing "x" or "0". We put a summary of the code review in the code-reviews.md file.
- We disccused about whether we can add more feature for the user such as adding password. But we all decided not to do that.

- ## Mar 29th, 2024
- **Scrum Master:** n/a
- **Recorded by:** Dylan
- **Notes submitted on:** April 1st, 2024  
- **Venue:** n/a
- **Source:** n/a
- **Time:** n/a
- **Attendance:** n/a
- **Agenda:** n/a

Notes:
- No meeting, holiday.
  
- ## Apr 1st, 2024
- **Scrum Master:** Selina
- **Recorded by:** Joel
- **Notes submitted on:** April 1st, 2024  
- **Venue:** Discord
- **Source:** Discord voice call
- **Time:** 6:30-7:30pm
- **Attendance:** Dylan, Fadi, Shamin, Joel, Selina
- **Agenda:** Do a code review for Selina's user module and it's tests, review Kanban board issues, discuss and modify serverAPI method changes, review individual feedbacks

Notes:
- Selina's code review:
  - Changed the tearDown test method in user_test.py and fixed some bugs as her review mentioned the tests needed to be improved.
  - Small change to create_session method in user.py to make the session ID as the currently selected index in the sessions dictionary instead of self
- Decided to let game.py handle invalid moves as it is more decoupled versus implementing it in serverAPI
- Decided that user's game history needs to be displayed on the homepage and in-game
  - Decided Joel will try to figure out how to show the user's history in the options menu firstly
- Fixed bug with a user object not being created properly in serverAPI
- Agreed that we need to implement make_move function in new iteration of serverAPI

## Apr 3rd, 2024
- **Scrum Master:** Shamin
- **Recorded by:** Selina
- **Notes submitted on:** Apr 3rd,2024  
- **Venue:** Discord
- **Source:** Discord voice call
- **Time:** 9.30pm-10.30pm
- **Attendance:** Selina, Dylan, Fadi, Shamin, Joel
- **Agenda:** Address final form of documentation for the end of spint/project submission. Update the relevant documents from last sprint updates. Coding tasks should be finish for final reviews on friday. Review outstanding tasks/issues on Kanban/tracker. Which will not be completed for this sprint? How will that be indicated for project status in final submission?

Notes:
- Reviewed our tasks in kanban board 
- Changed April 5th 8pm as our new pull request deadline.
- Everyone will start updating their documentation and we'll review them on Friday along with final code reviews. The process model and README files are also be updated accordingly. A more detailed user manual will be created with screenshots.
- Assigned Selina to create a user manual to show how to run the game.
- Assigned Dylan and Fadi to figure out how to implement the new feature to display opponent's last move.
- Joel and Shamin will be working on the server and html modules further.
- Noticed an important issue that was opened about server handling issues that hasn't been handled yet. Joel will take care of it before the deadline.
- The backlog features that we didn't move to to-do by now will not be implemented in this sprint. If there's anything we feel that was essential or was mentioned in the project description, we'll indicate that they are not yet implemented in the user manual.
- We have a new server layout, a code review will be made tomorrow.

## Apr 4th, 2024
- **Scrum Master:** Joel
- **Recorded by:** Dylan
- **Notes submitted on:** Apr 4th, 2024  
- **Venue:** Discord
- **Source:** Discord voice call
- **Time:** 9.00pm-10.00pm
- **Attendance:** Selina, Dylan, Fadi, Joel
- **Agenda:** Code review for final major changes of sprint 2. Review posted marking scheme for sprint 2.

Notes:
- Reviewed our tasks in kanban board.
- Reviewed marking scheme for sprint 2. 
- Performed code review for Fadi, Dylan and Joel's code for server. Game is now fully playable. Approved merge of pull request #76.
- Added a new issue for User module: sessions dictionary not updating.
- We won't highlight opponents last move, but will instead highlight the currently active board i.e. where you must place your next move. Assigned this task to Dylan.
- Changed usernames to not be case sensitive. 

## Apr 5th, 2024
- **Scrum Master:** Dylan
- **Recorded by:** Fadi
- **Notes submitted on:** Apr 5th, 2024  
- **Venue:** Discord
- **Source:** Discord voice call
- **Time:** 4.00pm-5.00pm
- **Attendance:** Selina, Dylan, Fadi, Joel, Shamin
- **Agenda:** Review final changes and review issue tracker and kanaban board

Notes:
- Made sure arch files are consistent with all other files
- Fixed a small bug with username handling in persistence. This was addressed in the meeting and after testing the bug fix we decided it was ready to accept the pull request.
- Fadi is going to record a demo of the project to include in the user manual that Selina is making.
- Review process model and user manual
- README file needs to updated. This is addressed and will be fixed before the due date.
- Noticed a bug with draws in the game. An issue has been made but a fix will not be implemented in this sprint.
- deadline has been changed to 8:30 instead of 8 because of a minor issue with docstring consistency in user.py.
- Added performance reviews for sprint 2.
