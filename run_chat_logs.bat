@echo off
REM Batch file to process Google AI Studio chat logs and convert them to Markdown.

REM Check if Python is in the PATH
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not found in your PATH.  Please install Python and add it to your PATH.
    pause
    exit /b 1
)

REM Get input and output file names from the user (optional, but user-friendly)
set /p "input_file=Enter the name of the input JSON file (e.g., chat_log.json): "
set /p "output_file=Enter the name of the output Markdown file (e.g., output.md): "

REM Check if input file exists
if not exist "%input_file%" (
    echo Error: Input file "%input_file%" not found.
    pause
    exit /b 1
)

REM Run the Python script
python process_chat_logs.py "%input_file%" "%output_file%"

pause