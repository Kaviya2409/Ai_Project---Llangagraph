# 🤖 AI Arithmetic Agent

An intelligent AI agent built with LangGraph that performs arithmetic operations using natural language processing. This agent leverages Ollama's Llama3.2 model to understand user requests and execute mathematical computations through integrated tools.

<div align="center">
  <img src="" alt="" width="" />
</div>

## 🚀 Features

- **Natural Language Processing**: Understands mathematical queries in conversational language
- **Arithmetic Operations**: Performs addition, multiplication, and division
- **Tool Integration**: Seamlessly executes computational functions
- **LangGraph Workflow**: Visual debugging and development with LangGraph Studio
- **Local AI Processing**: Runs on Ollama's Llama3.2:1b model for privacy and speed
- **Comprehensive Testing**: Unit and integration tests for reliability

## 🛠 Tech Stack

- **Core**: LangGraph, LangChain
- **LLM**: Ollama Llama3.2:1b
- **Language**: Python 3.10+
- **Package Management**: UV
- **Testing**: Pytest
- **Code Quality**: Ruff, MyPy
- **CI/CD**: GitHub Actions

## 📋 Project Structure

```
ai-project/
├── src/agent/
│   ├── __init__.py
│   └── graph.py          # Core agent logic with arithmetic tools
├── static/
│   └── studio_ui.png     # LangGraph Studio interface
├── tests/                # Test suite
├── .github/workflows/    # CI/CD automation
├── pyproject.toml        # Dependencies & configuration
├── langgraph.json       # LangGraph server configuration
└── README.md            # This file
```

## 🚀 Quick Start

### Prerequisites

1. **Install Ollama** and pull the required model:
```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull llama3.2:1b
```

2. **Clone and install dependencies**:
```bash
git clone https://github.com/USERNAME/ai-project.git
cd ai-project
uv sync
```

### Running the Agent

**Option 1: LangGraph Server**
```bash
langgraph dev
```

**Option 2: Direct Python execution**
```bash
python src/agent/graph.py
```

### Usage Examples

The agent can handle various arithmetic queries:

```python
# Test examples
"What is 5 + 3?"
"Calculate 10 * 4"
"Divide 100 by 5"
```

## 🔧 Configuration

Create a `.env` file for optional settings:

```bash
cp .env.example .env
```

Available environment variables:
```env
LANGCHAIN_TRACING_V2=false    # Disable/enable LangSmith tracing
LANGSMITH_API_KEY=your_key     # Optional: LangSmith for monitoring
```

## 🏗 Architecture

The agent is built using LangGraph's workflow architecture:

1. **State Management**: Maintains conversation context and computation history
2. **Tool Integration**: Arithmetic functions (add, multiply, divide) bound to the LLM
3. **Model Configuration**: Llama3.2:1b model with system prompt for math assistance
4. **Message Flow**: Human messages → LLM processing → Tool execution → Response

### Core Components

- **State Class**: Manages conversation messages and computation state
- **Arithmetic Tools**: `add()`, `multiply()`, `divide()` functions
- **Model Handler**: `call_model()` function orchestrates LLM and tool interactions
- **Graph Definition**: Workflow structure with LangGraph StateGraph

## 🧪 Testing

Run the test suite:

```bash
# Unit tests
uv run pytest tests/unit/

# Integration tests
uv run pytest tests/integration/

# All tests
uv run pytest
```

## 📊 Development

### Code Quality Tools

```bash
# Linting and formatting
ruff check .
ruff format .

# Type checking
mypy src/
```

### LangGraph Studio

Use LangGraph Studio for visual debugging:
1. Start the server: `langgraph dev`
2. Open Studio to visualize the agent graph
3. Test interactions and debug workflow

### Extending the Agent

To add new capabilities:

1. **Add new tools** in `src/agent/graph.py`
2. **Update the tool list**: `tools = [add, multiply, divide, your_new_tool]`
3. **Modify system prompt** to reflect new capabilities
4. **Update tests** to cover new functionality

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Ollama Documentation](https://ollama.ai/documentation)
- [LangChain Documentation](https://python.langchain.com/)
- [LangSmith](https://smith.langchain.com/) (for monitoring and debugging)
```

**Note**: Replace `USERNAME` with your actual GitHub username before pushing to your repository!

This README accurately reflects your AI arithmetic agent project with proper documentation of its features, architecture, and usage instructions.
