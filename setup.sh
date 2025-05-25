#!/bin/bash
echo "Starting DevOps Environment Setup..."

# Step 1: Update the system
sudo apt update && sudo apt upgrade -y

# Step 2: Install Git
sudo apt install git -y

# Step 3: Install Python & pip
sudo apt install python3 python3-pip -y

# Step 4: Install VS Code
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] \
https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code -y

# Step 5: Install Python libraries and tools
pip install ruff debugpy jupyter cline uv numpy pandas streamlit

echo "✅ All tools installed successfully!"

