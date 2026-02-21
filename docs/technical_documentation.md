# Meeting Scheduler Agent – Technical Documentation

## 1. Introduction

The Meeting Scheduler Agent is an AI-powered scheduling application built using Streamlit. The system allows users to schedule meetings through a conversational chatbot interface. It collects structured meeting information, processes it using AI services, compresses conversation context for efficiency, and stores validated records in a PostgreSQL database.

The system integrates Groq API for conversational intelligence and ScaleDown API for compression optimization.

---

## 2. System Objectives

The primary objectives of this project are:

- Enable conversational meeting scheduling
- Extract structured meeting details from natural language
- Reduce API latency and token usage using compression
- Store meeting data securely in a relational database
- Provide a deployable web-based interface

---

## 3. Technology Stack

**Frontend & Deployment**
- Streamlit

**AI Services**
- Groq API (LLM-powered chatbot)
- ScaleDown API (context compression)

**Database**
- PostgreSQL

**Backend**
- Python

---

## 4. System Architecture

### High-Level Workflow

1. User interacts with chatbot via Streamlit interface.
2. Groq API processes user input and extracts meeting details.
3. ScaleDown API compresses conversation context to optimize token usage.
4. Validated meeting data is stored in PostgreSQL.
5. Confirmation message is returned to the user.

---

## 5. Functional Components

### 5.1 Chatbot Interaction (Groq API)

The chatbot is responsible for:

- Collecting required meeting details:
  - Meeting Name
  - Meeting Date
  - Meeting Time
  - Participant Name
  - Phone Number
- Validating input formats
- Requesting missing information
- Generating structured confirmation responses

The chatbot ensures that all mandatory fields are collected before final submission.

---

### 5.2 Compression Layer (ScaleDown API)

The ScaleDown API is used to:

- Compress conversation history
- Reduce token consumption
- Improve response latency
- Optimize API cost

Compression is applied before sending extended conversation context to the Groq API.

---

### 5.3 Database Layer (PostgreSQL)

All validated meeting records are stored in PostgreSQL.

#### Example Table Structure: `meetings`

| Column Name        | Data Type   | Description |
|--------------------|------------|------------|
| id                 | SERIAL     | Primary key |
| meeting_name       | VARCHAR    | Name of the meeting |
| meeting_date       | DATE       | Scheduled date |
| meeting_time       | TIME       | Scheduled time |
| participant_name   | VARCHAR    | Name of participant |
| phone_number       | VARCHAR    | Contact number |
| created_at         | TIMESTAMP  | Record creation time |

The database ensures persistent and structured storage of meeting information.

---

## 6. Data Validation

The system performs validation checks for:

- Proper date format (YYYY-MM-DD)
- Proper time format (HH:MM)
- Valid phone number structure
- Completion of all required fields before insertion

If any field is missing or invalid, the chatbot prompts the user for correction.

---

## 7. Deployment

The application is deployed using Streamlit.

### Deployment Steps:

1. Push project to GitHub.
2. Connect repository to Streamlit Cloud.
3. Configure environment variables:
   - GROQ_API_KEY
   - SCALEDOWN_API_KEY
   - DATABASE_URL
4. Deploy the application.

The deployed application runs as a web-based chatbot interface.

---

## 8. Security Considerations

- API keys are stored as environment variables.
- No credentials are hardcoded.
- Database access is secured using connection strings.
- Input validation prevents malformed data storage.

---

## 9. Future Enhancements

- Google Calendar integration
- SMS confirmation using phone number
- OTP verification
- Recurring meeting scheduling
- Role-based access control
- Automated reminders

---

## 10. Conclusion

The Meeting Scheduler Agent demonstrates the integration of conversational AI, context compression, database management, and web deployment into a unified scheduling system. The project emphasizes efficiency, structured data handling, and scalable AI integration.
