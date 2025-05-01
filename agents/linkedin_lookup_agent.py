from dotenv import load_dotenv

from tools.tools import get_profile_url

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Tool: 검색 엔진, 계산기, 데이터베이스 쿼리 등을 Tool로 만들어 Agent가 활용할 수 있게 함
from langchain_core.tools import Tool

from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)

# AgentExecutor : Agent 런타임

from langchain import hub


def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini",
    )
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                          Your answer should contain only a URL"""

    prompt_template = PromptTemplate(
        template=template,
        input_variables=["name_of_person"],
    )
    tool_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile  page",
            func=get_profile_url,  # func 는 None , 아니면 호출 가능한 함수명을 넣어야함
            description="useful for looking up a person on Linkedin",  # 중요함!, 이유:LLM입장에서 이 도구를 사용할지 말지를 결정하는 기준이기 때문
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent( # <- 최종 Agent(AI 비서)
        llm=llm, tool=tool_for_agent, prompt=react_prompt
    )
    agent_executor = AgentExecutor(agent=agent, tools=tool_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format(name_of_person=name)}
    )

    linked_profile_url = result["output"]
    return linked_profile_url


if __name__ == "__main__":
    linkedin_url = lookup(name="Eden Marco")
    print(linkedin_url)
