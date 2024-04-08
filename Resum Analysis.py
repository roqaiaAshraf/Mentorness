import os
import re
import pandas as pd
import streamlit as st
import PyPDF2

# Function to read different types of files
def read_files(uploaded_file, filetype):
    if filetype == 'pdf':
        # Save the uploaded PDF file to a temporary location
        with open("temp_pdf.pdf", "wb") as f:
            f.write(uploaded_file.getvalue())
        # Use PyPDF2 to extract text from the saved PDF file
        text = extract_text_from_pdf("temp_pdf.pdf")
        # Remove the temporary file
        os.remove("temp_pdf.pdf")
        return text
    elif filetype == 'txt':
        # Read text directly from the uploaded TXT file
        return uploaded_file.getvalue().decode("utf-8")
    elif filetype == 'docx':
        # Save the uploaded DOCX file to a temporary location
        with open("temp_docx.docx", "wb") as f:
            f.write(uploaded_file.getvalue())
        # Use docx2txt to extract text from the saved DOCX file
        text = extract_text_from_docx("temp_docx.docx")
        # Remove the temporary file
        os.remove("temp_docx.docx")
        return text
    else:
        raise ValueError("Invalid file type")
def extract_text_from_pdf(file):
    text = ""
    with open(file, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
def extract_text_from_docx(file):
    import docx2txt 
    return docx2txt.process(file)

# Function to extract contact information using regular expressions
def extract_contact_info(text):
    regexEmail = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(.[A-Z|a-z]{2,})+')
    regexName = re.compile(r'[A-Za-z]{2,25}( [A-Za-z]{2,25})?')
    pattern = re.compile(r"(\+\d{1,3})?\s?\d{2,5}[\s.-]?\d{5,10}")
    experience_pattern = r'(?i)\b(?:Experience|Work\s*Experience)\b\s*[:\-—]*\s*(.*?)(?:(?=\b(?:Pandas|NumPy|Matplotlib|Seaborn|Sklearn|Joblib|Pickle|NLP|SQL|Soft\s*Skills|Language|SKILLS|EDUCATION SKILLS|SKILLS SUMMARY)\b)|(?=\bHard\s*Skills\b|\bHard\s*Skil\s*ls\b)|\Z)'
    extract_email = re.search(regexEmail, text).group() if re.search(regexEmail, text) else 'no email'
    extract_name = re.search(regexName, text).group() if re.search(regexName, text) else 'no name'
    extract_phone = re.search(pattern, text).group() if re.search(pattern, text) else 'no phone'
    experience_section_match = re.search(experience_pattern, text, flags=re.DOTALL)
    if experience_section_match and experience_section_match.group(1) is not None:
        experience_section = experience_section_match.group(1).strip()
        print("Experience Section:")
        print(experience_section)
    else:
        print("Experience section not found.")
        experience_section = 'Experience section not found.'

    return extract_name, extract_email, extract_phone, experience_section
# UI
def main():
    st.set_page_config(page_title="Resume Analyzer")
    st.title("Resume Analyzer")
    uploaded_files = st.file_uploader("Upload your resume files", accept_multiple_files=True, type=['pdf', 'docx', 'txt'])
    if uploaded_files:
        contact_info = []
        for uploaded_file in uploaded_files:
            file_type = os.path.splitext(uploaded_file.name)[1][1:].lower()
            text = read_files(uploaded_file, file_type)
            name, email, phone,experience = extract_contact_info(text)
            contact_info.append({'Name': name, 'Email': email, 'Phone': phone,'experience':experience})
        csv_file = 'Contact_information.csv'
        if os.path.exists(csv_file):
            existing_df = pd.read_csv(csv_file)
            df = pd.concat([existing_df, pd.DataFrame(contact_info)], ignore_index=True)
        else:
            df = pd.DataFrame(contact_info)
        df.to_csv(csv_file, index=False)
        st.success("Contact information extracted and saved to Contact_information.csv")
        st.subheader("Contents of Contact_information.csv")
        st.write(df)  # Display the contents of the CSV file
if __name__ == '__main__':
    main()





    