# 🎙️ AWS Text-to-Audio Converter

A serverless cloud application that automatically converts uploaded text files into natural-sounding speech using **Amazon Polly**, **AWS Lambda**, and **Amazon S3**.

---

## 📌 Project Overview

The AWS Text-to-Audio Converter is an event-driven serverless application that converts text files into MP3 audio files. Whenever a user uploads a text file to an Amazon S3 bucket, AWS Lambda is triggered automatically. The Lambda function reads the text, sends it to Amazon Polly for speech synthesis, and stores the generated MP3 file in an output S3 bucket.

This project demonstrates the use of AWS serverless services to build an automated, scalable, and cost-effective text-to-speech solution.

---

## ✨ Features

- 📄 Automatic text-to-speech conversion
- ☁️ Fully serverless architecture
- 🚀 Event-driven processing using S3 triggers
- 🔊 Natural-sounding speech with Amazon Polly
- 💾 Stores generated MP3 files in Amazon S3
- 🔒 Secure access using AWS IAM
- 📊 Monitoring and logging using Amazon CloudWatch

---

## 🛠️ Technologies Used

- Python
- AWS Lambda
- Amazon S3
- Amazon Polly
- AWS IAM
- Amazon CloudWatch
- Boto3 (AWS SDK for Python)

---

## 🏗️ System Architecture

```
                User
                  │
          Upload .txt File
                  │
                  ▼
        Amazon S3 (Input Bucket)
                  │
          S3 Event Trigger
                  │
                  ▼
             AWS Lambda
          (Python Function)
                  │
                  ▼
           Amazon Polly
        (Text-to-Speech)
                  │
                  ▼
      Amazon S3 (Output Bucket)
                  │
                  ▼
      Download Generated MP3
```

---

## ⚙️ Workflow

1. User uploads a `.txt` file to the Amazon S3 input bucket.
2. Amazon S3 triggers the AWS Lambda function.
3. Lambda reads the uploaded text file.
4. The text is sent to Amazon Polly.
5. Amazon Polly converts the text into speech.
6. The generated MP3 file is stored in the Amazon S3 output bucket.
7. The user can download or listen to the generated audio.

---

## ☁️ AWS Services Used

### Amazon S3
- Stores uploaded text files.
- Stores generated MP3 audio files.

### AWS Lambda
- Executes Python code automatically.
- Processes uploaded files without managing servers.

### Amazon Polly
- Converts text into natural-sounding speech.
- Generates MP3 audio output.

### AWS IAM
- Provides secure permissions between AWS services.

### Amazon CloudWatch
- Stores logs and monitors Lambda execution.

---

## 📂 Project Structure

```
aws-text-to-audio-converter/
│
├── README.md
├── LICENSE
│
├── documentation/
│   └── Project_Documentation.pdf
│
├── presentation/
│   └── Project_Presentation.pptx
│
├── lambda-code/
│   └── lambda_function.py
│
├── architecture/
│   └── architecture-diagram.png
│
└── screenshots/
    ├── s3-bucket.png
    ├── lambda.png
    ├── polly-output.png
    └── cloudwatch.png
```

---

## ▶️ How It Works

1. Upload a text file to Amazon S3.
2. AWS Lambda is triggered automatically.
3. Lambda reads the uploaded file.
4. Amazon Polly converts the text into speech.
5. The generated MP3 file is saved in the output S3 bucket.

---

## 📈 Future Enhancements

- Support PDF and DOCX files.
- Support multiple languages and voices.
- Web-based user interface.
- Authentication and user management.
- Audio download history.
- Real-time notifications.

---

## 🎯 Learning Outcomes

Through this project, we learned:

- AWS Serverless Computing
- Event-Driven Architecture
- Amazon Polly Integration
- Amazon S3 Bucket Management
- AWS Lambda Development
- IAM Roles and Permissions
- CloudWatch Monitoring
- Python with Boto3

---

## 👨‍💻 Author

**Girishma Giri**

Developed as part of an academic cloud computing project to demonstrate serverless text-to-speech conversion using AWS services.

---

## ⭐ If you found this project useful, consider giving it a Star!
