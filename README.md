
# 🚀 Research Assistant Crew (Local AI Powered)

This project is an autonomous AI research assistant that researches any topic specified by the user online, verifies the data obtained (fact-checking), and presents the results as a detailed report in both **Markdown (.md)** and **PDF (.pdf)** formats.

It is developed entirely using **CrewAI** infrastructure and local **Ollama** models. This allows for in-depth research without external API costs, while protecting data privacy.

## ✨ Solution Offered

In traditional research, gathering information, verifying the accuracy of sources, and transforming this into a proper report can take hours. This system:
1. Dynamically receives a research topic (input).
2. Breaks down the topic into subtopics and creates a research plan.
3. Extracts up-to-date data from the internet using **DuckDuckGo** and **Web Scraping** tools.
4. Filters out potential hallucinations and misinformation from the collected data. 5. It first creates a `report.md` file by citing the relevant sources (citations), and then automatically converts it to a `report.pdf` file.

## 🤖 Our Crew (Agents)

The system works by 5 different AI agents with specific roles collaborating sequentially:

* **🧠 Research Planner:** Analyzes the user's query, breaks it down into subheadings, and creates a roadmap with clear, specific goals for the research team.
* **🔎 Internet Researcher:** Conducts in-depth searches using search engine tools (DuckDuckGo) on the internet according to the plan. Identifies the most up-to-date and reliable sources.
* **🛡️ Fact Checker:** Cross-checks the raw data provided by the researcher. It identifies inconsistencies, misinformation, or hallucinations, ensuring the quality of the report. * **📝 Reporting Analyst:** It takes verified data, synthesizes the information, and writes a well-structured, fluent Markdown (`report.md`) report that also includes citations.
* **📄 File Converter:** It comes into play in the final step, reads the written Markdown report, and converts it into a presentation-ready `report.pdf` file for the user.

## 🛠️ Setup and Usage (How-to Guide)
### Prerequisites

1. Your computer must have **Python 3.10+** installed.
2. For local LLM usage, [Ollama](https://ollama.com/) must be installed and running.
3. The project references specific Ollama models (`ollama/researcher`, `ollama/tool_nano`) in the configuration files (`crew.py`). These specific models are created with ModelFiles you can create these models by running the "ollama create tool_nano -f ./ModelFile" in the terminal of the ModelFile's location. You have to do this with the given ModelFiles for each model to run it effectively or you can use your own models or cloud if you so choose.

### 1. Clone the Project

```bash
git clone [https://github.com/yugohubo/research_assistant.git](https://github.com/yugohubo/research_assistant.git)
cd research_assistant

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/research_assistant/config/agents.yaml` to define your agents
- Modify `src/research_assistant/config/tasks.yaml` to define your tasks
- Modify `src/research_assistant/crew.py` to add your own logic, tools and specific args
- Modify `src/research_assistant/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the research-assistant Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The research-assistant Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the ResearchAssistant Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
