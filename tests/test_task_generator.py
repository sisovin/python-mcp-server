import unittest
from server.task_generator import generate_tasks

class TestTaskGenerator(unittest.TestCase):

    def setUp(self):
        self.project_structure = """
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

    def test_generate_tasks(self):
        tasks = generate_tasks(self.project_structure)
        self.assertIsNotNone(tasks)
        self.assertIn("Generate tasks for the following project structure", tasks)

    def test_empty_project_structure(self):
        empty_structure = ""
        tasks = generate_tasks(empty_structure)
        self.assertIsNone(tasks)

    def test_invalid_project_structure(self):
        invalid_structure = "invalid structure"
        tasks = generate_tasks(invalid_structure)
        self.assertIsNone(tasks)

if __name__ == "__main__":
    unittest.main()
