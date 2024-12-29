#!/bin/bash

# Script to create Ollama models from directories in the `models` folder

# Ensure Ollama is running
if ! curl -s http://localhost:11434/status | grep "ok" > /dev/null; then
  echo "Ollama server is not running. Please start it using 'docker-compose up' and try again."
  exit 1
fi

# Loop through directories inside the `models` folder
for dir in models/*/; do
  # Ensure the directory exists and is not empty
  if [ -d "$dir" ]; then
    # Extract the model name from the directory name
    model_name=$(basename "$dir")

    # Path to the Modelfile
    modelfile_path="${dir}Modelfile"

    # Check if the Modelfile exists
    if [ -f "$modelfile_path" ]; then
      echo "Creating Ollama model: $model_name from $modelfile_path"
      ollama create "$model_name" -f "$modelfile_path"
    else
      echo "No Modelfile found in $dir. Skipping..."
    fi
  fi
done

echo "Ollama model creation process completed."
