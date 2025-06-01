#!/bin/bash

echo "Initializing git repo..."
git init

echo "Creating Python virtual environment..."
python -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Creating .gitignore file..."
cat > .gitignore << EOL
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
venv/

# dotenv environment variables file
.env

# Jupyter Notebook checkpoints
.ipynb_checkpoints

# Docker files to exclude (optional)
papers/

EOL

echo "Adding files to git and committing..."
git add .
git commit -m "Initial commit with project structure and code"
