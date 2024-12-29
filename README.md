# LangGraph Course Exercises Repository

This repository contains my solutions to the exercises from the [LangGraph course](https://academy.langchain.com/) offered by LangChain Academy. The exercises are structured to provide hands-on experience with LangChain's core concepts, focusing on chains, routers, agents, and more.

## Repository Structure

The repository is organized into the following directories:

### 1. **.langgraph_api/**

This directory contains API configuration and related assets, including visual resources like diagrams and examples:

- `assets/`: Visual assets, including images (`chain.png`, `router.png`, etc.) used to illustrate concepts.

### 2. **langgraph_academy/module_1/**

This directory holds solutions to exercises for Module 1 of the LangGraph course. It is subdivided into specific sections:

- `agent/`: Exercises related to creating and managing agents.
  - `agent.ipynb`: Jupyter notebook with detailed explanations and outputs.
  - `agent.py`: Python script version of the exercises.
- `chain/`: Exercises on building and managing chains.
  - `chain.ipynb`: Jupyter notebook with detailed explanations and outputs.
  - `chain.py`: Python script version of the exercises.
- `router/`: Exercises focused on implementing routing mechanisms.
  - `router.ipynb`: Jupyter notebook with detailed explanations and outputs.
  - `router.py`: Python script version of the exercises.
- `simple/`: Exercises on simpler foundational concepts.
  - `simple.ipynb`: Jupyter notebook with detailed explanations and outputs.
  - `simple.py`: Python script version of the exercises.

### 3. **models/**

Placeholder for models used or created during exercises.

### 4. **tests/**

Contains test cases and utilities for verifying the implementations.

### Root-level files:

- `.env`: Environment variables for API keys and configurations.
- `docker-compose.yml`: Docker configuration for running the project in a containerized environment.
- `langgraph.json`: LangGraph-specific settings or configurations.
- `pyproject.toml` & `poetry.lock`: Python project configuration and dependency management files.
- `README.md`: Project documentation (this file).

## Getting Started

To set up and run this project locally, follow these steps:

### Prerequisites

- **Python 3.11 or later**.
- **Poetry**: For dependency management. Install it via:
  ```bash
  pip install poetry
  ```
- **API Keys**:
  - **OpenAI API**: Add your OpenAI API key to the `.env` file.
  - **LangSmith API**: Add your LangSmith API key to the `.env` file.
  - **Tavily API**: Add your Tavily API key for web search features.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/langgraph-course-exercises.git
   cd langgraph-course-exercises
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

3. Activate the virtual environment:

   ```bash
   poetry shell
   ```

4. Set up the environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

### Running the Exercises

- Open Jupyter notebooks for interactive exploration:
  ```bash
  jupyter notebook
  ```
- Run Python scripts directly:
  ```bash
  python langgraph_academy/module_1/chain/chain.py
  ```

### Using Docker

Alternatively, you can use Docker for a containerized setup:

1. Build and run the container:
   ```bash
   docker-compose up --build
   ```
2. Access the environment in your browser or terminal.

## Contributing

If you'd like to contribute or report an issue, feel free to open a pull request or issue in this repository.

## Resources

- **LangChain Academy**: [LangGraph course](https://academy.langchain.com/)
- **LangGraph Documentation**: [LangGraph Docs](https://www.langchain.com/langgraph)
