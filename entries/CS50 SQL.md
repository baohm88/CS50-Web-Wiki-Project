# CS50 SQL

By Ha Manh Bao

Video overview: <https://youtu.be/Hacqh8vgcqQ>

## Scope

The db for CS50 SQL includes all entities necessary to facilitate the process of tracking the completion and expiration of each safety course completed by each employee and notifying them of this so they can take refresher courses to ensure their training is always valid and up to date. As such, included in the db's scope is:

* employees, including basic identification info
* instructors, including basic identification info
* courses, including basic info about the course such as id and title
* sesions, including the id for a particular session, the date on which the session took place, the id of the instructor conducting that session and the id of the safety course associated with that session
* classes, including the id for the session conducted and the id of the employees taking that session
* Ratings, including the id of sessions and the rating given by each employee for the session he/she took

Out of scope are the exam grades

## Functional Requirements

This database will support:
* CRUD operations for employees and instructors
* tracking the completion and expiration of safety training courses for all employees
* Allowing the employees to leave a rating for a session(course) they took