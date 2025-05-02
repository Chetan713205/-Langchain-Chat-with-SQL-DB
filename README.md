# 🦜 Langchain: Chat with SQL DB

## Overview

This application allows users to interact with SQL databases using natural language queries. Powered by LangChain and Groq's LLM, it translates user questions into SQL queries and returns the results in a conversational format. The application supports both SQLite and PostgreSQL databases.

## Features

- **Dual Database Support**: Connect to either a local SQLite database or a remote PostgreSQL database
- **Natural Language Queries**: Ask questions about your data in plain English
- **Interactive Chat Interface**: Maintain conversation history with the AI assistant
- **Real-time Streaming**: See the AI's thought process and query generation in real-time
- **Secure API Key Management**: Safely input your Groq API key through the Streamlit interface

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/langchain-sql-chat.git
   cd langchain-sql-chat
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Launch the application using the command above
2. In the sidebar, choose your database type:
   - SQLite (uses the included `student.db` file)
   - PostgreSQL (requires connection details)
3. Enter your Groq API key in the sidebar
4. Start asking questions about your data in natural language

## Configuration

### SQLite Database
The application comes with a pre-configured SQLite database (`student.db`). No additional setup is required for this option.

### PostgreSQL Database
To connect to a PostgreSQL database, you'll need to provide:
- Host address
- Port number
- Username
- Password
- Database name

## Example Queries

- "How many students are in the database?"
- "Show me the average grades by subject"
- "List all students with grades above 90"
- "Which teacher has the most students?"

## Technical Details

This application uses:
- **Streamlit**: For the web interface
- **LangChain**: For agent creation and database interaction
- **Groq**: LLM provider using the Llama3-8B model
- **SQLAlchemy**: For database connectivity
- **SQLite/PostgreSQL**: Supported database systems

## Limitations

- The quality of responses depends on the Groq LLM model
- Complex queries might require refinement
- Performance may vary based on database size and complexity

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
