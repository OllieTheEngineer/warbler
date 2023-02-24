Look over the code in app.py related to authentication.

How is the logged in user being kept track of?
- It is being kept track of under curr_user_key in session
What is Flask’s g object?
- it stands for global and used to store data in a Flask Web App
What is the purpose of add_user_to_g?
- The purpose is to ensure the user is logged in globally within the web application.
What does @app.before_request mean?
- It means that the function will execute before any other requests are made.