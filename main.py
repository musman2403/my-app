# Import Flask to create a web application
from flask import Flask

# Create the Flask app instance
app = Flask(__name__)

# Define the home route - what shows when you visit the site
@app.route('/')
def home():
    return "Hello, World! My app is deployed!"

# Run the app
if __name__ == '__main__':
    app.run()