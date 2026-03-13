# gold_investment_api

🪙 Gold Investment API – AI Powered Fintech Backend

An AI-powered Fintech backend service that enables users to ask questions about gold investment and purchase digital gold through a simple API.

Built using FastAPI, OpenAI, SQLAlchemy, and SQLite, this system simulates the workflow of fintech platforms like Simplify Money Kuber.AI, combining AI advisory with digital gold transactions.

This project demonstrates modern backend architecture, modular FastAPI design, AI integration, and fintech transaction workflows.

🚀 Features

AI-powered investment assistant for gold-related questions

OpenAI GPT integration for intelligent responses

Automatic fallback mode when API key is not provided

Digital gold purchase simulation

Modular backend architecture using FastAPI best practices

SQLite database for storing purchases

Pydantic validation for API requests and responses

Interactive API documentation with Swagger UI

🏗 System Architecture
User
 │
 ▼
Client / Frontend
 │
 ▼
FastAPI Backend
 │
 ├── AI Advisor (/ask)
 │      │
 │      ├── OpenAI API
 │      └── Fallback AI Mode
 │
 └── Gold Purchase Service (/buy-gold)
        │
        ▼
     SQLite Database
📁 Project Structure
gold-investment-api
│
├── backend
│   │
│   ├── main.py          # FastAPI application and routes
│   ├── database.py      # Database configuration and session
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   │
│   ├── gold.db          # SQLite database
│   ├── purchases.db     # Transaction database
│   │
│   ├── .env.example     # Environment variable template
│   └── requirements.txt
│
└── README.md
⚙️ Tech Stack

Python
FastAPI
OpenAI API
SQLAlchemy
SQLite
Pydantic
Uvicorn
Requests

🔑 API Endpoints
1️⃣ Ask AI About Gold Investment

Endpoint

POST /ask

Example Request

{
  "question": "How to invest in gold?"
}

Example Response

{
  "answer": "Gold is considered a stable investment and helps protect against inflation.",
  "nudge": "You can invest in digital gold using the Simplify Money platform. Would you like to purchase digital gold?"
}

This endpoint:

Uses OpenAI for generating intelligent responses

Suggests digital gold investment through a fintech-style nudge

2️⃣ Buy Digital Gold

Endpoint

POST /buy-gold

Example Request

{
  "user": "Test User",
  "amount": 12000
}

Example Response

{
  "message": "Digital gold purchase successful",
  "gold_grams": 2.0
}

The endpoint calculates gold grams based on the investment amount and stores the purchase in the database.

🗄 Database Schema
Purchases Table
Column	Type	Description
id	Integer	Primary key
user	String	User name
amount	Float	Investment amount
gold_grams	Float	Gold purchased
created_at	Timestamp	Purchase timestamp
🤖 OpenAI Integration

The /ask endpoint integrates with OpenAI GPT to generate intelligent financial responses.

Create a .env file inside the backend folder:

OPENAI_API_KEY=your_openai_api_key_here

If the API key is not provided, the backend automatically runs in Fallback Mode using basic keyword-based responses.

▶️ Running the Application
Clone the Repository
git clone https://github.com/YOUR_USERNAME/gold-investment-api.git
cd gold-investment-api
Install Dependencies
pip install -r requirements.txt
Configure Environment Variables

Create a .env file in the backend directory:

OPENAI_API_KEY=your_openai_api_key_here
Start the Backend Server
uvicorn main:app --reload

Server will start at:

http://127.0.0.1:8000
📘 API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI

http://127.0.0.1:8000/docs

ReDoc

http://127.0.0.1:8000/redoc
🧪 Example Workflow

Step 1 – Ask Investment Advice

POST /ask

User asks a question about gold investment.

The AI responds with an explanation and suggests investing in digital gold.

Step 2 – Purchase Gold

POST /buy-gold

User invests an amount and receives the equivalent gold grams.

The transaction is stored in the database.

📊 Project Highlights

AI + Fintech integration
Production-style backend architecture
FastAPI microservice design
Database modeling using SQLAlchemy
Prompt engineering for financial advisory
Persistent transaction storage

🔮 Future Improvements

Real-time gold price integration

User authentication with JWT

Payment gateway integration

Portfolio tracking system

React frontend dashboard

Docker deployment

Cloud deployment (AWS / GCP)

👨‍💻 Author

Jalagam Dolender

GitHub
https://github.com/Jalagamdolu

LinkedIn
https://www.linkedin.com/in/jalagam-dolender-vel-tech-chennai-1b0a10347/
