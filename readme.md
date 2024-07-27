# Gemini Pro Q/A Project

![Project Banner](image.png)

## Overview

The Gemini Pro Q/A Project is a web application built with Streamlit and Google Generative AI. It allows users to interact with a chatbot powered by the Gemini Pro model, which generates responses based on user questions. The application maintains a history of interactions and displays it in a sidebar for easy reference.

## Features

- **Chat Interface:** Users can ask questions and receive responses from the Gemini Pro model.
- **History Tracking:** Keeps a record of all interactions, which is displayed in the sidebar.
- **Streamlit Integration:** A user-friendly web interface built using Streamlit.

## Prerequisites

Before you can run the application, you need to have the following installed:

- Python 3.7 or higher
- Streamlit
- Google Generative AI Client Library
- `python-dotenv` for environment variable management

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/gemini-pro-qa.git
   cd gemini-pro-qa

2. **Create a virtual environment and activate it:**

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages:**

pip install -r requirements.txt

4. **Set up environment variables:**

Create a .env file in the root of your project directory and add your Google API key:
*GOOGLE_API_KEY=your_google_api_key*

## Contributing

If you'd like to contribute to this project, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them.
- Push your changes to your forked repository.
- Create a pull request describing your changes.

