import os
import openai
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_tasks(project_structure):
    """
    Generate tasks based on the project structure using OpenAI API.
    """
    try:
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=f"Generate tasks for the following project structure:\n{project_structure}",
            max_tokens=150
        )
        tasks = response.choices[0].text.strip()
        return tasks
    except Exception as e:
        logger.error(f"Error generating tasks: {e}")
        return None

if __name__ == "__main__":
    project_structure = """
    python-mcp-server/
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    ├── server/
    │   ├── __init__.py
    │   ├── config.py
    │   ├── database/
    │   │   ├── __init__.py
    │   │   ├── db.py
    │   │   └── models.py
    │   ├── main.py
    │   ├── static/
    │   │   ├── css/
    │   │   │   └── styles.css
    │   │   └── js/
    │   │       └── script.js
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── home.html
    │   │   └── login.html
    │   └── utils/
    │       ├── __init__.py
    │       ├── auth.py
    │       └── helpers.py
    └── tests/
        ├── __init__.py
        ├── test_auth.py
        └── test_db.py
    """
    tasks = generate_tasks(project_structure)
    if tasks:
        print("Generated Tasks:")
        print(tasks)
    else:
        print("Failed to generate tasks.")
