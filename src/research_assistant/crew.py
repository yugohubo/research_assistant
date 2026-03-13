from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_files import File


from .tools.custom_tool import ddg_search_tool, scrape_website_tool, MarkdownToPDFTool
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators





@CrewBase
class ResearchAssistant():
    """ResearchAssistant crew"""

    agents: list[BaseAgent]
    tasks: list[Task]


    ollama_llm_planner = LLM(
        model="ollama/researcher",
        base_url="http://localhost:11434",
        temperature=0.7
    )

    ollama_llm_writing = LLM(
        model="ollama/researcher",
        base_url="http://localhost:11434",
        temperature=0.4
    )

    ollama_llm_thinking = LLM(
        model="ollama/researcher",
        base_url="http://localhost:11434"
    )
    ollama_llm_tool = LLM(
        model = "ollama/tool_nano",
        base_url = "http://localhost:11434"
    )

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    
    @agent
    def research_planner(self) -> Agent:
        return Agent(
            config = self.agents_config['research_planner'], #type: ignore[index]
            llm = self.ollama_llm_planner,
            verbose = True,
            inject_date = True
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            llm = self.ollama_llm_thinking,
            verbose=True,
            tools=[ddg_search_tool, scrape_website_tool],
            max_iter = 1
        )

    @agent
    def fact_checker(self) -> Agent:
        return Agent(
            config = self.agents_config['fact_checker'], #type: ignore[index]
            llm = self.ollama_llm_thinking,
            verbose = True,
            tools=[ddg_search_tool, scrape_website_tool],
            max_iter = 1
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
            llm = self.ollama_llm_writing,
            verbose=True,
            max_iter = 1,
            inject_date=True,
        )
 
    @agent
    def converter(self) -> Agent:
        return Agent(
            config=self.agents_config['converter'], # type: ignore[index]
            llm = self.ollama_llm_tool,
            verbose=True,
            max_iter = 1,
            tools=[MarkdownToPDFTool]
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    
    @task
    def create_research_plan_task(self) ->Task:
        return Task(
            config=self.tasks_config['create_research_plan_task'], #type: ignore[index]
        )


    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
            context=[self.create_research_plan_task()]  # type: ignore[index]
        )
    
    @task
    def verify_information_quality_task(self) -> Task:
        return Task(
            config=self.tasks_config['verify_information_quality_task'], #type: ignore[index]
        )
    
    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], # type: ignore[index]
            context=[self.verify_information_quality_task(), self.create_research_plan_task()], # type: ignore[index]
            output_file='report.md'
        )
    
    @task
    def convert_pdf_task(self) -> Task:
        return Task(
            config=self.tasks_config['convert_pdf_task'], # type: ignore[index]
            context= [], #type: ignore
            tools=[MarkdownToPDFTool]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ResearchAssistant crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            output_log_file='crew_log.txt',
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
