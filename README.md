# Forum Web App

This is a simple web app that allows users to post and view messages on a public forum. It uses the Flask web framework and SQLite database to store the messages.

## Prerequisites

Before running this app, you need to have the following installed:

- Python 3
- Flask
- SQLite

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory in a terminal window.
3. Run the following command to install the dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Start the Flask development server by running the following command:

```
python app.py
```

2. Open a web browser and navigate to the URL displayed in the terminal window (usually http://localhost:5000).
3. Use the web interface to post and view messages on the forum.

## Deployment

To deploy this app to a production server, you can follow these steps:

1. Set up a virtual environment and install the dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Create a WSGI entry point file, for example `wsgi.py`, with the following contents:

```python
from app import create_app

app = create_app()
```

3. Install a production web server, such as Gunicorn or uWSGI, and configure it to serve the WSGI app. For example, to use Gunicorn with 4 worker processes, run the following command:

```
gunicorn -w 4 wsgi:app
```

or

```
gunicorn --bind 0.0.0.0:8000 -w 4 --timeout 36000 wsgi:app
```

4. Set up a production database, such as PostgreSQL or MySQL, and configure the app to use it instead of SQLite.

# Credits

This app was created by Leonardo.
