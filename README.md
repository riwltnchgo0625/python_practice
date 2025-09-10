# Python Practice – Selenium & Pytest 중심 학습 저장소

이 저장소는 Python을 활용한 **소프트웨어 테스팅 자동화 학습 기록**입니다.  
특히 **Selenium WebDriver**와 **Pytest**를 활용한 웹 UI 자동화 및 단위 테스트 중심으로 구성되어 있습니다.  
QA 직무 포트폴리오 증빙을 위해 실습 코드, 테스트 케이스, 실행 결과를 정리합니다.

---

## 📂 저장소 구조

- **/selenium/**  
  - 웹사이트 자동화 스크립트 (로그인, 폼 입력, 버튼 클릭 등)  
  - WebDriver 제어 및 DOM 탐색 실습  

- **/pytest/**  
  - 단위 테스트 및 기능 테스트 예제  
  - Selenium 코드와 연계한 자동화 테스트 케이스  

- **/basics/**  
  - Python 기초 문법 복습 (조건문, 반복문, 함수, 클래스)  

- **/screenshots/**  
  - 실행된 자동화 테스트 결과 화면 캡처  

---

## 🛠 사용 기술 및 도구

- **언어**: Python 3.x  
- **프레임워크**: Pytest  
- **자동화 도구**: Selenium WebDriver (ChromeDriver)  
- **IDE**: VS Code / PyCharm  
- **환경 관리**: pip, venv  

---

## 🔑 주요 학습 내용

1. **Selenium 웹 UI 자동화**
   - `find_element(By.ID / NAME / XPATH)`로 DOM 요소 탐색
   - 로그인 폼 자동 입력 및 버튼 클릭
   - Explicit/Implicit Wait 활용

2. **Pytest 기반 테스트**
   - `@pytest.mark.parametrize` 로 데이터 기반 테스트
   - `setup_method`, `teardown_method` 로 환경 초기화
   - Selenium 스크립트를 Pytest로 실행

3. **테스트 케이스 예시**

| 테스트 항목 | 입력 데이터 | 예상 결과 | 비고 |
|-------------|------------|-----------|------|
| 로그인 성공 | ID=tomsmith, PW=SuperSecretPassword! | 로그인 성공 메시지 출력 | 정상 케이스 |
| 로그인 실패 | ID=wrong, PW=wrong | 오류 메시지 출력 | 경계값/예외 케이스 |
| 입력값 공백 | ID="", PW="" | 필수 입력 오류 발생 | 유효성 검증 |

---

## 🚀 실행 방법

1. 저장소 클론  
   ```bash
   git clone https://github.com/riwltnchgo0625/python_practice.git
   cd python_practice

## 🍎bash 명령어
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install -r requirements.txt

