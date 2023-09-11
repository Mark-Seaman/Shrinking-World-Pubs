# Lesson 6 - Milestone 2 - Design

The goal of milestone 2 is to proove the technical feasibility.

## Design Role

**Product code architecture with list of data, views, modules.**

Create a product code architecture that defines the structure of the solution being created.

	App = Data + Views + Tests
	
Define the data types needed and show the dependencies as a simple outline.

Example:

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

Views for each data type

- **Student**: list, detail, create, update, delete
- **Course**: list, detail, create, update, delete
- **Assignment**: list, detail, create, update, delete

