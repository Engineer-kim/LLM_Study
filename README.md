# 프로젝트 초기 설정
1.  **Python 설치:**
    * Python이 설치되어 있지 않다면 [Python 공식 홈페이지](https://www.python.org/downloads/)에서 다운로드하여 설치

2.  **환경 변수 설정:**
    * 아래 경로들을 시스템 환경 변수의 `Path`에 추가 (이미 설정되어 있다면 생략 가능)  => 중요!
        * `C:\Users\당신의 유저명\AppData\Local\Programs\Python\Python313\`
        * `C:\Users\당신의 유저명\AppData\Local\Programs\Python\Python313\Scripts\`
    * 명령 프롬프트 또는 PowerShell을 열어 다음 명령어로 Python 설치를 확인
    
    (단, 윈도우는 Python.exe 1개만 설치 되어 있을수 있음, 고로 복사해서 Python3.exe 만들면됨 => 필수 아님)
        
     ```
     python --version
     python3 --version
     ```
                
      **위의 두 명령어 모두 Python 버전을 정확하게 출력해야 함 ex) Python 3.13.3**



3.  **인터프리터 설정 (Idea의 PyCharm 기준):**
    * PyCharm 설정 (Settings) > 프로젝트 (Project) > Python 인터프리터 (Python Interpreter) 메뉴로 이동
    * **Pipenv 환경**을 선택하거나 추가
    * 기존 인터프리터를 사용한다면, 인터프리터 경로를 환경 변수에 설정된 Python Scripts 폴더 (`C:\Users\당신의 유저명\AppData\Local\Programs\Python\Python313\Scripts\`) 내의 `pipenv` 실행 파일로 지정합니다.
    * 새로운 Pipenv 환경을 생성할 수도 있음

**종속성 설치:**

해당 프로젝트는 아래의 종속성 설치및 사용함.(더 나은게 있으면, 설치후 마음대로 사용 ㄱㄱ)

```
pipenv install langchain-openai
pipenv install langchain-community
pipenv install langchainhub
pipenv install black
```
종속성 목록은 필요에 따라 향후 업데이트될 수 있음

4. 들여쓰기 자동화
  * pipenv install black 종속성 설치 <br>
   (C:\Users\hammo\AppData\Roaming\Python\Python313\Scripts 이 경로가 시스템 PATH 환경 변수에 정확하게 등록되있는지 확인)
  * 코드 작성후 ``` black . ```  입력 (뒤에 점까지 black 하고 한칸 띄고 작성해야함)