Regex Matching Web App Development Project

Objective:
Your task is to replicate the core functionality of the website regex101.com. This entails creating a web application that allows users to input a test string and a regular expression (regex) and displays all the matches found.

Steps:
1. Create a new directory for your project and navigate into it.

2. Set up your virtual development environment:
   - Install Flask, a Python web framework, using pip if not already installed: `pip install Flask`.

3. Initialize a new Flask application:
   - Create a new Python file named `app.py`.
   - Import Flask and create a new Flask app instance.
   - Define a route for the home page ("/") where users can input the test string and regex.
   - Render an HTML template containing a form with fields for the test string and regex, and a submit button.

4. Create the HTML template:
   - Create a new directory named `templates` within your project directory.
   - Inside the `templates` directory, create a new HTML file named `index.html`.
   - Design the HTML form with input fields for the test string and regex, and a submit button.

5. Define a route to handle form submission:
   - Define a new route ("/results") in your `app.py` file to handle form submission.
   - Extract the test string and regex submitted by the user from the form data.
   - Use Python's `re` module to perform regex matching on the test string.
   - Store the matched strings in a list.

6. Render the results:
   - Pass the list of matched strings to the HTML template.
   - Modify the HTML template to display the matched strings below the input form.

7. Test your application:
   - Run your Flask application (`python app.py`).
   - Open a web browser and navigate to http://localhost:5000 to access your application.
  - Input various test strings and regex patterns to ensure the application displays the correct matches.

8. (BONUS) Implement a new route where a user can validate if a given email id is valid or not.

9. (IMPORTANT) Deploy the application on AWS Cloud.
