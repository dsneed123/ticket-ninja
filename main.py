import webview
import json

# Get login data from the JSON file
def load_login_info():
    with open('login_info.json') as f:
        return json.load(f)

# Sign into the ticket claim page
def signin(window):
    login_info = load_login_info()
    username = login_info['username']
    password = login_info['password']
    print(username)
    # JavaScript code to auto-fill and submit the login form
    js_code = f'''
    setTimeout(function() {{
        var email = document.getElementById('signin-email-input');
        if (email) {{
            email.value = '{username}';
        }}
    }}, 1000);

    setTimeout(function() {{
        var signinButton = document.getElementById('signin-submit-btn');
        if (signinButton) {{
            signinButton.click();
        }}
    }}, 1000);

    // Wait for 1 second before setting the password
    setTimeout(function() {{
        var pass = document.getElementById('password');
        if (pass) {{
            pass.value = '{password}';
        }}
    }}, 1000); // 1000 ms = 1 second delay

    // Wait for an additional 0.5 seconds before clicking the sign-in button again
    setTimeout(function() {{
        var signinButton = document.getElementById('signin-submit-btn');
        if (signinButton) {{
            signinButton.click();
        }}
    }}, 1500); // 1500 ms = 1.5 seconds total delay, which includes the 1-second delay from earlier
    '''

    # Inject JavaScript after the page is loaded
    window.evaluate_js(js_code)

# Create and start the webview window
def create_webview():
    # Create the webview window
    view = webview.create_window('Zag ticket claim', "https://gozags.evenue.net/signin?continue=%2F")

    # Define the function to run after the page is loaded
    def on_load(window):
        signin(window)  # Execute the signin function after the page is loaded

    # Start webview with the on_load event handler
    webview.start(on_load, view)

create_webview()
