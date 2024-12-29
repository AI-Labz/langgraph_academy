# LangGraph Course Exercises Repository

This repository contains my solutions to the exercises from the [LangGraph course](https://academy.langchain.com/) offered by LangChain Academy. The exercises are structured to provide hands-on experience with LangChain's core concepts, focusing on chains, routers, agents, and more.

## Repository Structure

The repository is organized into the following directories:

- `assets/`: Visual assets, including images (`chain.png`, `router.png`, etc.) used to illustrate concepts.

### 1. **langgraph_academy/module_1/**

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

### 2. **models/**

This directory contains model files for creating custom models in Ollama. Each model has its own subdirectory with a `Modelfile` defining the model's configuration.

### 3. **tests/**

Contains test cases and utilities for verifying the implementations.

### Root-level files:

- `.env`: Environment variables for API keys and configurations.
- `docker-compose.yml`: Docker configuration for running a containerized Ollama server.
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

  - **LangSmith API**: Add your LangSmith API key to the `.env` file.
  - **Tavily API**: Add your Tavily API key for web search features.

- **Docker**: Install Docker to run the Ollama server.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/langgraph_academy.git
   cd langgraph_academy
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
   touch .env
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

### Running Ollama in Docker

To run a containerized Ollama server:

1. Build and start the Docker container:

   ```bash
   docker-compose up -d
   ```

2. Verify that Ollama is running:
   ```bash
   curl http://localhost:11434/status
   ```

### Creating Ollama Models

To create models defined in the `models/` directory, use the provided Bash script:

1. Run the script:

   ```bash
   bash create_ollama_models.sh
   ```

2. The script loops through all subdirectories inside the `models/` folder, finds the `Modelfile` for each model, and uses the subdirectory name as the model name to create the Ollama model. Ensure Ollama is running before executing the script.

## Contributing

If you'd like to contribute or report an issue, feel free to open a pull request or issue in this repository.

## Resources

- **LangChain Academy**: [LangGraph course](https://academy.langchain.com/)
- **LangGraph Documentation**: [LangGraph Docs](https://www.langchain.com/langgraph)

---
