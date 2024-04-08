# Your PDF Chat Bot
Your PDF Chat Bot is a conversational AI designed to extract information from one or multiple PDF documents and respond to user queries based on the content within them. This project utilizes Streamlit for the user interface, PyPDF2 for PDF parsing, and Google Generative AI for text embeddings and conversational capabilities.

## **Features**
- **PDF Parsing:** Extracts text from uploaded PDF documents.
- **Question Answering:** Provides answers to user questions based on the content of the PDFs.
- **Conversational AI:** Engages in conversational exchanges to provide detailed responses.
- **Streamlit Interface:** User-friendly interface for interacting with the chat bot.

## Usage
1. **Upload PDFs:** Users can upload one or multiple PDF documents containing relevant information.
2. **Ask Questions:** Users can input questions related to the content of the PDFs.
3. **Receive Answers:** The chat bot analyzes the PDF content and responds with relevant answers.

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your Google API key in a `.env` file.
4. Run the application: `streamlit run your_pdf_chat_bot.py`

## Dependencies
- Streamlit
- PyPDF2
- langchain
- Google Generative AI
- dotenv

## Contributing
Contributions welcome! Open issues or PRs for improvements.
