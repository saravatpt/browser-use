# Browser Automation with Google Gemini AI

This project demonstrates browser automation using Google's Gemini AI model through the LangChain framework. It allows you to perform automated web tasks using natural language instructions.

## Demo
[https://github.com/yourusername/browser-use-demo/raw/main/Browseruse-Demo.mp4](https://github.com/saravatpt/browser-use/blob/main/Browseruse-Demo.mp4)

## Features

- Automated web browsing using natural language instructions
- Integration with Google's Gemini AI model
- Environment variable support for API key management
- Asynchronous operation for better performance

## Prerequisites

- Python 3.8 or higher
- Google API key for Gemini AI
- Internet connection

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## Usage

1. Import and use the Agent class in your code:
```python
from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=your_api_key)

# Create an agent with your task
agent = Agent(
    task='Your task description here',
    llm=llm,
    max_actions_per_step=4,
)

# Run the agent
await agent.run(max_steps=25)
```

2. Example task:
```python
task = 'Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result'
```

## Configuration

- `max_actions_per_step`: Maximum number of actions the agent can perform in a single step
- `max_steps`: Maximum number of steps the agent can take to complete the task
- `model`: The Gemini AI model to use (default: 'gemini-2.0-flash-exp')

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
