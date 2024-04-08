# Mentorness Internship Program - AI Intern

Welcome to the main repository for my internship experience with the Mentorness Internship Program as an AI intern! This repository contains two projects that I have worked on during my internship.

## Projects

### Your PDF Chat Bot

Your PDF Chat Bot is a conversational AI designed to extract information from one or multiple PDF documents and respond to user queries based on the content within them. This project utilizes Streamlit for the user interface, PyPDF2 for PDF parsing, and Google Generative AI for text embeddings and conversational capabilities.

#### Features

- **PDF Parsing**: Extracts text from uploaded PDF documents.
- **Question Answering**: Provides answers to user questions based on the content of the PDFs.
- **Conversational AI**: Engages in conversational exchanges to provide detailed responses.
- **Streamlit Interface**: User-friendly interface for interacting with the chat bot.

#### How to Run

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your Google API key in a `.env` file.
4. Run the application: `streamlit run your_pdf_chat_bot.py`

#### Dependencies

- Streamlit
- PyPDF2
- langchain
- Google Generative AI
- dotenv

#### Contributing

Contributions welcome! Open issues or PRs for improvements.

### Resume Analyzer

The Resume Analyzer is a Python script designed to extract contact information and experience sections from resumes uploaded in PDF, DOCX, or TXT formats. The extracted information is then saved to a CSV file named "Contact_information.csv" for further analysis.

#### How it Works

- **File Reading**: Reads various file formats (PDF, DOCX, TXT) using the `read_files()` function, which utilizes different libraries (PyPDF2 for PDF, docx2txt for DOCX, and direct decoding for TXT files).
- **Contact Information Extraction**: Extracts contact information such as name, email, and phone number using regular expressions.
- **User Interface**: Provides a simple user interface using Streamlit.
- **CSV Output**: Saves extracted information to a CSV file named "Contact_information.csv".

#### Usage

1. Upload Resumes: Click the "Upload your resume files" button and select one or multiple resume files in PDF, DOCX, or TXT formats.
2. Analysis: Once files are uploaded, the script automatically extracts contact information and experience sections from each resume.
3. Output: Extracted information is displayed on the Streamlit web interface and saved to "Contact_information.csv".

#### Requirements

- Python 3.x
- PyPDF2
- pandas
- streamlit
- docx2txt (for DOCX files)

#### How to Run

1. Ensure you have Python and required libraries installed.
2. Copy the provided code into a Python script (e.g., `resume_analyzer.py`).
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script using the command `streamlit run resume_analyzer.py`.
5. Upload resumes for analysis using the provided interface.

## Contact Information

For any inquiries or collaboration opportunities, feel free to reach out to me at [Your Email Address].

Thank you for visiting my repository!
