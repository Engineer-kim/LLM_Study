from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from typing import Tuple

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
from output_parser import Summary


def ice_break_with(name: str) -> Tuple[Summary, str]:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    # 1, 2번은 => 명령어처럼 생기지 않아도 GPT는 그것을 요청으로 인식하고 응답
    summary_template = """ 
       given the Linkedin information {information}  about a person I want you to create:
       1. A short summary
       2. two interesting facts about them
       """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(
    #   temperature=0, model_name="gpt-3.5-turbo"
    # )  # temperature => 텍스트의 무작위성을 조절하는 값(=>수치가 1에 가까울수록 창의적 , 부정확해짐)

    # llm => 객체임
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    # llm = ChatOllama(model="mistral")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    # :Summary  => 메서드가 반환할 것으로 예상되는 데이터의 형태(타입 힌트)
    res:Summary = chain.invoke(input={"information": linkedin_data})

    return res, linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    load_dotenv()  # .env 파일에서 환경변수 로드

    print("Ice Breaker")
    ice_break_with(name="Eden Marco Udemy")
