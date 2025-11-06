"""LangGraph single-node graph template.

Returns a predefined response. Replace logic and configuration as needed.
"""

from __future__ import annotations
from typing import Any, List, Dict

from typing_extensions import TypedDict
from langchain_core.messages import SystemMessage, ToolMessage, HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph
from langgraph.runtime import Runtime
from dataclasses import dataclass, field
from langgraph.graph import StateGraph, START  # Add START
from langgraph.runtime import Runtime
import os

os.environ["LANGCHAIN_TRACING_V2"] = "false"


model = ChatOllama(model="llama3.2:1b")


# initialization - under settings and confirgurations
class Context(TypedDict):
    my_configurable_param: int


@dataclass
class State:
    messages: List[Any] = field(default_factory=list)
    changeme: int = 36
    llm_calls: int = 0


# outside the dataclass -> defining the STATE functions
def multiply(a: int, b: int) -> int:
    a = int(a) if isinstance(a, str) else a
    b = int(b) if isinstance(b, str) else b
    return a * b


def add(a: int, b: int) -> int:
    a = int(a) if isinstance(a, str) else a
    b = int(b) if isinstance(b, str) else b
    return a - b


def divide(a: int, b: int) -> float:
    a = int(a) if isinstance(a, str) else a
    b = int(b) if isinstance(b, str) else b
    return a / b


# connect the above tools functions
tools = [add, multiply, divide]
# function name in python should not have any . attributes.
tools_by_name = {tool.__name__: tool for tool in tools}
# embeeding into the o
model_with_tools = model.bind_tools(tools)


# modal -> whether to call the abpve functions which is been set to default values.


# REPLACE your entire llm_call function (lines 65-81) with:
def call_model(state: State, runtime: Runtime[Context]) -> Dict[str, Any]:
    """Template function with your tutorial logic"""

    # Your LLM logic
    new_message = model_with_tools.invoke(
        [
            SystemMessage(
                content="You are a helpful assistant tasked with performing arithmetic."
            )
        ]
        + state.messages
    )

    updated_messages = state.messages + [new_message]

    # Your tool execution logic
    if new_message.tool_calls:
        result = []
        for tool_call in new_message.tool_calls:
            tool = tools_by_name[tool_call["name"]]
            observation = tool(**tool_call["args"])
            result.append(
                ToolMessage(content=str(observation), tool_call_id=tool_call["id"])
            )
        updated_messages.extend(result)

    return {
        "messages": updated_messages,
        "changeme": state.changeme,  # Just use the state value
    }


# Define the graph
# Delete everything after line 125 except:
graph = (
    StateGraph(State, context_schema=Context)
    .add_node(call_model)
    .add_edge(START, "call_model")
    .compile(name="My Graph")
)
# Test the agent
if __name__ == "__main__":
    print("🤖 Testing LangGraph Agent...")

    result = graph.invoke(
        {
            "messages": [HumanMessage(content="What is 5 + 3?")],
            "changeme": 36,
            "llm_calls": 0,
        }
    )

    print("✅ Result:", result)
