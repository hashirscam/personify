from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage


@CrewBase
class Personify():
    """Personal Statement Writer Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def personality_interviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['personality_interviewer'],
            tools=[SerperDevTool()],
            verbose=True,
            memory=True
        )

    @agent
    def technical_interviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_interviewer'],
            tools=[SerperDevTool()],
            verbose=True,
            memory=True
        )

    @agent
    def best_statement_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['best_statement_researcher'],
            tools=[SerperDevTool()],
            verbose=True,
            memory=True
        )

    @agent
    def university_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['university_researcher'],
            tools=[SerperDevTool()],
            verbose=True,
            memory=True
        )

    @agent
    def statement_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['statement_writer'],
            verbose=True,
            memory=True
        )

    @agent
    def evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['evaluator'],
            verbose=True,
            memory=True
        )

    @task
    def conduct_personality_interview(self) -> Task:
        return Task(
            config=self.tasks_config['conduct_personality_interview'],
        )

    @task
    def conduct_technical_interview(self) -> Task:
        return Task(
            config=self.tasks_config['conduct_technical_interview'],
        )

    @task
    def research_best_statements(self) -> Task:
        return Task(
            config=self.tasks_config['research_best_statements'],
        )

    @task
    def research_university(self) -> Task:
        return Task(
            config=self.tasks_config['research_university'],
        )

    @task
    def write_personal_statement(self) -> Task:
        return Task(
            config=self.tasks_config['write_personal_statement'],
        )

    @task
    def evaluate_statement(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_statement'],
        )

    @task
    def improve_statement(self) -> Task:
        return Task(
            config=self.tasks_config['improve_statement'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Personal Statement Writer crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
            memory=True,
            # Long-term memory for persistent storage across sessions
            long_term_memory = LongTermMemory(
                storage=LTMSQLiteStorage(
                    db_path="./memory/long_term_memory_storage.db"
                )
            ),
            # Short-term memory for current context using RAG
            short_term_memory = ShortTermMemory(
                storage = RAGStorage(
                        embedder_config={
                            "provider": "openai",
                            "config": {
                                "model": 'text-embedding-3-small'
                            }
                        },
                        type="short_term",
                        path="./memory/"
                    )
                ),            # Entity memory for tracking key information about entities
            entity_memory = EntityMemory(
                storage=RAGStorage(
                    embedder_config={
                        "provider": "openai",
                        "config": {
                            "model": 'text-embedding-3-small'
                        }
                    },
                    type="short_term",
                    path="./memory/"
                )
            ),
        )

