# Shrinking World Development Process

A special kind of TDD


## Development Formula


### Create a plan for today

Define a big goal requiring a day of work

Break the day goal into medium goals (requiring two hours)

Break each medium goal into tasks (requiring less than 1/2 hour)


### Workflow Iterate over each task

Follow this process while coding!  Repeat these steps with each of the smallest tasks.

**Test** - Build a test that fails showing you the code that is currently missing.

**Fix** - Write the minimum code to pass the test.

**Enhance** - Make the code better and more robust.

**Improve** - Make the code beautiful and simple without duplication.

---

## Example Project Breakdown


### Project: Ghost Writer

### Build Automatic Chapter Publisher **<-- Day goal**

Read and Understand Outline for Pub. **<-- Two Hour goal**

    Read outline file (indented text). <-- Half Hour goal
    Recognize three levels of headings
    Build tree structure for outline
    Print the outline with Markdown headers

Convert Outline into Table of Contents

    ...

Create Index.md File with Links to Pages

    ...

Publish the Pub Content

    ...


---

## Ghost Writer Chapter Publisher

Development Loop for Tasks


### Read outline file (indented text)

Test

    def test_outline_file():
        assert read_outline()

Fix

    def read_outline():
        return Path('Software Engineering').read_text()

Enhance

    tests.py

        def test_outline_file():
            text = read_outline('Software Engineering')
            assert text

    ghost.py

        def read_outline(path):
            return Path(path).read_text()

Improve

    tests.py

        def test_outline_file():
            text = read_outline('Software Engineering')
            assert text.startswith('Practical Skills in Software Engineering')

    ghost.py

        def read_outline(path):
            path = Path(path)
            if path.exists():
                text  = path.read_text()
                assert text
                return text
            return "File Not Found" + path

---

### Recognize three levels of headings

Test

Fix

Enhance

Improve


---

### Build tree structure for outline

Test

Fix

Enhance

Improve


---


### Print the outline with Markdown headers

Test

Fix

Enhance

Improve


