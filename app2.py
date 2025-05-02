import streamlit as st 
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

st.set_page_config(page_title = "Langchain: Chat with SQL DB", page_icon = "🦜")
st.title("🦜 Langchain: Chat with SQL DB")

LOCAL_DB = "USE_LOCALDB"
POSTGRESQL = "USE_POSTGRESQL"

radio_opt = ["Use SQL Lite-3 database -> STUDENT.db", "Connect to PostgreSQL database"]
selected_opt = st.sidebar.radio(label = "Choose the db you want to chat with", options = radio_opt)

if radio_opt.index(selected_opt) == 1:
    db_uri = POSTGRESQL
    pg_host = st.sidebar.text_input("PostgreSQL host", value="localhost")
    pg_port = st.sidebar.text_input("PostgreSQL port", value="5432")
    pg_user = st.sidebar.text_input("PostgreSQL user")
    pg_pwd = st.sidebar.text_input("PostgreSQL password", type = "password")
    pg_db = st.sidebar.text_input("PostgreSQL database")
else:
    db_uri = LOCAL_DB

# Enter Groq API key
api_key = st.sidebar.text_input(label ="Enter your GROQ API key", type = "password")

# Error handling
if not db_uri:
    st.info("Please enter the database information")
    
if not api_key:
    st.info("Please enter your Groq-API key")
    
# LLM model
if api_key:
    llm = ChatGroq(groq_api_key=api_key, model_name="llama3-8b-8192", streaming=True)
else:
    st.warning("Please enter your GROQ API key to proceed.")
    st.stop()

@st.cache_resource(ttl = "2h")
def configure_db(db_uri, pg_host = None, pg_port = None, pg_user = None, pg_pwd = None, pg_db = None):
    if db_uri == LOCAL_DB:
        db_filepath = (Path(__file__).parent/"student.db").absolute()
        print(db_filepath)
        creator = lambda: sqlite3.connect(f"file:{db_filepath}?mode=ro", uri=True)
        return SQLDatabase(create_engine("sqlite:///", creator = creator))
    elif db_uri == POSTGRESQL:
        if not (pg_host and pg_port and pg_user and pg_pwd and pg_db):
            st.error("Please provide all the PostgreSQL connection details")
            st.stop()
        # Note: psycopg2 must be installed: pip install psycopg2
        return SQLDatabase(
            create_engine(
                f"postgresql+psycopg2://{pg_user}:{pg_pwd}@{pg_host}:{pg_port}/{pg_db}"
            )
        )
    
if db_uri == POSTGRESQL:
    db = configure_db(db_uri, pg_host, pg_port, pg_user, pg_pwd, pg_db) 
else:
    db = configure_db(db_uri)
        
# Toolkit
toolkit = SQLDatabaseToolkit(db = db, llm = llm)
agent = create_sql_agent(
    llm = llm,
    toolkit = toolkit,
    verbose = True,
    agent_type = AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# To maintain chat history
if "messages" not in st.session_state or st.sidebar.button("Clear message history ->"):
    st.session_state['messages'] = [{"role" : "assistant", "content" : "How can I help you?"}]
    
for i in st.session_state.messages:
    st.chat_message(i["role"]).write(i["content"])
    
user_query = st.chat_input(placeholder = "Ask anything from database..")

if user_query:
    st.session_state.messages.append({"role" : "user", "content" : user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query, callbacks = [streamlit_callback])    
        st.session_state.messages.append({"role" : "assistant", "content" : response})
