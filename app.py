from flask import Flask, request, render_template
import re

app = Flask(__name__)

##############
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/regex", methods =["Post"])
def pattern():
    # Get user input for the regular expression pattern
    user_pattern = request.form.get("regex_pattern")
    
    # Get user input data
    data = request.form.get("in_string")
    
    try:
        # Find all occurrences of the user-defined pattern in the input data
        match_results = re.findall(user_pattern, data)
        
        if match_results:
            matched_content = ', '.join(match_results)
            result = f'Thanks! The input matches the pattern: {user_pattern}. Matched content: {match_results}'
        else:
            result = f'Sorry, the input does not match the pattern: {user_pattern}. No matched content.'
    except re.error as e:
        result = f'Error in regular expression: {str(e)}'
    
    return render_template("home.html", result=result)

@app.route("/email", methods=["Post"])
def validate_email():

    email = request.form.get("input_mail")
    pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@(gmail\.com|edu\.in)$", re.IGNORECASE)

    if bool(pattern.match(email)):
        value = "valid"
    else:
        value = "invalid"
         
    return render_template("home.html", value=value)
    


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)