from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage
class MessageState(TypedDict):

    messages: Annotated[list[AnyMessage], add_messages]

llm = ChatOllama(
    model="llama3.1",
    base_url="http://localhost:11434",
    max_tokens=500,
    temperature=0.8,
)

def multiply(a: int, b: int) -> int:
    """
    Multiply a by b only when asked to do so.

    Args:
        a (int): The first number.
        b (int): The second number.
    """
    return a * b

llm_with_tool = llm.bind_tools([multiply])

def tool_calling_llm(state: MessageState):
    return {
        "messages": llm_with_tool.invoke(state["messages"])
    }

graph_builder = StateGraph(MessageState)
graph_builder.add_node("tool_calling_llm", tool_calling_llm)
graph_builder.add_edge(START, "tool_calling_llm")
graph_builder.add_edge("tool_calling_llm", END)

graph = graph_builder.compile()


if __name__ == "__main__":

    messages = graph.invoke({"messages": HumanMessage("Hello, how are you?")})
    print(messages)

    messages = graph.invoke({"messages": HumanMessage("Multiply 3 by 5.")})
    print(messages)