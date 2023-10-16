# Lesson 18 - Milestone 5 - Design


## Design support to team members

In order to ensure that team members have the resources and guidance they need to complete their
tasks effectively, it is important to provide assistance and support. This can involve answering
questions, offering clarification, and providing guidance on best practices. By offering help, the
designer can help the team members overcome any obstacles they may encounter and ultimately
contribute to the successful completion of the project.

To collaborate with the project manager on project evaluation, the designer works closely with them
to assess the progress and effectiveness of the project. This includes evaluating the overall
performance of the team, identifying areas for improvement, and determining if the project is on
track to meet its goals. By collaborating with the project manager, the designer can ensure that
any necessary adjustments or improvements are made to optimize the project's success.

Seeking feedback from team members on design improvements is an important step in the development
process. By gathering input from different perspectives, the designer can identify potential issues
or areas for improvement that may not be obvious to them. This feedback helps refine and enhance
the design, ensuring it meets the needs and expectations of customers. Actively seeking feedback
demonstrates the designer's commitment to creating the best possible product.


## Refactoring

Refactoring is the process of making changes to the design to improve its structure and readability.
Selecting one design area and refactoring it can simplify the design and make it more efficient. A
refactoring report is a comprehensive document that highlights the changes made to the design
throughout the development process. It compares the design before and after the refactoring
process, explaining the reasons for the changes and the impact they had on the overall product.
This report serves as a reference for future iterations or updates.

Refactoring is a crucial skill for software developers. It's the art of improving the design of existing code without changing its behavior. By refactoring code, we can make it more readable, maintainable, and efficient. While there are many refactoring techniques, here are the six most important ones, as outlined by Martin Fowler:

### Extract Method

Imagine you have a long and convoluted method that performs multiple actions. It's hard to understand and debug. The Extract Method refactoring comes to the rescue. It allows us to take a block of code within a larger method and extract it into a separate method. Let's look at an example in Python:

    def calculate_total_price(quantity, unit_price):
        total_price = quantity * unit_price
        tax = total_price * 0.1
        discounted_price = total_price - tax
        shipping_cost = calculate_shipping_cost(quantity)
        final_price = discounted_price + shipping_cost
        return final_price

    def calculate_shipping_cost(quantity):
        return 5 * quantity

In this example, we extract the code responsible for calculating shipping cost into a separate method called `calculate_shipping_cost()`. This makes the code more readable and allows us to reuse the shipping cost calculation logic in other parts of our code.

### Inline Method

On the flip side, the Inline Method technique involves removing a method and placing its code directly into the calling code. This refactoring is useful when a method becomes unnecessary due to changes in the codebase or when the method no longer provides value. Let's take a look at an example:

    class Order:
        def __init__(self, total_price):
            self.total_price = total_price

        def get_total_price(self):
            return self.total_price

        def calculate_discounted_price(self):
            discount = 0.2
            discounted_price = self.total_price * (1 - discount)
            return discounted_price

    order = Order(100)
    discounted_price = order.calculate_discounted_price()

In this example, the `calculate_discounted_price()` method doesn't add much value since it's just a simple calculation. We can inline the method, removing the extra layer of abstraction:

    class Order:
        def __init__(self, total_price):
            self.total_price = total_price

        def get_total_price(self):
            return self.total_price

    order = Order(100)
    discounted_price = order.total_price * 0.8

By inlining the method, we improve the clarity of the code.

### Extract Variable

Complex expressions can hinder code readability. The Extract Variable refactoring allows us to break down these expressions into smaller, more readable parts by assigning them to variables. Let's see an example:

    def calculate_order_total(quantity, unit_price, tax_rate):
        total_price = quantity * unit_price
        tax = total_price * tax_rate
        discounted_price = total_price - tax
        shipping_cost = 5 * quantity
        final_price = discounted_price + shipping_cost
        return final_price

In this example, the expression `quantity * unit_price` is repeated twice. We can improve the readability by extracting it into a variable:

    def calculate_order_total(quantity, unit_price, tax_rate):
        total_price = quantity * unit_price
        tax = total_price * tax_rate
        discounted_price = total_price - tax
        shipping_cost = 5 * quantity
        final_price = discounted_price + shipping_cost
        return final_price

By assigning the expression to the variable `total_price`, we make the code easier to understand and modify.

### Inline Variable

Sometimes, variables are only referenced once in the code, which adds unnecessary complexity. The Inline Variable technique allows us to replace the variable with its value in places where it is only referenced once. Let's take a look at an example:

    def calculate_circle_area(radius):
        pi = 3.14
        circle_area = pi * radius * radius
        return circle_area

In this example, the variable `pi` is only used once. We can inline it:

    def calculate_circle_area(radius):
        circle_area = 3.14 * radius * radius
        return circle_area

By eliminating the variable `pi`, we reduce clutter in the code and make it more concise.

### Move Method

Sometimes, a method is more closely related to another class than its current class. The Move Method refactoring allows us to relocate the method from one class to another. Let's see an example:

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def calculate_area(self):
            return self.width * self.height

    class Square:
        def __init__(self, side):
            self.side = side

        def calculate_area(self):
            return self.side * self.side

In this example, both `Rectangle` and `Square` classes have a method called `calculate_area()`, even though the calculation logic is different. We can move the `calculate_area()` method from `Square` to `Rectangle` to improve code coherence:

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def calculate_area(self):
            return self.width * self.height

    class Square(Rectangle):
        def __init__(self, side):
            super().__init__(side, side)

By moving the `calculate_area()` method, we ensure that each class is responsible for its own data and behavior.

### Rename Method

Choosing clear and descriptive names for methods is essential for code readability. The Rename Method refactoring involves changing the name of a method to better reflect its purpose and improve its readability. Let's consider an example:

    class Calculator:
        def calculate(self, a, b):
            return a + b

In this example, the method name `calculate` is too generic. We can rename it to `add_numbers`:

    class Calculator:
        def add_numbers(self, a, b):
            return a + b

By choosing a clearer and more descriptive name, we make the code more self-explanatory and maintainable.

These six important refactorings provide a solid foundation for improving code quality and maintainability. By applying these techniques, we can enhance the structure, readability, and flexibility of our code, making it easier to understand and modify in the long run. Happy refactoring!


## Design pattern catalog

Building a design pattern catalog can greatly benefit software development teams. It provides a
comprehensive overview of different design patterns that can be used in a project, ensuring
consistency and best practices. Let's go through the steps of creating a design pattern catalog
together.

First, understand the project requirements. Take the time to thoroughly grasp the project goals and
constraints. This will help you select the most appropriate design patterns for the project.

Examine your code to look for design patterns.  Categorize the design patterns according to their
purpose and usage. Group them as creational, structural, or behavioral patterns. This will make it
easier to find the right pattern for a particular scenario.

Show concrete examples from your code. Show how they can be implemented in real-world scenarios that
are relevant to the project. By doing so, you'll help the team understand how to apply the patterns
effectively.

Explain the benefits of using each design pattern. Highlight how the patterns can improve code
quality, maintainability, flexibility, and reusability. This will demonstrate the value of design
patterns to the team.

Include design guidelines or best practices for each pattern. These guidelines will outline the
recommended ways to use the pattern and any potential pitfalls to avoid. By following these
guidelines, the team can ensure effective implementation.

Keep the design pattern catalog updated. Design patterns evolve, and new patterns may emerge.
Regularly review and revise the catalog to ensure its relevance and value.

Building a design pattern catalog should be a collaborative effort. Involve experienced software
developers, architects, and designers in the process. Make the catalog easily accessible to the
team in a digital format like a wiki or shared document.

Creating and maintaining a design pattern catalog will enable the team to consistently apply
efficient design practices, resulting in high-quality software products.


## Help with implementation

Once the design is finalized, it is time to start implementing the code and testing it. The designer
can provide support to the team during this phase to help finish the code and ensure it is
functioning correctly. This can involve offering guidance on best practices, troubleshooting any
issues that arise, and assisting with testing and debugging. By providing help with implementation,
the designer can contribute to the successful completion of the project.

