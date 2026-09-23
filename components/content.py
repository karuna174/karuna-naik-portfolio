"""All portfolio copy lives here so the UI code stays clean."""

PROFILE = {
    "name": "Karuna M Naik",
    "role": "Software Engineer · Python & Full-Stack",
    "headline": "I build Python software from the database query to the button a user clicks.",
    "lead": (
        "Computer Science graduate (2026) with hands-on internship experience shipping "
        "front-end features, writing MySQL queries and fixing real application bugs. "
        "I also train machine learning models when the problem calls for it."
    ),
    "status": "Open to Software Developer roles",
    "location": "Bengaluru, India",
    "email": "karunamnaik59@gmail.com",
    "linkedin": "https://www.linkedin.com/in/karunamnaik",
    "github": "https://github.com/karuna174",
}

STATS = [
    ("8.45", "CGPA out of 10"),
    ("90%", "crop model accuracy"),
    ("10+", "production bugs fixed"),
    ("1,500+", "records preprocessed"),
]

ABOUT = [
    "I care about software that is understandable end to end. During my internship at "
    "Dhee Coding Lab I worked across the stack: building interface components, querying "
    "MySQL, and tracking down defects in a live web application.",
    "Outside of work I like understanding how tools actually function. I wrote a Pascal-style "
    "interpreter from scratch to learn how languages run, and built a classifier that "
    "recommends crops from soil chemistry.",
    "I'm looking for a Python or Software Developer role on a team that values clean code "
    "and steady, practical progress.",
]

STRENGTHS = [
    ("Full-stack range", "HTML, CSS and JavaScript on the front, Python with MySQL behind it."),
    ("Solid fundamentals", "Data structures, algorithms and object-oriented design."),
    ("Debugging mindset", "Comfortable reading unfamiliar code and isolating root causes."),
]

PROJECTS = [
    {
        "title": "Soil-Based Crop Recommendation System",
        "kind": "Machine learning · Classification",
        "summary": (
            "A classifier that suggests the most suitable crop from soil nutrients, pH and "
            "climate readings, so the choice rests on data rather than guesswork."
        ),
        "flow": ["Clean", "Engineer features", "Train", "Compare", "Select"],
        "points": [
            "Reached 90% accuracy after comparing Random Forest and Decision Tree models.",
            "Cleaned a 1,500+ record dataset and handled missing values with Pandas and NumPy.",
            "Built a repeatable pipeline from raw data to model evaluation.",
        ],
        "tags": ["Python", "Scikit-learn", "Pandas", "NumPy"],
        "metric": ("90%", "accuracy"),
    },
    {
        "title": "Pascal-Style Interpreter in Python",
        "kind": "Systems · Language design",
        "summary": (
            "An interpreter written from first principles to see exactly how source code "
            "becomes running behaviour."
        ),
        "flow": ["Lexer", "Parser", "Interpreter"],
        "points": [
            "Implemented tokenisation, syntax parsing and expression evaluation.",
            "Supports variable assignment and execution of Pascal-like statements.",
            "Structured each stage as its own class to keep responsibilities separate.",
        ],
        "tags": ["Python", "OOP", "Parsing", "Data structures"],
        "metric": ("3", "core stages"),
    },
]

EXPERIENCE = {
    "role": "Python Full-Stack Intern",
    "company": "Dhee Coding Lab",
    "place": "Bengaluru",
    "period": "Mar 2026 – Present",
    "points": [
        "Built front-end components in HTML, CSS and JavaScript for four features of a live web application, making the interface more consistent.",
        "Wrote MySQL queries for data retrieval and manipulation that supported backend workflows.",
        "Diagnosed and fixed 10+ application defects, improving stability across features.",
        "Worked through the full software development life cycle, including production support.",
    ],
    "tags": ["HTML", "CSS", "JavaScript", "MySQL", "Debugging", "SDLC"],
}

SKILLS = [
    ("Languages", ["Python", "JavaScript", "SQL"]),
    ("Web", ["HTML5", "CSS3", "React (basics)", "REST API basics"]),
    ("Data & ML", ["Scikit-learn", "Pandas", "NumPy", "Preprocessing", "Predictive modelling"]),
    ("Database", ["MySQL", "Joins", "Query design"]),
    ("Foundations", ["OOP", "Data structures", "Algorithms", "SDLC"]),
    ("Tooling", ["Git", "GitHub", "Jupyter", "VS Code"]),
]

EDUCATION = [
    ("B.E. Computer Science & Engineering", "East West College of Engineering, Bengaluru", "2022 – 2026", "CGPA 8.45 / 10"),
    ("Pre-University (PCMC)", "St Claret PU College, Bengaluru", "2020 – 2022", "79%"),
    ("SSLC", "Mother Teresa High School, Bengaluru", "2019 – 2020", "92%"),
]

CERTIFICATIONS = [
    "Python Fundamentals · Infosys Springboard",
    "Python for Beginners: Data Structures · Coursera Project Network",
    "Machine Learning & Applications · Skill Development Program",
]
