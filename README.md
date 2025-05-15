# Docker-AI CLI Tool

The Docker-AI CLI tool provides an intelligent interface for managing Docker environments. It translates natural language user intent into precise Docker operations, aiming to make Docker management more accessible and efficient. This tool acts as an intermediary between the user and the Docker daemon, leveraging Large Language Models (LLMs) via the google-adk framework to interpret user intent.

## Features

  * **Natural Language Query Processing:** Interprets natural language queries and utilizes the google-adk for interfacing with LLMs.
  * **Docker Command Generation:** Translates interpreted intent into valid Docker CLI commands and proposes them for confirmation.
  * **Docker Command Execution:** Executes generated Docker commands and displays output.
  * **LLM Provider Integration:** Supports integration with various LLM providers (initially Gemini 2.0 Flash) via google-adk and manages API keys using `python-dotenv`.
  * **Interactive Mode:** Provides a conversational interactive mode built with Click that maintains context across queries and supports special commands.
  * **Error Handling and Feedback:** Identifies and reports errors from natural language interpretation, command generation, or execution using the logging library, providing informative messages and suggestions.

## Installation

The tool requires Python 3.12 and `pip` installed.

1.  **Prerequisites:** Ensure you have Docker Engine or Docker Desktop installed and running. Install Python 3.12.
2.  **Install via pip:** The tool and its dependencies can be installed from a source repository or a package index.
```bash
pip install docker-ai
```

1.  **Required Packages:** The installation via pip should handle the core dependencies: `google-adk`, `python-dotenv`, `click`, `json`, `logging`, `pathlib`, `subprocess`.

## Configuration

LLM API keys must be managed via environment variables, preferably loaded using `python-dotenv`. The system will securely retrieve API keys from environment variables based on the selected LLM provider (e.g., `GEMINI_API_KEY`, `OPENAI_API_KEY`).

1.  **Create a `.env` file:** In the directory where you run the tool, create a file named `.env`.
2.  **Add your API key:** Add your LLM provider API key to the `.env` file. For example, for Gemini:
    ```dotenv
    GEMINI_API_KEY=your_gemini_api_key
    ```
    Replace `your_gemini_api_key` with your actual API key. Ensure sensitive information like API keys are not exposed in logs or standard output.

You can specify the desired LLM provider and model using command-line flags `--llm-provider` and `--model`. The tool defaults to using the Gemini 2.0 Flash model with the `gemini` provider if none is explicitly specified.

## Usage

### Single Query

Run a single natural language query directly from the command line:

```bash
docker-ai "list all running containers"
```

The tool will display the generated Docker command and its output. Potentially destructive commands will require confirmation unless the `--quiet` flag is used.

### Interactive Mode

Enter interactive mode for a continuous conversational session:

```bash
docker-ai
```

The tool will display a prompt (e.g., `>>>`). You can type natural language queries and the tool will maintain conversational context.

**Special Commands in Interactive Mode:**

  * `reset`: Clears the conversational context.
  * `exit` or `quit`: Terminates the interactive shell.
  * `model`: Displays the currently selected LLM model.
  * `models`: Lists available models from the configured LLM provider.
  * `version`: Displays the `docker-ai` tool version.
  * `clear`: Clears the terminal screen.

### Command-Line Options

  * `--quiet`: Bypasses confirmation prompts for destructive commands.
  * `--llm-provider [PROVIDER]`: Specifies the LLM provider (e.g., `gemini`, `openai`, `ollama`).
  * `--model [MODEL]`: Specifies the LLM model (e.g., `gemini-2.0-flash`, `gpt-4o`, `gemma3`).
  * `--version`: Displays the tool version.
  * `--help`: Displays help information.

## Uninstallation

To uninstall the tool and its dependencies installed via pip, use the following command:

```bash
pip uninstall docker-ai
```

This will not affect your Docker installation or configuration.

## Error Handling



## Contributing

[CONTRIBUTING.md](CONTRIBUTING.md)

## License

[LICENSE](LICENSE)

## Disclaimer

