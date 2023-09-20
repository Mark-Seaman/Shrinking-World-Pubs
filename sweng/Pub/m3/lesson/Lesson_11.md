# Lesson 9 - Milestone 3 - Code

## Iterative Development

Uncle Bob Martin, also known as Robert C. Martin, is a well-respected software engineer and one of the leading figures in the software development community. He has advocated for various software development principles and practices, including iterative development. Iterative development is a fundamental approach to building software systems, and Uncle Bob's teachings emphasize its importance. 

Development Process


* **Incremental and Iterative:** Iterative development is a software development approach that focuses on building a system in small, incremental steps. Instead of trying to create the entire system in one go, developers work on a series of iterations, each of which adds new functionality or improvements to the existing system. These iterations are typically short and time-boxed, often lasting a few weeks.

* **Progressive Refinement:** Uncle Bob emphasizes that during each iteration, developers should aim to deliver a working and potentially shippable product increment. This means that at the end of each iteration, the software should be in a state where it could be deployed if needed. However, it may not yet contain all the desired features.

*  **Feedback-Driven:** Iterative development thrives on feedback. By delivering working increments of the software at the end of each iteration, stakeholders, including end-users and business representatives, can provide feedback on the product's functionality and quality. This feedback loop is essential for adjusting priorities, clarifying requirements, and ensuring the system aligns with business objectives.

*  **Adaptability:** Uncle Bob emphasizes the importance of adaptability in iterative development. As feedback is received and new information becomes available, the development team can adapt and adjust their plans for subsequent iterations. This flexibility allows the system to evolve in response to changing requirements or insights gained during development.

*  **Risk Mitigation:** Iterative development helps mitigate project risks. Instead of waiting until the end of a lengthy development cycle to discover issues or misunderstandings, potential problems are uncovered early in the process. This allows for timely course corrections and reduces the likelihood of costly late-stage changes.

*  **Prioritization:** In iterative development, the most critical and valuable features are often tackled first. This ensures that high-priority functionality is delivered early in the project, providing immediate benefits to users and stakeholders.

*  **Test-Driven Development (TDD):** Uncle Bob often promotes practices like Test-Driven Development (TDD) within iterative development. TDD involves writing automated tests before writing code, ensuring that each piece of functionality is thoroughly tested. This practice enhances code quality and reliability throughout the iterative process.

*  **Continuous Integration and Deployment:** In alignment with iterative development, Uncle Bob emphasizes the importance of continuous integration and deployment (CI/CD) practices. CI/CD pipelines automate the building, testing, and deployment of code changes, allowing for faster and more reliable delivery of software increments.


## Example of Iterative Development

Imagine a team developing an e-commerce website. In an iterative approach:

- **Iteration 1:** The team focuses on creating the basic structure of the website, including user registration and product browsing.

- **Iteration 2:** Additional features like shopping cart functionality and product reviews are added.

- **Iteration 3:** Payment processing and order tracking features are implemented.

- **Iteration 4:** The team works on optimizing website performance and addressing user interface improvements based on feedback.

Throughout these iterations, the website gradually evolves, and each iteration delivers a working, potentially shippable product increment. Feedback from users and stakeholders guides the team's priorities and decisions, ensuring that the website aligns with the evolving requirements and business goals.

In summary, Uncle Bob Martin's teachings on iterative development emphasize building software in small, incremental steps, delivering working increments at the end of each iteration, and using feedback to drive development decisions. This approach promotes adaptability, risk mitigation, and a focus on delivering high-priority features early in the project, ultimately leading to more successful and responsive software projects.


Here are some simple code examples that illustrate the concept of iterative development, incorporating feedback and delivering working increments at the end of each iteration.

**Example: Building a To-Do List Application**

Imagine you're building a to-do list application in Python using an iterative development approach. Here's how the development might progress through several iterations:

**Iteration 1: Basic To-Do List**
In this first iteration, you focus on creating a basic to-do list with the ability to add and list tasks.

```python
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks:
            print(task)

# Initial usage
todo_list = TodoList()
todo_list.add_task("Buy groceries")
todo_list.add_task("Write a report")
todo_list.list_tasks()
```

**Iteration 2: Mark Tasks as Completed**
In the second iteration, you add the ability to mark tasks as completed.

```python
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def list_tasks(self):
        for task in self.tasks:
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{status} {task['task']}")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True

# Iteration 2 usage
todo_list = TodoList()
todo_list.add_task("Buy groceries")
todo_list.add_task("Write a report")
todo_list.complete_task(0)  # Mark the first task as completed
todo_list.list_tasks()
```

**Iteration 3: Remove Completed Tasks**
In the third iteration, you add the ability to remove completed tasks.

```python
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{i+1}. {status} {task['task']}")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True

    def remove_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task["completed"]]

# Iteration 3 usage
todo_list = TodoList()
todo_list.add_task("Buy groceries")
todo_list.add_task("Write a report")
todo_list.complete_task(0)
todo_list.remove_completed_tasks()  # Remove completed tasks
todo_list.list_tasks()
```

With each iteration, the to-do list application becomes more feature-rich and refined. It demonstrates the incremental and feedback-driven nature of iterative development, where each iteration builds upon the previous one and delivers a working product increment.


# Tutorial Video

<iframe width="481" height="271" src="https://www.youtube.com/embed/T8xvMIiFzD0" title="How To Create An MVP" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>



# AI Prompts

Here are some interesting AI prompts to try.

* Create Django data model for Student: name, email, github, server

* Explain how to migrate the database

* Write functions for views of Student data type: List, Detail, Edit, Create, Delete

* Create tests for Student data and Student views

