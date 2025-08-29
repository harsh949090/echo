INSTALL THIS (pip install streamlit transformers torch torchaudio soundfile scipy bark ibm-watsonx-ai)





EchoVerse: AI-Powered Audiobook Creation Tool
Description:
EchoVerse is a generative AI-based application that transforms text into expressive, downloadable audio content. Designed for accessibility and content reusability, the tool empowers users to convert written material into natural-sounding narrations with a customizable tone and voice.

The system uses a two-step AI pipeline:

Tone-Adaptive Text Rewriting: It first rewrites user-provided text to a specific tone (e.g., suspenseful) using a large language model.

High-Quality Voice Narration: It then converts the rewritten, expressive text into an audio file, which can be played back and downloaded.

How to Prepare for Submission
To properly submit your project, you should organize your files and provide clear instructions for anyone who wants to run it. Follow these steps:

Step 1: Finalize Your Files
Make sure your app.py file is complete and saved. Then, you need to create a requirements.txt file. This is essential as it lists all the libraries required for the project.

Open your VS Code terminal.

Make sure your virtual environment is activated.

Run the following command to generate the requirements.txt file:

Bash

pip freeze > requirements.txt
Step 2: Organize Your Project Folder
Your project folder should have a clean and logical structure. It should look like this:

EchoVerse/
├── app.py
├── requirements.txt
└── (other files created during runtime, e.g., audiobook.wav)
Step 3: Write the Project Documentation
Create a file named README.md in your main project folder. This file will be the main documentation for your project and should include the following sections:

Project Title: EchoVerse - An AI-Powered Audiobook Creation Tool

Description: A brief summary of what the project does.

Technologies Used: A list of the key technologies (Python, Streamlit, Hugging Face, PyTorch).

How to Run:

Prerequisites: List the required software (Python 3.10+, VS Code, Git).

Setup: Explain how to create and activate a virtual environment.

Installation: Tell the user to run pip install -r requirements.txt.

Execution: Instruct the user to run the app with streamlit run app.py.

AI Models Used: List and briefly describe the specific models for each task:

Text Rewriting: google/flan-t5-base

Text-to-Speech: suno/bark

Step 4: Demonstrate the Project
To prove that your project works, you should either:

Create a short video of you running the application, showing a live demonstration of it taking text and producing audio.

Take a series of screenshots of the different stages of the application.

Step 5: Package for Submission

Finally, zip the entire EchoVerse folder. The zipped file will contain all your code, documentation, and the requirements.txt file, making it easy for the person reviewing your project to use.
