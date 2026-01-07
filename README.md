## AI/ML Based Text-to-Text Machine Translation
Nepali & Sinhalese → English


## 📌 Overview
This project is an AI/ML-based text-to-text machine translation system designed to translate Nepali and Sinhalese text into English.
The system first extracts text from images using OCR (Optical Character Recognition) and then translates the extracted text into English using a machine translation service.

The project is developed with a focus on heritage and cultural documents, helping improve multilingual accessibility.

## 🚀 Features

Upload images containing Nepali or Sinhalese text

Extract text using OCR

Translate extracted text into English

REST API–based backend

Simple and responsive frontend interface

## 🛠️ Tech Stack
## Backend

Python

Flask

Tesseract OCR (pytesseract)

Google Cloud Translation API

Pillow (PIL)

## Frontend

HTML

CSS

JavaScript



## 📂 Project Structure
ntro-translation/
│

├── backend/

│   └── app.py


├── frontend/

│   ├── index.html

│   └── multiformat_ingestion.html
│

├── README.md

└── LICENSE


## ⚙️ How the System Works

User uploads an image containing Nepali or Sinhalese text.

The backend performs OCR to extract text from the image.

The extracted text is sent to a machine translation service.

The translated English text is returned as a JSON response.

The frontend displays both original and translated text.

## 🔗 API Endpoint
POST /process-image

Request

Form-data:

file → Image file containing Nepali or Sinhalese text

Response

{
  "originalText": "Extracted Nepali/Sinhalese text",
  "translatedText": "Translated English text"
}

## ▶️ Running the Project Locally
Prerequisites

Python 3.x

Tesseract OCR installed

Google Cloud account (for Translation API)

Installation
pip install flask flask-cors pytesseract pillow google-cloud-translate

Run Backend
python backend/app.py


The backend server will start at:

http://localhost:5000

## 🔑 API & Credentials Setup

This project uses external services that require API credentials.

Google Cloud Translation API

The Translation API requires authentication using a service account credentials file.

For security reasons, API keys and credentials are not included in this repository.

Setup Steps

Create a Google Cloud project.

Enable the Cloud Translation API.

Generate a service account and download the credentials file.

Set the environment variable:

GOOGLE_APPLICATION_CREDENTIALS=credentials.json


Place the credentials file locally (do not commit it to GitHub).

## 🔒 Security Note

Sensitive information such as API keys and credentials has been intentionally excluded from this repository to follow security best practices.

#3 📌 Current Status

Academic / prototype project

Supports Nepali (nep) and Sinhalese (sin)

Designed for learning, experimentation, and cultural applications

## 🎯 Use Cases

Translation of heritage and cultural documents

Multilingual accessibility

Academic and research purposes

## 👨‍💻 Author

Vishal Dhara

GitHub: https://github.com/vishaldhara31
