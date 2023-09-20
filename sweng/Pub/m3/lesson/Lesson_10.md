# Lesson 9 - Milestone 3 - Design


## Refactoring

Refactoring, as taught by Martin Fowler, is a disciplined technique for restructuring and improving the quality of existing code without changing its external behavior. It's a crucial practice in software development that helps developers keep their codebase clean, maintainable, and adaptable to changing requirements. Martin Fowler, along with Kent Beck and others, has contributed significantly to the popularization of refactoring techniques.

Here are the key principles and practices of refactoring, as taught by Martin Fowler:

**Maintain External Behavior:** The most fundamental principle of refactoring is that you should not change the observable behavior of the code when you refactor it. This means that the inputs, outputs, and side effects of the code must remain the same after the refactoring is complete.

**Small, Incremental Changes:** Refactoring is performed through a series of small, incremental changes to the code. Each step should be simple and well-understood, making it easy to verify that the behavior remains intact.

**Comprehensive Testing:** Before starting any refactoring, it's essential to have a comprehensive suite of automated tests in place. These tests act as a safety net, allowing you to detect regressions quickly. After each refactoring step, you should rerun the tests to ensure you haven't introduced any defects.

**Code Smells:** Martin Fowler and Kent Beck introduced the concept of "code smells" in their book "Refactoring: Improving the Design of Existing Code." Code smells are indicators of potential issues in your code, such as duplicated code, long methods, or excessive complexity. Recognizing these smells is the first step in identifying areas where refactoring can be beneficial.

**Catalog of Refactorings:** Martin Fowler's book on refactoring includes a catalog of common refactoring techniques. This catalog provides detailed descriptions of various refactorings, such as Extract Method, Rename Variable, or Replace Conditional with Polymorphism. These refactorings serve as practical guidelines for improving code quality.

**Continuous Improvement:** Refactoring is not a one-time activity; it's an ongoing process. As you work on your codebase, you should constantly look for opportunities to refactor and make improvements. This helps prevent code from becoming overly complex and difficult to maintain over time.

**Refactoring Tools:** To facilitate refactoring, many integrated development environments (IDEs) provide built-in or third-party refactoring tools. These tools automate many of the tedious aspects of code restructuring, making it easier and safer to refactor.

**Example: Extract Method Refactoring**

One of the most commonly used refactoring techniques is "Extract Method." This refactoring is used when you have a block of code that can be grouped into a separate method with a meaningful name. Here's an example:

**Original Code:**

    public double calculateTotalPrice(List<Product> products) {
        double totalPrice = 0.0;
        for (Product product : products) {
            totalPrice += product.getPrice();
        }
        return totalPrice;
    }

In this example, we have a method that calculates the total price of a list of products. We can apply the "Extract Method" refactoring to improve code readability and maintainability:

**Refactored Code:**

    public double calculateTotalPrice(List<Product> products) {
        double totalPrice = 0.0;
        for (Product product : products) {
            totalPrice += getProductPrice(product);
        }
        return totalPrice;
    }

    private double getProductPrice(Product product) {
        return product.getPrice();
    }

In this refactoring, we extracted the code responsible for getting the product price into a separate method called getProductPrice(). This makes the code more readable and also allows us to reuse this logic if needed.

By following the principles and practices of refactoring as taught by Martin Fowler, developers can maintain and improve their codebase over time, making it easier to understand, modify, and extend. This leads to more robust and maintainable software systems.


# Tutorial Video

<iframe width="481" height="271" src="https://www.youtube.com/embed/7oZBfpI_hxI" title="4 Tips for Refactoring Your Code for Readability" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


# AI Prompts

Here are some interesting AI prompts to try.

* Identify the core data types within my app [app overview]

* Try to reduce the data types to support.

* Create Django data model for Student: name, email, github, server

* Write function stubs for views of Student data type: List, Detail, Edit, Create, Delete

