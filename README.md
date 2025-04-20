# Modal VSCode Server

This repository demonstrates how to deploy Visual Studio Code as a serverless workstation using Modal. It allows you to run a VSCode server in the cloud that you can connect to from anywhere.

## Overview

The project sets up a persistent VSCode server on Modal's infrastructure, enabling you to:

- Access your development environment from any device with a web browser
- Maintain persistent storage for your code, settings, and extensions
- Work in a consistent environment without local setup requirements

## How It Works

The deployment uses Modal's serverless infrastructure to:

1. Create a container with VSCode installed
2. Set up persistent volumes for VSCode settings and your code repositories
3. Run VSCode in "tunnel" mode, which allows secure remote access
4. Keep the server running continuously

## Prerequisites

- A Modal account (sign up at [modal.com](https://modal.com))
- Modal CLI installed (`pip install modal`)
- A device with a web browser to connect to the VSCode server

## Setup and Deployment

1. Clone this repository:

   ```bash
   git clone https://github.com/ericmjl/modal-vscode-server.git
   cd modal-vscode-server
   ```

2. Deploy the VSCode server to Modal:

   ```bash
   uvx modal deploy deploy_vscode.py
   ```

3. Run the VSCode server:

   ```bash
   uvx modal run deploy_vscode.py::run_vscode_server
   ```

4. Follow the authentication instructions that appear in the terminal to connect to your VSCode server.

The server will time out after 5 minutes of inactivity. Adjust the amount of RAM, CPU, and GPU needed based on your use case.

## Key Components

- **Persistent Volumes**: Three Modal volumes are used to maintain state:
  - `vscode-server`: Stores VSCode settings and configurations
  - `vscode-server-dir`: Stores VSCode server-specific data
  - `workstation-code-dir`: Stores your code repositories

- **Container Setup**: The Modal image is configured with:
  - Debian Slim as the base
  - Git, wget, curl, and other essential tools
  - Official Microsoft VSCode package
  - Pixi package manager for Python environment management

## Usage

Once connected to your VSCode server:

1. You can install extensions as needed
2. Clone repositories to the `/root/_repos` directory for persistence
3. Configure your settings as you would in a local VSCode installation
4. Use Pixi to manage Python environments for your projects

Your environment will persist between sessions, allowing you to continue your work seamlessly.

## Limitations

- Performance depends on Modal's infrastructure and your internet connection
- Some VSCode extensions that require specific local resources might not work
- The server will consume Modal credits while running

## License

[MIT License](LICENSE)
