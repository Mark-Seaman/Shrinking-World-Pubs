# Lesson 6 - Milestone 2 - Test

The goal of milestone 2 is to prove the technical feasibility.

## Test Role

**Automated deployment from source code**


## Automated Deployment

Devops is the combination of development and operations.   This is how the dev team gets the code onto the web application hosting environment.  

Set up some form of continuous integration and continuous deployment:

- One command to perform the deployment from source code
- A process to monitor the build and escalate the failures (may be manual or automated)


## Automated Test

Build an automatic test that loads the web page from the server.  Create a script to be run
from your local computer that gets web pages from the server and looks to see that they
contain the proper text.

Example Page Tester:

    import requests
    from bs4 import BeautifulSoup

    # Define the URL
    url = "https://shrinking-world.com"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find and extract the title tag
        title_tag = soup.find('title')
        
        # Check if the title tag exists and contains text
        if title_tag and title_tag.string:
            print(f"Title: {title_tag.string}")
        else:
            print("Title not found on the webpage.")
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")

Setup:

    pip install requests beautifulsoup4
    
