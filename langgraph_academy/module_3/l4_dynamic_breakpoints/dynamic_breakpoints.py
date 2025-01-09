from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.errors import NodeInterrupt
from langgraph.checkpoint.memory import MemorySaver

class State(TypedDict):
    input: str


def step_1(state: State) -> State:
    print("---- Step 1 ----")
    return state

def step_2(state: State) -> State:
    print("---- Step 2 ----")
    if len(state['input']) > 5:
        raise NodeInterrupt(f"Input is longer than 5 characters: {state['input']}")
    return state

def step_3(state: State) -> State:
    print("---- Step 3 ----")
    return state


builder = StateGraph(State)

builder.add_node("step_1", step_1)
builder.add_node("step_2", step_2)
builder.add_node("step_3", step_3)

builder.add_edge(START, 'step_1')
builder.add_edge("step_1", "step_2")
builder.add_edge("step_2","step_3")
builder.add_edge("step_3", END)

memory = MemorySaver()

graph = builder.compile(checkpointer=memory)