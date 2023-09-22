# Lesson 12 - Milestone 3 - Test

## Test-Driven Development

Test-Driven Development (TDD) is a software development methodology that emphasizes writing tests before writing the actual code. It follows a cycle of "Red-Green-Refactor" to ensure code quality and maintainability. In this explanation, I'll break down TDD into its key principles, the TDD cycle, and provide examples to illustrate each step.

**Key Principles of TDD:**

**Write Tests First:** 

In TDD, you begin by writing a failing test that specifies the desired behavior of the code you're about to write. This test is a small, automated script that checks if the code functions as expected.

**Write the Minimum Code:** 

After writing the failing test, you write the minimum amount of code necessary to make the test pass. This code should be simple and straightforward.

**Refactor:** 

Once the test passes, you can refactor the code without changing its external behavior. This step ensures that the code remains clean, maintainable, and efficient.

**Repeat:** 

The TDD cycle continues iteratively for each new piece of functionality or feature you want to add. Write a failing test, write the minimum code to pass it, and refactor as needed.

**The TDD Cycle:**

Let's break down the TDD cycle into three main phases:

**Red:** 

In this phase, you write a failing test case. You're essentially defining what you want the code to do. Your test case checks whether the code exhibits the expected behavior. 

    *Example: Imagine you're building a simple calculator, and you want to add two numbers.*

    def test_addition():
        result = add(2, 3)
        assert result == 5  # This test will fail initially because 'add' is not defined yet.

**Green:** 

In this phase, you write the minimum code to make the test pass. Your goal is to make the test case go from red (failing) to green (passing).

    *Example: You implement the 'add' function.*

    def add(a, b):
        return a + b

**Refactor:** 

In this phase, you review your code to improve its structure, readability, or performance. You make changes without altering the external behavior validated by the test. 

    *Example: You refactor the 'add' function for clarity.*

    def add(augend, addend):
        return augend + addend

**Repeat:** 

You continue this cycle, adding more tests and code incrementally to build your application while ensuring that it behaves correctly and efficiently. Each cycle tightens the code and improves its quality.

**Why TDD?**

TDD offers several benefits:

- **Improved Code Quality:** Writing tests first helps clarify your code's requirements and behavior, resulting in more robust and reliable software.

- **Rapid Feedback:** TDD provides immediate feedback when you introduce a bug or break existing functionality. This makes debugging easier and more efficient.

- **Maintainability:** The refactoring step ensures that your code remains clean and adaptable to future changes.

- **Collaboration:** Tests serve as documentation and help team members understand the intended functionality of your code.

**Common Testing Frameworks:**

TDD is typically implemented using testing frameworks for various programming languages. Here are a few examples:

- **Python:** The Python ecosystem has libraries like `unittest`, `pytest`, and `nose` for TDD.

- **JavaScript:** JavaScript developers often use `Jest`, `Mocha`, or `Jasmine` for testing.

- **Java:** Java developers can use `JUnit` for unit testing and `TestNG` for more advanced testing scenarios.

**Additional Concepts:**

**Unit Testing:** TDD primarily focuses on unit testing, where you test individual components (e.g., functions or methods) in isolation. This helps identify issues at the smallest level.

**Integration Testing:** In addition to unit tests, integration tests ensure that different components work together correctly.

**Continuous Integration (CI):** CI systems like Jenkins, Travis CI, or CircleCI automatically run your tests whenever you make changes to your code, ensuring that new code doesn't break existing functionality.

**Test Doubles:** During testing, you might use test doubles like mocks, stubs, or fakes to isolate the code being tested.

**Example: Building a Simple Stack**

Let's illustrate TDD with an example of building a simple stack data structure using Python and the `unittest` framework.

**Red:** Write a failing test for the stack's `push` and `pop` operations.

    import unittest

    class TestStack(unittest.TestCase):
        def test_push(self):
            stack = Stack()
            stack.push(5)
            self.assertEqual(stack.pop(), 5)  # This test will fail as the Stack class doesn't exist yet.

**Green:** Write the minimum code to make the test pass. Implement the `Stack` class with `push` and `pop` methods.

    class Stack:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            if not self.is_empty():
                return self.items.pop()
            else:
                raise IndexError("pop from empty stack")

**Refactor:** No refactoring is needed in this simple example.

**Repeat:** Continue adding more test cases and code for other stack operations like `is_empty`, `peek`, and error handling.

By following the TDD cycle, you ensure that each piece of functionality you add to your stack is tested thoroughly, and you have confidence that it works correctly. This iterative process continues as you expand your stack's capabilities and maintain its quality.

In summary, Test-Driven Development is a software development approach that promotes writing tests before writing code. It follows a cycle of "Red-Green-Refactor" to ensure code quality, rapid feedback, and maintainability. It is widely used across different programming languages and helps in building reliable and robust software.


# Tutorial Video

<iframe width="481" height="271" src="https://www.youtube.com/embed/Jv2uxzhPFl4" title="Test-Driven Development // Fun TDD Introduction with JavaScript" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="481" height="271" src="https://www.youtube.com/embed/amkDB_oPix0" title="Test-Driven Development explained in 3 minutes" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


# AI Prompts

Here are some interesting AI prompts to try.

* Show how to setup Django automated tests.

* Create tests for Student data and Student views.

* Explain how to run the debugger in Visual Studio Code.

* Explain how to create an "implementation spike".

