# Groq Request Form with Flask

This project is a simple Flask application that accepts user input from a web form, sends the data to the Groq API, and displays the response. It uses Tailwind CSS for styling and `python-dotenv` for managing environment variables.

## Features

- Accepts JSON input from a web form.
- Sends data to the Groq API and processes the response.
- Uses Tailwind CSS for styling.
- Loads environment variables from a `.env` file.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/darkevo24/groq.git
cd groq

### 2. Create and Activate a Virtual Environment

python -m venv venv
On macOS/Linux:
source venv/bin/activate
On Windows:
venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Set Up Environment Variables

Create a .env file in the root of the project directory and add your Groq API key:
GROQ_API_KEY=your_actual_api_key

### 5. Run the Application

python app.py

### 6. Access the Web Form

Open your web browser and navigate to http://127.0.0.1:5000/.
