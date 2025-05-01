from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()  # .env 파일에서 환경변수 로드

    print("Hello LangChain")

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
    llm = ChatOllama(model="llama3")
    # llm = ChatOllama(model="mistral")

    chain = (
        summary_prompt_template | llm
    )  # | => 앞의 출력을 뒤로 넘겨줌 (=  summary_prompt_template 를 llm(언어모델) 에 넘겨줌)

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/eden-marco/"
    )
    res = chain.invoke(input={"information": linkedin_data})

    print(res)
