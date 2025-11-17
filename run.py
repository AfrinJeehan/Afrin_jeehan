from flask import Flask, render_template, request, jsonify, send_from_directory, abort
import os
from datetime import datetime

app = Flask(__name__, static_folder='static')

# Project data
projects = [
    {
        "title": "AI-Powered Python Debugging Education Platform",
        "description": "A sophisticated AI-powered platform revolutionizing Python education through personalized debugging assistance.",
        "technologies": ["Python", "PyTorch", "Hugging Face", "PEFT", "LIME", "SHAP"],
        "category": "AI/ML",
        "overview": """An innovative educational platform leveraging artificial intelligence to provide personalized Python debugging assistance. This project combines fine-tuned language models with explainable AI techniques to help students understand and resolve code errors effectively.""",
        "objectives": [
            "Develop an AI model capable of understanding Python debugging contexts",
            "Implement personalized feedback mechanisms for individual learning styles",
            "Create explainable AI systems using LIME and SHAP for transparency",
            "Build a scalable platform supporting concurrent user sessions"
        ],
        "outcomes": [
            "Successfully fine-tuned LLM achieving 87% accuracy in error detection",
            "Reduced average debugging time by 45% compared to traditional methods",
            "Generated interpretable explanations for AI-suggested fixes using XAI",
            "Platform deployed supporting 100+ concurrent users with 99.2% uptime"
        ],
        "features": [
            "Real-time code analysis and error detection",
            "Personalized debugging suggestions based on user history",
            "Explainable AI recommendations with LIME/SHAP visualizations",
            "Interactive learning modules with step-by-step guidance",
            "Progress tracking and performance analytics dashboard"
        ]
    },
    {
        "title": "Share Plate - Surplus Food Management System",
        "description": "An innovative web-based platform designed to bridge the gap between surplus food availability and community need, reducing food waste while addressing food insecurity through efficient redistribution.",
        "technologies": ["React.js", "PHP", "MySQL", "JavaScript", "REST API", "Bootstrap", "Google Maps API"],
        "category": "Web Development",
        "overview": """Share Plate is a comprehensive food surplus management system that connects restaurants, catering services, events, and households with surplus food to individuals and organizations in need. The platform facilitates real-time food donation coordination, tracking, and distribution, contributing to United Nations Sustainable Development Goal 12 (Responsible Consumption and Production) by minimizing food waste and maximizing community benefit.""",
        "objectives": [
            "Create a user-friendly platform to connect food donors with recipients efficiently",
            "Implement real-time tracking and notification systems for surplus food availability",
            "Develop secure authentication and role-based access control for multiple user types",
            "Build a scalable database architecture to manage donations, pickups, and user interactions",
            "Integrate geolocation services for proximity-based matching of donors and recipients",
            "Establish analytics and reporting systems to measure environmental and social impact"
        ],
        "outcomes": [
            "Successfully facilitated over 500+ food donations during pilot phase",
            "Reduced food waste by approximately 2,500 kg within first 3 months of operation",
            "Achieved 92% user satisfaction rate among donors and recipients",
            "Platform response time under 2 seconds for critical operations",
            "Established partnerships with 25+ restaurants and 15+ community organizations",
            "Generated measurable impact reports showing CO2 emissions reduction equivalent to 6,000 kg"
        ],
        "features": [
            "Multi-tier User Authentication: Separate portals for donors (restaurants, events, households) and recipients (individuals, NGOs, community centers)",
            "Real-time Availability Dashboard: Live updates on available surplus food with photos, quantity, and expiry information",
            "Smart Matching Algorithm: Location-based matching system connecting nearest donors with recipients",
            "Donation Management System: Complete lifecycle tracking from listing to pickup confirmation",
            "Interactive Map Integration: Google Maps API integration for route optimization and location services",
            "Notification System: Email and in-app notifications for new donations, pickup reminders, and status updates",
            "Rating and Review System: Trust-building mechanism allowing users to rate transactions",
            "Impact Analytics Dashboard: Visual reports showing food saved, waste reduced, and community impact metrics",
            "Inventory Management: Donors can manage multiple listings with expiry tracking and auto-archiving",
            "Search and Filter Options: Advanced filtering by food type, dietary preferences, distance, and availability",
            "Mobile Responsive Design: Fully optimized for smartphones and tablets",
            "Admin Control Panel: Comprehensive management tools for platform oversight and user verification"
        ],
        "technical_architecture": {
            "frontend": "React.js with Bootstrap for responsive UI, Redux for state management",
            "backend": "PHP with MVC architecture, RESTful API endpoints",
            "database": "MySQL with normalized schema, indexed queries for performance",
            "apis": "Google Maps API for geolocation, Email service integration",
            "security": "JWT authentication, password hashing, SQL injection prevention, XSS protection"
        },
        "impact": {
            "environmental": "Significant reduction in landfill waste and greenhouse gas emissions from decomposing food",
            "social": "Improved food security for vulnerable populations and strengthened community connections",
            "economic": "Cost savings for businesses through tax deductions and reduced waste disposal fees"
        },
        "future_enhancements": [
            "Mobile application development for iOS and Android platforms",
            "AI-powered demand prediction based on historical donation patterns",
            "Blockchain integration for transparent donation tracking and impact verification",
            "Gamification features to encourage regular participation and community engagement",
            "Multi-language support for diverse communities",
            "Integration with existing food bank management systems"
        ]
    },
    {
        "title": "OSAC Connect - Vehicle Management",
        "description": "Advanced vehicle management system with real-time tracking and automated dispatching.",
        "technologies": ["React.js", "Django REST", "MySQL", "Google Maps API"],
        "category": "Full Stack",
        "overview": """A comprehensive vehicle fleet management solution designed for organizational efficiency, featuring real-time GPS tracking, automated dispatching, and maintenance scheduling.""",
        "objectives": [
            "Develop centralized vehicle tracking and management system",
            "Implement automated dispatching algorithms for optimal resource allocation",
            "Create maintenance scheduling and alerts system",
            "Build driver management and performance monitoring modules"
        ],
        "outcomes": [
            "Reduced vehicle idle time by 38% through optimized dispatching",
            "Improved maintenance compliance to 98% with automated reminders",
            "Decreased fuel costs by 22% through route optimization",
            "Enhanced driver accountability with comprehensive activity logs"
        ],
        "features": [
            "Real-time GPS tracking with geofencing capabilities",
            "Automated dispatch system with route optimization",
            "Maintenance scheduling and service history tracking",
            "Driver assignment and performance analytics",
            "Fuel consumption monitoring and reporting",
            "Trip history and expense management"
        ]
    }
]

# Content/Writings data organized by category
writings = {
    "articles": [
        {
            "id": "art-1",
            "title": "The Future of AI in Education: Personalized Learning at Scale",
            "excerpt": "Exploring how artificial intelligence is transforming education through adaptive learning systems and personalized feedback mechanisms.",
            "content": """Artificial Intelligence is revolutionizing education in ways we never imagined. From personalized learning paths to instant feedback systems, AI is making education more accessible and effective. In my research on AI-powered debugging education, I've witnessed firsthand how machine learning can adapt to individual learning styles. The key is not replacing human educators but augmenting their capabilities with intelligent systems that can provide 24/7 support and personalized guidance.""",
            "date": "2025-11-10",
            "read_time": "5 min",
            "tags": ["AI", "Education", "Technology"]
        },
        {
            "id": "art-2",
            "title": "Business Intelligence: Turning Data into Strategic Decisions",
            "excerpt": "How organizations can leverage BI tools to gain competitive advantages and make data-driven decisions in today's fast-paced market.",
            "content": """Business Intelligence is no longer a luxury—it's a necessity. Modern organizations are drowning in data but starving for insights. Through proper BI implementation using tools like Power BI and statistical analysis, businesses can uncover patterns, predict trends, and make informed decisions. My journey in business analytics has taught me that the real power lies not in collecting data, but in asking the right questions.""",
            "date": "2025-11-08",
            "read_time": "7 min",
            "tags": ["Business Intelligence", "Analytics", "Strategy"]
        },
        {
            "id": "art-3",
            "title": "The Intersection of Computer Science and Business Management",
            "excerpt": "Why pursuing dual degrees in CS and Business creates unique opportunities in today's tech-driven business world.",
            "content": """Combining Computer Science with Business Management opens doors to unique opportunities. Technical skills allow you to build solutions, while business acumen helps you understand market needs and create value. This intersection is where innovation thrives—understanding both the 'how' and the 'why' behind technology solutions.""",
            "date": "2025-11-05",
            "read_time": "6 min",
            "tags": ["Career", "Education", "Business"]
        }
    ],
    "poems": [
        {
            "id": "poem-1",
            "title": "Digital Dreams",
            "excerpt": "A reflection on the beauty of code and the poetry in algorithms.",
            "content": """Lines of code, like verses flow,\nIn Python's grace, ideas grow.\nAlgorithms dance, patterns gleam,\nBuilding tomorrow's digital dream.\n\nData whispers tales untold,\nIn neural nets, futures unfold.\nFrom zero, one, worlds we create,\nWhere innovation meets its fate.\n\nDebug the heart, refine the mind,\nIn every error, lessons find.\nFor code is art, and art is code,\nOn this eternal learning road.""",
            "date": "2025-11-12",
            "read_time": "2 min",
            "tags": ["Poetry", "Technology", "Creativity"]
        },
        {
            "id": "poem-2",
            "title": "The Learner's Journey",
            "excerpt": "Celebrating the continuous pursuit of knowledge and growth.",
            "content": """Each day a page, each moment ink,\nIn books of life, we pause and think.\nQuestions rise like morning sun,\nKnowledge sought, never done.\n\nFrom classroom walls to real-world tests,\nWe grow through failures, find our bests.\nEvery challenge, every fall,\nTeaches us to stand more tall.\n\nSo let us learn, forever more,\nOpen every knowledge door.\nFor wisdom comes not from one place,\nBut from life's continuous embrace.""",
            "date": "2025-11-09",
            "read_time": "2 min",
            "tags": ["Poetry", "Education", "Inspiration"]
        }
    ],
    "essays": [
        {
            "id": "essay-1",
            "title": "Why Explainable AI Matters: Building Trust in Intelligent Systems",
            "excerpt": "Deep dive into the importance of transparency in AI systems and how XAI techniques like LIME and SHAP are changing the game.",
            "content": """As AI systems become more prevalent in critical decision-making processes, the need for explainability has never been greater. Black-box models, while powerful, can erode trust and raise ethical concerns.\n\nIn my research work on AI-powered Python debugging, implementing Explainable AI (XAI) techniques like LIME and SHAP transformed user engagement. Students could see why the AI suggested certain fixes, which not only built trust but enhanced learning outcomes.\n\nThe future of AI isn't just about accuracy—it's about transparency, accountability, and building systems that humans can understand and trust. This is especially crucial in education, healthcare, and finance where decisions have real-world consequences.""",
            "date": "2025-11-11",
            "read_time": "8 min",
            "tags": ["AI", "Ethics", "Research"]
        },
        {
            "id": "essay-2",
            "title": "Sustainable Technology: Building Solutions for Tomorrow",
            "excerpt": "Examining how technology can address global challenges while minimizing environmental impact.",
            "content": """Technology has the power to solve humanity's greatest challenges, but it must be wielded responsibly. As a student focused on creating meaningful innovations, I believe sustainability should be at the core of every technological solution.\n\nFrom reducing food waste through platforms like Share Plate to optimizing resource usage through intelligent systems, technology can be a force for good. But we must ask: Is our solution energy-efficient? Does it create more problems than it solves? How does it impact communities?\n\nSustainable technology isn't just about green energy—it's about creating holistic solutions that benefit society, economy, and environment simultaneously.""",
            "date": "2025-11-06",
            "read_time": "10 min",
            "tags": ["Sustainability", "Technology", "Social Impact"]
        }
    ],
    "tips": [
        {
            "id": "tip-1",
            "title": "5 Tips for Effective Machine Learning Model Training",
            "excerpt": "Practical advice for improving your ML model performance and avoiding common pitfalls.",
            "content": """**1. Start with Data Quality**: Garbage in, garbage out. Clean your data thoroughly before training.\n\n**2. Use Cross-Validation**: Don't rely on a single train-test split. K-fold cross-validation gives you better performance estimates.\n\n**3. Monitor for Overfitting**: If your training accuracy is 99% but validation is 70%, you're overfitting. Use regularization techniques.\n\n**4. Experiment with Learning Rates**: The learning rate can make or break your model. Use learning rate schedulers for better convergence.\n\n**5. Track Your Experiments**: Use tools like MLflow to log parameters, metrics, and artifacts. You'll thank yourself later when trying to reproduce results.""",
            "date": "2025-11-09",
            "read_time": "4 min",
            "tags": ["Tips", "Machine Learning", "Tutorial"]
        },
        {
            "id": "tip-2",
            "title": "Time Management for Student Developers and Researchers",
            "excerpt": "How to balance coursework, projects, research, and personal life effectively.",
            "content": """**1. Use Time Blocking**: Dedicate specific hours to specific tasks. No multitasking during these blocks.\n\n**2. Prioritize with Impact Matrix**: Urgent AND Important gets done first. Important but not urgent gets scheduled.\n\n**3. Learn to Say No**: Not every opportunity is right for you right now. Focus on alignment with your goals.\n\n**4. Batch Similar Tasks**: Code all at once, write all at once, read papers all at once. Context switching kills productivity.\n\n**5. Rest is Productive**: Your brain needs downtime. Schedule breaks and actually take them.""",
            "date": "2025-11-07",
            "read_time": "5 min",
            "tags": ["Tips", "Productivity", "Student Life"]
        },
        {
            "id": "tip-3",
            "title": "Getting Started with Business Intelligence Tools",
            "excerpt": "A beginner's guide to Power BI, data visualization, and analytics.",
            "content": """**1. Understand Your Data First**: Before jumping into Power BI, explore your data in Excel or Python. Know what you're working with.\n\n**2. Start Simple**: Don't try to build complex dashboards on day one. Start with basic charts and add complexity gradually.\n\n**3. Focus on Storytelling**: Every dashboard should tell a story. What insights do you want viewers to take away?\n\n**4. Use DAX Wisely**: Data Analysis Expressions are powerful but can be complex. Learn the basics well before advanced techniques.\n\n**5. Optimize Performance**: Large datasets slow down dashboards. Use aggregations and filters strategically.""",
            "date": "2025-11-04",
            "read_time": "6 min",
            "tags": ["Tips", "Business Intelligence", "Tutorial"]
        }
    ],
    "creative-thinking": [
        {
            "id": "creative-1",
            "title": "From Problem to Solution: A Creative Framework",
            "excerpt": "How to approach problems creatively and generate innovative solutions.",
            "content": """Creative problem-solving isn't magic—it's a process. Here's my framework:\n\n**1. Reframe the Problem**: Don't accept the problem as stated. Ask 'why' five times to get to the root cause.\n\n**2. Gather Diverse Inputs**: Read outside your field. Talk to people with different backgrounds. Inspiration comes from unexpected places.\n\n**3. Generate Abundantly**: Quantity before quality. List 20 solutions, no matter how crazy. You can filter later.\n\n**4. Combine Ideas**: The best solutions often merge multiple concepts. Mix and match your ideas.\n\n**5. Prototype Quickly**: Build a minimum viable version. Learn from failure fast.\n\nWhen I developed the Share Plate platform, we reframed 'food waste' as 'resource optimization,' which opened up entirely new solution paths.""",
            "date": "2025-11-10",
            "read_time": "7 min",
            "tags": ["Creative Thinking", "Innovation", "Problem Solving"]
        },
        {
            "id": "creative-2",
            "title": "The Art of Asking Better Questions",
            "excerpt": "Why question quality determines solution quality—and how to improve yours.",
            "content": """The quality of your solutions depends on the quality of your questions. Here's how to ask better ones:\n\n**Instead of**: 'How can I make this faster?'\n**Ask**: 'What's the real bottleneck here? Is speed even the right metric?'\n\n**Instead of**: 'What technology should I use?'\n**Ask**: 'What problem am I actually solving? Who benefits? What constraints matter most?'\n\n**Instead of**: 'How do I fix this bug?'\n**Ask**: 'Why did this bug occur? What systemic issue does it reveal?'\n\nGood questions open possibilities. Great questions challenge assumptions. Start questioning your questions.""",
            "date": "2025-11-03",
            "read_time": "5 min",
            "tags": ["Creative Thinking", "Critical Thinking", "Strategy"]
        }
    ],
    "tech-news": [
        {
            "id": "tech-1",
            "title": "The Rise of Small Language Models: Efficiency Meets Performance",
            "excerpt": "Why smaller, specialized AI models are becoming more popular than massive general-purpose ones.",
            "content": """The AI community is experiencing a fascinating shift. While companies race to build ever-larger language models, a counter-movement toward smaller, more efficient models is gaining momentum.\n\nSmall Language Models (SLMs) like Phi-2, Mistral 7B, and specialized domain models are proving that bigger isn't always better. These models:\n\n• Run on consumer hardware\n• Fine-tune faster with less data\n• Produce less carbon emissions\n• Often outperform larger models on specific tasks\n\nIn my debugging education research, using a fine-tuned smaller model (CodeT5+) with PEFT techniques achieved better results than prompting GPT-4, at a fraction of the cost and latency.\n\nThe future might not be one massive model to rule them all, but an ecosystem of specialized, efficient models working together.""",
            "date": "2025-11-12",
            "read_time": "6 min",
            "tags": ["Tech News", "AI", "Trends"]
        },
        {
            "id": "tech-2",
            "title": "Reinforcement Learning: Beyond Games and Into Real World",
            "excerpt": "How RL is moving from AlphaGo to practical applications in robotics, education, and business.",
            "content": """Reinforcement Learning burst into public consciousness with AlphaGo defeating world champions. But the real revolution is happening now, in practical applications:\n\n**Education**: Adaptive learning systems that adjust difficulty and content based on student performance (like my Python debugging platform's adaptive learning policy).\n\n**Robotics**: Warehouse robots learning optimal paths and handling strategies through trial and error.\n\n**Business**: Dynamic pricing, inventory management, and resource allocation that learns from market feedback.\n\nThe shift from simulation to reality requires solving challenges like sample efficiency, safety constraints, and handling partial observability. But the potential is enormous—systems that improve themselves through experience.""",
            "date": "2025-11-08",
            "read_time": "7 min",
            "tags": ["Tech News", "AI", "Research"]
        },
        {
            "id": "tech-3",
            "title": "The Developer Experience Revolution: AI-Powered Coding Tools",
            "excerpt": "How GitHub Copilot, Cursor, and other AI assistants are transforming software development.",
            "content": """The way we write code is changing fundamentally. AI-powered coding assistants are now mainstream tools, not experimental features.\n\n**The Good**: Faster prototyping, better documentation, learning from examples, reducing boilerplate code.\n\n**The Challenge**: Over-reliance on generated code, security concerns, understanding what the AI produces.\n\n**My Take**: These tools are incredible for productivity but dangerous for learning. As students, we must use them wisely—let them handle repetitive tasks while we focus on understanding core concepts and architecture.\n\nThe best developers of tomorrow won't be those who can write the most code, but those who can design systems, ask the right questions, and critically evaluate AI-generated solutions.""",
            "date": "2025-11-05",
            "read_time": "5 min",
            "tags": ["Tech News", "Development", "AI"]
        }
    ]
}

# Category metadata
writing_categories = {
    "articles": {
        "name": "Articles",
        "icon": "fa-newspaper",
        "description": "In-depth explorations of technology, education, and business topics",
        "color": "blue"
    },
    "poems": {
        "name": "Poems",
        "icon": "fa-feather",
        "description": "Creative expressions blending technology and human experience",
        "color": "purple"
    },
    "essays": {
        "name": "Essays",
        "icon": "fa-book",
        "description": "Thoughtful analysis on AI ethics, sustainability, and innovation",
        "color": "indigo"
    },
    "tips": {
        "name": "Tips & Tutorials",
        "icon": "fa-lightbulb",
        "description": "Practical advice for developers, students, and tech enthusiasts",
        "color": "green"
    },
    "creative-thinking": {
        "name": "Creative Thinking",
        "icon": "fa-brain",
        "description": "Frameworks and insights for innovative problem-solving",
        "color": "pink"
    },
    "tech-news": {
        "name": "Tech Insights",
        "icon": "fa-rocket",
        "description": "Analysis of emerging trends in AI, development, and technology",
        "color": "orange"
    }
}

@app.route("/")
def index():
    # Get featured writings (latest from each category)
    featured_writings = []
    for category_key, items in writings.items():
        if items:
            latest = items[0].copy()
            latest['category_key'] = category_key
            latest['category_name'] = writing_categories[category_key]['name']
            latest['color'] = writing_categories[category_key]['color']
            featured_writings.append(latest)
    
    return render_template("index.html", projects=projects, featured_writings=featured_writings)


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


@app.route('/writings')
def writings_page():
    # Main writings page with all categories
    return render_template('writings.html', 
                         writing_categories=writing_categories,
                         writings=writings)


@app.route('/writings/<category>')
def writings_category(category):
    # Category-specific listing
    if category not in writing_categories:
        abort(404)
    
    items = writings.get(category, [])
    category_info = writing_categories[category]
    
    return render_template('writings_category.html',
                         category=category,
                         category_info=category_info,
                         items=items)


@app.route('/writings/<category>/<writing_id>')
def writing_detail(category, writing_id):
    # Individual writing detail
    if category not in writing_categories:
        abort(404)
    
    items = writings.get(category, [])
    writing = next((w for w in items if w['id'] == writing_id), None)
    
    if not writing:
        abort(404)
    
    category_info = writing_categories[category]
    related_writings = items  # All writings in the same category
    
    return render_template('writing_detail.html',
                         writing=writing,
                         category=category,
                         category_info=category_info,
                         related_writings=related_writings)

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
