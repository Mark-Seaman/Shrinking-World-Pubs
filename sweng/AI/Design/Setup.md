# Tools Setup

## Development Process Setup

To setup the development process using Django/Python, Visual Studio Code, and Github, follow the steps below:

1. Install Python:
   * Download Python from the official website: https://www.python.org/downloads/
   * Follow the installation instructions for your operating system.

2. Install Django:
   * Open a terminal or command prompt.
   * Run the following command to install Django: 
     ```
     pip install django
     ```

3. Create a new Django project:
   * Open a terminal or command prompt.
   * Navigate to the directory where you want to create the project.
   * Run the following command to create a new Django project named "myproject":
     ```
     django-admin startproject myproject
     ```
   * This will create a new directory named "myproject" with the project structure.

4. Install Visual Studio Code:
   * Download Visual Studio Code from the official website: https://code.visualstudio.com/
   * Follow the installation instructions for your operating system.

5. Open the project in Visual Studio Code:
   * Open Visual Studio Code.
   * Click on "File" > "Open Folder".
   * Navigate to the "myproject" directory and select it.
   * Visual Studio Code will open the project in a new window.

6. Install the Python extension in Visual Studio Code:
   * Click on the "Extensions" icon in the sidebar (or press `Ctrl+Shift+X`).
   * Search for "Python" in the extensions marketplace.
   * Click on the "Python" extension by Microsoft and click on the "Install" button.
   * This will enable Python support in Visual Studio Code.

7. Setup a virtual environment:
   * Open a terminal in Visual Studio Code (click on "View" > "Terminal").
   * Run the following command to create a virtual environment:
     ```
     python -m venv venv
     ```
   * This will create a new directory named "venv" inside the project.
   * Activate the virtual environment by running the appropriate command for your operating system:
     - On Windows (PowerShell): `venv\Scripts\Activate.ps1`
     - On macOS/Linux (Bash): `source venv/bin/activate`

8. Install Django in the virtual environment:
   * Make sure the virtual environment is activated.
   * Run the following command to install Django:
     ```
     pip install django
     ```

## GitHub Setup

To setup GitHub for your project, follow the steps below:

1. Create a GitHub account:
   * Go to the GitHub website: https://github.com/
   * Sign up for a new account if you don't have one.

2. Create a new repository:
   * Click on the "+" icon in the top-right corner and select "New Repository".
   * Enter a name for your repository (e.g., "myproject").
   * Optionally, provide a description for your repository.
   * Choose whether you want to make the repository public or private.
   * Click on the "Create repository" button.

3. Connect your local project to the GitHub repository:
   * In Visual Studio Code, go to the source control sidebar (click on the icon with three horizontal lines).
   * Click on the "Initialize Repository" button to initialize a new Git repository.
   * Stage and commit your initial files (README, .gitignore, etc.).

4. Add the remote repository:
   * Go to your GitHub repository page.
   * Copy the URL of your repository (e.g., https://github.com/your-username/myproject.git).
   * In Visual Studio Code, open the command palette (press `Ctrl+Shift+P`).
   * Search for "Git: Add Remote" and select it.
   * Paste the repository URL and press `Enter`.

5. Push your local project to GitHub:
   * In Visual Studio Code, go to the source control sidebar.
   * Click on the three dots (...) and select "Push" to push your changes to GitHub.

Congratulations! You have successfully setup the development process using Django/Python, Visual Studio Code, and GitHub.

# Tutorial: Building a "Hello World" App

## Step 1: Create a Django App

1. Open a terminal in Visual Studio Code.
2. Make sure the virtual environment is activated.
3. Run the following command to create a new Django app named "helloworld":
   ```
   python manage.py startapp helloworld
   ```

## Step 2: Define a View

1. Open the file `myproject/helloworld/views.py` in Visual Studio Code.
2. Replace the contents of the file with the following code:
   ```python
   from django.http import HttpResponse

   def hello_world(request):
       return HttpResponse("Hello, World!")
   ```

## Step 3: Configure URL Mapping

1. Open the file `myproject/myproject/urls.py` in Visual Studio Code.
2. Add the following import statement at the top of the file:
   ```python
   from helloworld.views import hello_world
   ```
3. Replace the `urlpatterns` list with the following code:
   ```python
   from django.urls import path

   urlpatterns = [
       path('hello/', hello_world),
   ]
   ```

## Step 4: Run the Development Server

1. Open a terminal in Visual Studio Code.
2. Make sure the virtual environment is activated.
3. Run the following command to start the development server:
   ```
   python manage.py runserver
   ```

## Step 5: Test the "Hello World" App

1. Open a web browser.
2. Visit the URL `http://localhost:8000/hello/`.
3. You should see the text "Hello, World!" displayed in the browser.

Congratulations! You have successfully built a "Hello World" app using Django/Python.

Unordered List of Tools Setup:
- Python
- Django
- Visual Studio Code
- GitHub

*Note: Make sure to follow the tutorials and documentation provided for each tool for detailed instructions on installation and usage.*