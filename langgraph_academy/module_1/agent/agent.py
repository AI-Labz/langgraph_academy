from typing import TypedDict, Annotated
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph.message import add_messages

class MessageState(TypedDict):
    messages: Annotated[list[str], add_messages]

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

def add(a: int, b: int) -> int:
    """
    Add a and b only when the operation is requested.

    Args:
        a (int): First number
        b (int): Second number
    """
    return a + b

def divide(a: int, b: int) -> int:
    """
    Divide a and b only when the operation is requested.

    Args:
        a (int): First number
        b (int): Second number
    """
    return a / b

tools = [multiply, add, divide]
llm_with_tools = llm.bind_tools(tools)


system_message = SystemMessage(
    content="You are a helpful AI that can do math. You can multiply, add, and divide numbers given a set of inputs. You can also chat with me about anything else.",
)

# Node
def assistant(state: MessageState):
    messages = [system_message] + state["messages"]
    return {
        "messages": [llm_with_tools.invoke(messages)]
    }

graph_builder = StateGraph(MessageState)
graph_builder.add_node("assistant", assistant)
graph_builder.add_node("tools", ToolNode(tools))

graph_builder.add_edge(START, "assistant")
graph_builder.add_conditional_edges("assistant", tools_condition)
graph_builder.add_edge("tools", "assistant")


graph = graph_builder.compile()


if __name__ == "__main__":
    messages = [HumanMessage(content="Add 3 and 4. Multiply the output by 2. Divide the output by 5.")]
    messages = graph.invoke({"messages": messages})

    for m in messages["messages"]:
        m.pretty_print()