from typing import Annotated, TypedDict
import operator
import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.document_loaders import WikipediaLoader
from langchain_core.documents import Document
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper

load_dotenv()

llm = ChatOllama(
    model="llama3.1-tool",
    base_url="http://localhost:11434",
    temperature=0.8,
    max_tokens=1000
)

class State(TypedDict):
    question:  str
    answer: str
    context: Annotated[list, operator.add]

def search_web(state: State):

    tavily_search = TavilySearchResults(max_results=3, api_wrapper=TavilySearchAPIWrapper(tavily_api_key=os.getenv("TAVILY_API_KEY")))
    search_docs = tavily_search.invoke(state["question"])

    # Format answer
    formatted_search_docs = "\n\n---\n\n".join(
        [
            f"""<Document href="{doc["url"]}">\n{doc["content"]}\n</Document>"""
            for doc in search_docs
        ]
    )

    return {"context":[formatted_search_docs]}

def search_wikipedia(state:State):

    search_docs = WikipediaLoader(query=state["question"], load_max_docs=2).load()

    # Format answer
    formatted_search_docs = "\n\n---\n\n".join(
        [
            f"""<Document source="{doc.metadata["source"]}" page="{doc.metadata.get("page","")}">\n{doc.page_content}\n</Document>"""
            for doc in search_docs
        ]
    )

    return {"context": [formatted_search_docs]}

def generate_answer(state: State):

    context = state["context"]
    question = state["question"]

    system_prompt = """Given the following context:{context}"""
    system_instruction = system_prompt.format(question=question, context=context)

    answer = llm.invoke([SystemMessage(content=system_instruction)] + [HumanMessage(content=f"Answer the question: {state["question"]}")])

    return {"answer": answer}


builder = StateGraph(State)

builder.add_node("search_web", search_web)
builder.add_node("search_wikipedia", search_wikipedia)
builder.add_node("generate_answer", generate_answer)

builder.add_edge(START, "search_web")
builder.add_edge(START, "search_wikipedia")
builder.add_edge(["search_web","search_wikipedia"],"generate_answer")
builder.add_edge("generate_answer",END)

graph = builder.compile()