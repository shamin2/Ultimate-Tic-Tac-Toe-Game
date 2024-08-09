# Process Model
The different aspects of our process model will be outlines in this document.
We want to capture the aspects of a software process that need to identified,
controlled, measured and evaluated, so we can make sure the project is advancing 
and make changes to the process as necessary.

### Sprint 1 final pull request deadline for code: 5:00 PM, March 16th, 2024
### Sprint 2 final pull request deadline for code: 8:30 PM, April 5th, 2024
 
### Main activities:
Project Vision: Develop a dynamic, engaging 2-player Ultimate Tic-Tac-Toe game server, emphasizing teamwork, continuous improvement, and quality.

### Team Composition:
- Scrum Master (Rotating): Facilitates Scrum meetings, ensuring adherence to Agile practices. The role rotates each meeting, selecting one of the development team members to ensure everyone knows the different parts of development. 
- Development Team: Works collaboratively on design, development, testing, and deployment, with flexibility in task assignments.
  - Fadi Baghdadi
  - Joel Hicks
  - Dylan Winter
  - Selina Elvayn
  - Shamin Yasar

### Cycle of Activities:

##### Sprint Planning:
- Rotating Scrum Master: The incoming Scrum Master leads the planning, ensuring a fresh perspective on task prioritization and sprint goals.
- Tasks Assignment: Tasks are chosen from the Kanban board; developers express interest or are assigned based on skills and sprint goals.

##### Scrum Meetings (3 per week):
- Rotating Scrum Master: Leads the meeting, facilitating updates and discussions on progress and impediments.

##### Development Work:
- Once a task is decided on in a team meeting, it should be assigned a member. The member is supposed to make a task on the kanban board and meet the deadline.
- Once the task is completed. A discussion of next steps/tasks should be done.
- Task Reassignment: Requires permission from the original assignee to ensure respect and communication within the team.
- Code Reviews: Scheduled bi-meeting to ensure code quality and adherence to standards. Facilitated by the current Scrum Master, but peer-reviewed by team members.
- Performance Reviews: Conducted at the end of each sprint, focusing on individual contributions, learning, and areas for improvement.
- If an issue between team members rise, they should address this in the issue tracker so the other team members are notified and can work on a solution together. If no issues are present, suggestions for improvements will be made in the performance reviews at the end of each sprint.

##### Accepting Pull Requests / Code Review Criterion:
- Dylan is in charge of accepting pull requests, and the requirements we have are:
- The code should go through a code review with every member attending before it is accepted
- The code should be written in the format and style that was decided and being used by other team members.
- The code shouldn't conflict with the other codes its interacting with.
- If any of the method names are changed, other members should be notified in the code review.
- The functionality claimed for the code revision should be present
- None of the existing functionality of the app should regress to a non-working state
- The app should run correctly with the changes made, the parts that are not working should be noted as a to do to look into it later.

##### Updating Documents:
- Docs can be updated by team members in the master branch without needing a PR each time.
- These changes should be consistent with what the team has in mind and what was discussed in the meetings.
- To ensure consistency these documents will be reviewed before the deadline by the whole team.
  
##### Sprint Review & Retrospective:
- Inclusive Reflection: With the rotating Scrum Master, each team member can share insights from their leadership experience, enhancing the retrospective's value.

### Tools and Supporting Practices:

- Kanban Board & Issue Tracker: Central to task management, allowing for dynamic task selection and transparency in reassignments.
  - Kanban board is used to allow us to keep track of tasks that need to be done. It should be kept up-to-date and relevant to current state of the project.
  - Issue Tracker should be adhered to whenever a problem is faced. This is to allow us to keep track of what is still left to figure out.
- Code Review Cycle: Encourages continuous improvement and learning. The rotating Scrum Master ensures reviews are scheduled and completed.
- Performance Evaluations: Aim to recognize achievements, address challenges, and set goals for individual growth, enhancing team dynamics and project outcomes.
 
### Source Control Strategy:
- The changes to code will be made through each team member's own branch. Team members are free to create branches according to their needs but they should try and keep it minimal.
- Each member's code will be reviewed in a meeting using our Code Review criterion. If it seems appropriate they can open a pull request with their changes and it will be merged by Dylan.
   
### Evaluation and Adaptation:

- Adaptive Leadership: Rotating the Scrum Master role encourages adaptability and shared responsibility, fostering a well-rounded team.
- Task Management: The process for changing task assignments is formalized to respect ownership and encourage collaboration.
- Continuous Feedback Loops: Through code and performance reviews, the team maintains high standards and continuously adapts to improve efficiency and output quality.

### Handling of incomplete features
- Stuff that was not implemented in this sprint is outlined in the arch documents provided for each module. Refer to README.md for location.
- Present bugs that affect the user experience are mentioned in the user manual.
- All kinds of bugs and inconsistencies are kept track of using the issue tracker. If anyone notices that something is not right, they should make an issue about it.
- Future ideas that are not implemented yet are documented in the backlog of the kanban board. 
