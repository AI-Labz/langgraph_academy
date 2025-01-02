from typing import TypedDict, Literal
import random
from langgraph.graph import StateGraph, START, END
from IPython.display import display, Image

class State(TypedDict):

    graph_state: str


def node_1(state: State) -> dict[str, str]:
    print("---- Node 1 Executed ----")
    return {"graph_state": state["graph_state"] + " I'm"}

def node_2(state: State) -> dict[str, str]:
    print("---- Node 2 Executed ----")
    return {"graph_state": state["graph_state"] + " happy!"}

def node_3(state: State) -> dict[str, str]:
    print("---- Node 3 Executed ----")
    return {"graph_state": state["graph_state"] + " sad!"}

def decide_mood(state: State) -> Literal["node_2", "node_3"]:
    return "node_2" if random.random() > 0.5 else "node_3"


graph_builder = StateGraph(State)

graph_builder.add_node("node_1", node_1)
graph_builder.add_node("node_2", node_2)
graph_builder.add_node("node_3", node_3)

graph_builder.add_edge(START, "node_1")
graph_builder.add_conditional_edges("node_1", decide_mood)
graph_builder.add_edge("node_2", END)
graph_builder.add_edge("node_3", END)

graph = graph_builder.compile()


if __name__ == "__main__":
    state = {"graph_state": "Hi, my name is Guilherme."}
    response = graph.invoke(state)
    print(response)