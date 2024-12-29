from typing import TypedDict, Annotated
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from IPython.display import display, Image
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage
from pprint import pprint


llm = ChatOllama(
    model="llama3.1-tool",
    base_url="http://localhost:11434",
    max_tokens=1000,
    temperature=0.8,
)

def multiply(a: int, b: int) -> int:
    """
    Multiply a and b only when the operation is requested.

    Args:
        a (int): First number
        b (int): Second number
    """
    return a * b

llm_with_tools = llm.bind_tools([multiply])

class MessageState(TypedDict):
    messages: Annotated[list[str], add_messages]

# Node
def tool_calling_llm(state: MessageState):
    return {
        "messages": [llm_with_tools.invoke(state["messages"])]
    }

graph_builder = StateGraph(MessageState)
graph_builder.add_node("tool_calling_llm", tool_calling_llm)
graph_builder.add_node("tools", ToolNode([multiply]))

graph_builder.add_edge(START, "tool_calling_llm")
graph_builder.add_conditional_edges("tool_calling_llm", tools_condition)
graph_builder.add_edge("tools", END)

graph = graph_builder.compile()

if __name__ == "__main__":

    messages = [HumanMessage("What is 2 multiplied by 3?")]
    messages = graph.invoke({"messages": messages})

    for m in messages["messages"]:
        m.pretty_print()

    messages = [HumanMessage("Hello,  how are you?")]
    messages = graph.invoke({"messages": messages})
    for m in messages["messages"]:
        m.pretty_print()