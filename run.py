from flask import Flask, render_template, request, jsonify, send_from_directory, abort
import os

app = Flask(__name__, static_folder='static')

# Project data
projects = [
    {
        "title": "AI-Powered Python Debugging Education Platform",
        "description": "A sophisticated AI-powered platform revolutionizing Python education through personalized debugging assistance.",
        "technologies": ["Python", "PyTorch", "Hugging Face", "PEFT", "LIME", "SHAP"],
        "category": "AI/ML"
    },
    {
        "title": "Share Plate - Surplus Food Management",
        "description": "Platform connecting surplus food donors with recipients to reduce waste.",
        "technologies": ["React.js", "PHP", "MySQL", "JavaScript"],
        "category": "Web Development"
    },
    {
        "title": "OSAC Connect - Vehicle Management",
        "description": "Advanced vehicle management system with real-time tracking and automated dispatching.",
        "technologies": ["React.js", "Django REST", "MySQL", "Google Maps API"],
        "category": "Full Stack"
    }
]

@app.route("/")
def index():
    return render_template("index.html", projects=projects)


@app.route('/projects')
def projects_page():
    # list all projects with brief info
    return render_template('projects.html', projects=projects)


@app.route('/projects/<int:pid>')
def project_detail(pid):
    # show project detail by index
    if pid < 0 or pid >= len(projects):
        abort(404)
    project = projects[pid]
    return render_template('project_detail.html', project=project, pid=pid)


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/api/projects")
def get_projects():
    category = request.args.get('category', default=None)
    if category:
        filtered_projects = [p for p in projects if p['category'] == category]
        return jsonify(filtered_projects)
    return jsonify(projects)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    # Ensure static folder exists
    os.makedirs('static', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    
    app.run(debug=True, port=5000)
