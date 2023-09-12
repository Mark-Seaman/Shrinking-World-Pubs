# Lesson 6 - Milestone 2 - Design

The goal of milestone 2 is to prove the technical feasibility.

## Design Role

**Product code architecture with list of data, views, modules.**


## Software Architecture

Create a product code architecture that defines the structure of the solution being created.

	App = Data + Views + Tests


## Data

Use a simple outline of the key data types supported by the application.
These appear as nouns in the user stories.
Create a list of all the data types and identify the fields that will are needed
to implement the data records.

Each data type becomes a table in the database and is represented as an object class.
Each record in the table represents an object instance.
Each field in the record is stored in a column in the table.

Pay special attention to the relationships between the tables.  In the following example,
see how every assignment points to a Course and a Student.

Example of Data Design:

	- Student
		- name
		- address
		- phone
		- Course
	- Course
		- title
		- professor
		- time
	- Assignment
		- Student
		- Course
		- title 
		- description


## Views

The views match the actions (verbs) that can be performed on a data
type.

**CRUD Operations**
* CREATE - Create View
* READ - List View, Details View (many & one)
* UPDATE - Update View
* DELETE - Delete View

Views for each data type

- **Student**: list, detail, create, update, delete
- **Course**: list, detail, create, update, delete
- **Assignment**: list, detail, create, update, delete

Try to eliminate any views that are not immediately needed to simplify the design.


## Tests

Every function in your code should have an automatic test.
Test each CRUD operation on the data.
Test each CRUD operation on the views.
Plan to build 10 tests for each data type.

