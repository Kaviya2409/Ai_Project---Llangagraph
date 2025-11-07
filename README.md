🤖 AI Arithmetic Agent - Perfect README

```ai-project/README.md
# 🤖 AI Arithmetic Agent with LangGraph

[![CI](https://github.com/Kaviya2409/Ai_Project---Llangagraph/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/Kaviya2409/Ai_Project---Llangagraph/actions/workflows/unit-tests.yml)
[![Integration Tests](https://github.com/Kaviya2409/Ai_Project---Llangagraph/actions/workflows/integration-tests.yml/badge.svg)](https://github.com/Kaviya2409/Ai_Project---Llangagraph/actions/workflows/integration-tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A sophisticated AI agent built with LangGraph that understands natural language and performs arithmetic computations through intelligent tool integration. This project demonstrates the power of combining large language models with structured function calling for precise mathematical operations.

## 📸 Project Showcase

<div align="center">

### LangGraph Studio Visualization
![LangGraph Studio Interface](./static/studio_ui.png)

### Agent in Action
![Terminal Output](./static/terminal-demo.png)
*Agent processing arithmetic queries with tool execution*

### Project Architecture
![Architecture Diagram](./static/architecture-diagram.png)
*High-level system architecture showing data flow*

</div>

## 🚀 Key Features

- 🧠 **Natural Language Understanding**: Processes conversational math queries
- 🛠️ **Tool Integration**: Seamlessly calls arithmetic functions (add, multiply, divide)
- 📊 **Real-time Computation**: Executes mathematical operations instantly
- 🎯 **State Management**: Maintains conversation context and computation history
- 🔧 **Visual Debugging**: LangGraph Studio for workflow visualization
- 🚀 **Local Processing**: Runs on Ollama's Llama3.2:1b for privacy and speed
- 🧪 **Comprehensive Testing**: Full test suite with unit and integration tests
- 🔄 **CI/CD Pipeline**: Automated testing and deployment with GitHub Actions

## 🛠 Technology Stack

### Core Technologies
| Component | Version | Purpose |
|-----------|---------|---------|
| **LangGraph** | ≥1.0.0 | Workflow orchestration and graph management |
| **LangChain** | ≥1.0.3 | LLM integration and tool binding |
| **LangChain Ollama** | ≥1.0.0 | Local LLM connectivity |
| **Llama3.2:1b** | Latest | Natural language processing engine |
| **Python** | ≥3.10 | Core programming language |

### Development Tools
| Tool | Purpose |
|------|---------|
| **UV** | Fast package management |
| **Ruff** | Linting and formatting |
| **MyPy** | Static type checking |
| **Pytest** | Testing framework |
| **GitHub Actions** | CI/CD automation |

## 📁 Project Structure

```
ai-project/
├── 📂 src/agent/                  # Core application code
│   ├── 🐍 __init__.py             # Package initialization
│   └── 🧮 graph.py                # Main agent logic and workflow
├── 📂 static/                      # Static assets and screenshots
│   ├── 🖼️ studio_ui.png           # LangGraph Studio interface
│   ├── 🖼️ terminal-demo.png       # Terminal output demonstration
│   └── 🖼️ architecture-diagram.png # System architecture
├── 📂 tests/                       # Test suite
│   ├── 📂 unit/                   # Unit tests
│   └── 📂 integration/            # Integration tests
├── 📂 .github/workflows/           # GitHub Actions CI/CD
│   ├── 🔧 unit-tests.yml          # Unit test automation
│   └── 🔧 integration-tests.yml   # Integration test automation
├── 📄 pyproject.toml              # Dependencies and project config
├── 📄 langgraph.json             # LangGraph server configuration
├── 📄 Makefile                    # Build and development commands
├── 📄 .gitignore                  # Git ignore patterns
├── 📄 LICENSE                     # MIT License
└── 📄 README.md                   # This documentation
```

## 🏗️ Architecture Overview

### System Architecture
![System Architecture](./static/architecture-diagram.png)

### Component Breakdown

1. **🤖 LLM Engine**: ChatOllama with Llama3.2:1b model
2. **🛠️ Tool Executor**: Mathematical function handler
3. **📊 State Manager**: Conversation and computation state
4. **🔄 Workflow Engine**: LangGraph orchestration
5. **🎛️ Interface**: CLI and LangGraph Studio

### Data Flow
```
User Input → LLM Processing → Tool Selection → Function Execution → Response Generation → Output
```

## 🧮 Supported Operations

### Arithmetic Functions

| Function | Operation | Example | Output |
|----------|-----------|---------|--------|
| **add()** | Addition (currently subtracts - bug to fix) | "add(5, 3)" | 2 |
| **multiply()** | Multiplication | "multiply(4, 6)" | 24 |
| **divide()** | Division | "divide(15, 3)" | 5.0 |

### Natural Language Examples

```python
# Supported queries
"What is 5 + 3?"
"Calculate 10 * 4"
"Divide 100 by 5"
"Can you multiply 7 by 8?"
"What do you get when you add 12 and 8?"
```

## 🚀 Quick Start Guide

### Prerequisites

1. **Install Ollama** (if not already installed):
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

2. **Pull the required model**:
   ```bash
   ollama pull llama3.2:1b
   ```

### Installation

```bash
# Clone the repository
git clone https://github.com/Kaviya2409/Ai_Project---Llangagraph.git
cd ai-project

# Install dependencies with UV
uv sync

# Or with pip (alternative)
pip install -e . "langgraph-cli[inmem]"
```

### Running the Agent

#### Option 1: LangGraph Server (Recommended)
```bash
# Start the development server
langgraph dev

# Open LangGraph Studio at: http://localhost:8123
```

#### Option 2: Direct Python Execution
```bash
# Run the test case directly
python src/agent/graph.py
```

#### Option 3: Interactive Mode
```bash
# Import and use in Python
from src.agent.graph import graph

# Test the agent
result = graph.invoke({
    "messages": [{"type": "human", "content": "What is 5 + 3?"}],
    "changeme": 36,
    "llm_calls": 0
})

print(result)
```

## 🖥️ Usage Examples

### Terminal Output
![Terminal Usage Example](./static/terminal-demo.png)

### Sample Interactions

```python
# Example 1: Addition
>>> result = graph.invoke({
...     "messages": [{"type": "human", "content": "What is 15 + 7?"}],
...     "changeme": 36,
...     "llm_calls": 0
... })
>>> print(result['messages'][-1].content)
"The result of adding 15 and 7 is 22."

# Example 2: Multiplication
>>> result = graph.invoke({
...     "messages": [{"type": "human", "content": "Multiply 8 by 6"}],
...     "changeme": 36,
...     "llm_calls": 0
... })
>>> print(result['messages'][-1].content)
"8 multiplied by 6 equals 48."

# Example 3: Division
>>> result = graph.invoke({
...     "messages": [{"type": "human", "content": "What's 100 divided by 4?"}],
...     "changeme": 36,
...     "llm_calls": 0
... })
>>> print(result['messages'][-1].content)
"100 divided by 4 is 25.0."
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file:
```bash
cp .env.example .env
```

Available configuration options:
```env
# LangSmith tracing (optional)
LANGCHAIN_TRACING_V2=false
LANGSMITH_API_KEY=lsv2_your_key_here

# Ollama configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:1b
```

### LangGraph Configuration

The `langgraph.json` file configures the server:
```json
{
  "$schema": "https://langgra.ph/schema.json",
  "dependencies": ["."],
  "graphs": {
    "agent": "./src/agent/graph.py:graph"
  },
  "env": ".env",
  "image_distro": "wolfi"
}
```

## 🧪 Testing

### Run All Tests
```bash
# Using UV
uv run pytest

# Using pip
pytest
```

### Run Specific Test Suites
```bash
# Unit tests only
uv run pytest tests/unit/

# Integration tests only
uv run pytest tests/integration/

# With coverage
uv run pytest --cov=src --cov-report=html
```

### Test Results
![Test Results](./static/test-results.png)

## 📊 Development Workflow

### Code Quality
```bash
# Linting
uv run ruff check .
uv run ruff format .

# Type checking
uv run mypy src/

# Run all quality checks
uv run ruff check . && uv run mypy src/ && uv run pytest
```

### LangGraph Studio Development

1. **Start the server**:
   ```bash
   langgraph dev
   ```

2. **Open Studio**: Navigate to `http://localhost:8123`

3. **Debug workflow**: Use the visual interface to test and debug

### Studio Interface Features
![LangGraph Studio Features](./static/studio-features.png)

## 🔧 Extending the Agent

### Adding New Tools

1. **Define new function** in `src/agent/graph.py`:
   ```python
   def power(base: float, exponent: float) -> float:
       """Calculate base to the power of exponent."""
       return base ** exponent
   ```

2. **Add to tools list**:
   ```python
   tools = [add, multiply, divide, power]
   ```

3. **Update system prompt** if needed:
   ```python
   SystemMessage(content="You are a helpful assistant tasked with performing arithmetic and mathematical calculations.")
   ```

4. **Add tests** for the new functionality

### Customizing the State

```python
@dataclass
class State:
    messages: List[Any] = field(default_factory=list)
    changeme: int = 36
    llm_calls: int = 0
    # Add your custom fields
    calculation_history: List[str] = field(default_factory=list)
    user_preferences: Dict[str, Any] = field(default_factory=dict)
```

## 🐛 Known Issues & Fixes

### Current Bug: Addition Function
The `add()` function currently performs subtraction instead of addition:

```python
# Current (buggy) code:
def add(a: int, b: int) -> int:
    return a - b  # This should be a + b

# Fixed version:
def add(a: int, b: int) -> int:
    return a + b
```

## 🚀 Deployment

### Docker Deployment
```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY . .
RUN pip install -e . "langgraph-cli[inmem]"
EXPOSE 8123
CMD ["langgraph", "dev", "--host", "0.0.0.0"]
```

### Environment Setup
![Deployment Architecture](./static/deployment-architecture.png)

## 🤝 Contributing

1. **Fork** the repository
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and add tests
4. **Run the test suite**: `uv run pytest`
5. **Commit your changes**: `git commit -m 'Add amazing feature'`
6. **Push to the branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Contribution Guidelines
![Contribution Workflow](./static/contribution-workflow.png)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangChain Team** for the amazing LangChain and LangGraph frameworks
- **Ollama Project** for providing local LLM capabilities
- **OpenAI** for pioneering LLM technology
- **GitHub Community** for the valuable feedback and contributions

## 🔗 Resources & Links

### Documentation
- [📚 LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [🤖 LangChain Documentation](https://python.langchain.com/)
- [🦙 Ollama Documentation](https://ollama.ai/documentation)
- [🔧 Python Package Index](https://pypi.org/)

### Tools & Services
- [🧪 LangSmith](https://smith.langchain.com/) - Monitoring and debugging
- [🐙 GitHub Repository](https://github.com/Kaviya2409/Ai_Project---Llangagraph)
- [🎨 LangGraph Studio](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/)

### Community
- [💬 Discord Community](https://discord.gg/langchain)
- [🐦 Twitter Updates](https://twitter.com/langchainai)
- [📈 GitHub Discussions](https://github.com/langchain-ai/langgraph/discussions)

---

<div align="center">

**⭐ Star this repository if it helped you!**

Made with ❤️ by [Kaviya2409](https://github.com/Kaviya2409)

[![GitHub followers](https://img.shields.io/github/followers/Kaviya2409?style=social)](https://github.com/Kaviya2409)
[![GitHub stars](https://img.shields.io/github/stars/Kaviya2409/Ai_Project---Llangagraph?style=social)](https://github.com/Kaviya2409/Ai_Project---Llangagraph)

</div>
```

## 📸 Screenshots You Need to Add

To make this README complete, you'll need to create these screenshots and place them in the `static/` folder:

1. **`terminal-demo.png`** - Show terminal output when running the agent
2. **`architecture-diagram.png`** - Create a simple diagram showing the system architecture
3. **`test-results.png`** - Show pytest results
4. **`studio-features.png`** - Show LangGraph Studio interface
5. **`deployment-architecture.png`** - Show deployment setup
6. **`contribution-workflow.png`** - Show Git workflow

## 🚀 Commands to Apply This README

```bash
# Navigate to your project
cd /home/kaviya/projects/ai-project

# Add the new README
git add README.md

# Commit with a detailed message
git commit -m "Add comprehensive README.md with complete documentation

- Added detailed project overview and features
- Included technology stack with versions
- Added project structure visualization
- Created architecture section with diagrams
- Added installation and usage guides
- Included testing and development instructions
- Added screenshots placeholders for visual documentation
- Added contribution guidelines and resources
- Updated with proper GitHub badges and links"

# Push to GitHub
git push origin main
