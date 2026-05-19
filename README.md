# Task-Manager
## Task Manager web application that allows users to create, organize, track, and complete personal tasks through a browser-based interface. It maps cleanly onto core web development concepts, including routing, form handling, and persistent data storage.

## Description

This project is a browser-based Task Manager application built with Flask and SQLAlchemy. It allows users to create, organize, track, and complete personal tasks through a clean web interface. The project was chosen because it maps directly onto core web development concepts such as routing, form handling, and data storage.

## Overview

The purpose of this application is to give users a simple, intuitive way to manage their personal task lists from a browser. Tasks can be added, marked complete, deleted, and filtered by status—making it easy to stay organized without switching between tools.

## Key Features Include

- Add new tasks with a title and optional details
- Mark tasks as complete or incomplete
- Delete tasks individually
- Filter tasks by status (all, active, completed)
- Date-based task filtering with dynamic query logic
- Persistent data storage via SQLAlchemy ORM

## Prerequisites

#### Before running this project, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Basic understanding of Python and command-line usage
- Flask
- Flask-SQLAlchemy

## Installation Instructions

1. Clone or download the project files to your local machine.

```
git clone https://github.com/emanual3murry-coder/Task-Manager-App.git
cd Task-Manager-App
```

2. Create a virtual environment

```
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Install the required dependencies using pip:

```
pip install flask
pip install flask-sqlalchemy
```

## How to Run the Program

1. From the root directory, run the Flask application:

```
flask run
```

2. The application will be available in your browser at:

```
http://localhost:5000
```

## Usage Instructions

1. Upon launching the application, you will see your current task list.
2. Enter a task in the input field and click **Add Task** to create a new item.
3. Click the **Complete** button next to any task to mark it as done.
4. Use the **filter options** to view all tasks, only active tasks, or only completed tasks.
5. Click **Delete** to permanently remove a task from the list.

***This project was built as a learning exercise in Flask routing, form handling, and database modeling. It reflects a real-world understanding of how web applications manage and persist user data.***

## License

This project is not licensed and is intended for educational purposes only.

## Acknowledgements

- Flask for the web application framework
- SQLAlchemy for the database ORM
- Flask documentation and quickstart guide for foundational reference
