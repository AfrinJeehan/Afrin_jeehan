from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    """Renders the main portfolio page."""
    # Pass data about the developer for dynamic content
    developer_info = {
        'name': 'A.I. Developer',
        'title': 'Computer Science Undergraduate',
        'specialization': 'Artificial Intelligence, Machine Learning, Business Intelligence',
        'tagline': 'Developing intelligent, data-driven systems to enhance decision-making and efficiency.'
    }
    return render_template('index.html', info=developer_info)

# Run the app
if __name__ == '__main__':
    # Use debug=True for development. Change for production.
    app.run(debug=True)