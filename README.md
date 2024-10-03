# Socratist: A Socratic AI Teaching Assistant

## Project Overview

Socratist is an interactive web-based application designed to provide teaching assistance through a Socratic approach. By engaging users with guided questions, the platform helps learners explore topics, develop critical thinking skills, and arrive at answers independently.
**The application is created primarily for sorting algorithm related questions.**

## Features

- **Interactive Chat Interface**: Users can engage in a dialogue with the AI assistant, asking questions and receiving guidance.
- **Socratic Method**: The AI employs the Socratic method, prompting users with questions to stimulate critical thinking.
- **Backend Integration**: The backend handles requests, and communicates with the Gemini API for intelligent responses.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **AI Model**: Gemini API for natural language processing
- **Deployment**: Render for hosting the application

## Installation

1. Clone the repository:
   
    git clone repo
    cd socratist

2. Install the required dependencies:
    
    pip install -r requirements.txt

3. Set up environment variables:

    Create a .env file in the root directory and add your API key:
    API_KEY=your_api_key_here

4. Run the application locally:

    add app.run() in run.py file

    python run.py
