

from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

llm = ChatOllama(model="deepseek-r1:7b")

# Update the template based on the type of SQL Database like MySQL, Microsoft SQL Server and so on
template = """Based on the table schema below, write a SQL query that would answer the user's question:
Question: {question}
SQL Query:"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Given an input question, convert it to a SQL query. No pre-amble."),
        ("human", template),
    ]
)

client_response = (
    prompt
    | llm
    | StrOutputParser()
)
# Simply set the LLM we want to use
client_response.invoke({"question": "What team is Klay Thompson on?"})

