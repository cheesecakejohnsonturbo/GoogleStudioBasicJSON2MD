#!/bin/bash

# Shell script to process Google AI Studio chat logs and convert them to Markdown.

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not found. Please install Python 3."
    exit 1
fi

# Ask for input and output file names (interactive)
read -r -p "Enter the name of the input JSON file (e.g., chat_log.json): " input_file
read -r -p "Enter the name of the output Markdown file (e.g., output.md): " output_file

# Check if the input file exists
if [ ! -f "$input_file" ]; then
  echo "Error: Input file '$input_file' not found."
  exit 1
fi

# Run the Python script with customizable role names (using defaults here)
python3 process_chat_logs.py "$input_file" "$output_file"

exit 0