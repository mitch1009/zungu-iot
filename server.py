"""
Main Entry Point for the API
"""
from main.config import app

if __name__ == "__main__":
    app.run(debug=True, port=5400)
