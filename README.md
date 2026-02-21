# Meeting Scheduler Agent

## Overview
The Meeting Scheduler Agent is an intelligent scheduling system built with Streamlit. It processes calendar data and user preferences to generate optimized meeting time suggestions while minimizing scheduling conflicts and latency.

## Features
- Calendar availability analysis
- Preference-based time slot optimization
- Conflict detection
- Timezone-aware scheduling
- Ranked meeting slot suggestions
- Interactive web interface built with Streamlit

## Tech Stack
- Python
- Streamlit
- Optimization / Scheduling Algorithms
- (Optional) LLM API integration
- (Optional) Database integration

## Installation

Clone the repository:

Create a virtual environment:

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Install dependencies:

pip install -r requirements.txt

## Environment Variables

Create a `.env` file if required:

API_KEY=your_api_key
DATABASE_URL=your_database_url

## Running the Application

streamlit run app.py
