from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.prebuilt import tools_condition, ToolNode

llm = ChatOllama(
    model="llama3.1-tool",
    base_url="http://localhost:11434",
    temperature=0.8,
    max_tokens=1000
)

def multiply(a:int, b:int)-> int:
    """Multiply a and b.
    
    Args:
        a: first int
        b: second int
    """
    return a*b

def add(a:int, b:int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a+b

def divide(a:int, b:int) -> float:
    """Divide a and b.
    
    Args:
        a: first int
        b: second: int
    """
    return a/b

tools = [multiply, add, divide]
llm_with_tools = llm.bind_tools(tools)

# System Message
system_message = SystemMessage(content="You are a helpful AI assistant tasked with performing arithmatic on a set of inputs.")

# Assistant
def assistant(state: MessagesState):
    return {"messages": llm_with_tools.invoke([system_message] + state["messages"])}

# Graph
builder = StateGraph(MessagesState)

# Add the nodes
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

# Add the edges
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")


# Compile
memory = MemorySaver()
graph = builder.compile(interrupt_before=["assistant"], checkpointer=memory)