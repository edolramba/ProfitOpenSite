# ProfitOpenSite - Trading Bot Performance Report

자동 매매 봇의 성과를 시각화하는 Streamlit 웹 애플리케이션입니다.

## 📋 목차
- [프로젝트 소개](#프로젝트-소개)
- [VSCode IDE 설정](#vscode-ide-설정)
- [GitHub 계정 연결](#github-계정-연결)
- [개발 환경 설정](#개발-환경-설정)
- [실행 방법](#실행-방법)

## 프로젝트 소개

이 프로젝트는 MongoDB에서 추출한 자동 매매 거래 데이터를 분석하고 시각화하는 Streamlit 애플리케이션입니다.

### 주요 기능
- 📊 거래 내역 시각화
- 💰 누적 수익률 차트
- 📈 매매 성과 분석
- 📋 상세 거래 내역 테이블

## VSCode IDE 설정

### 1. VSCode 설치
1. [Visual Studio Code 공식 웹사이트](https://code.visualstudio.com/)에서 다운로드
2. 운영체제에 맞는 버전 설치

### 2. 필수 확장 프로그램 설치
VSCode에서 다음 확장 프로그램을 설치하세요:

```
- Python (Microsoft)
- Pylance (Microsoft)
- Python Debugger (Microsoft)
- GitLens (선택사항)
```

확장 프로그램 설치 방법:
1. VSCode 실행
2. 좌측 사이드바에서 확장 프로그램 아이콘 클릭 (Ctrl+Shift+X)
3. 검색창에서 "Python" 검색 후 설치

## GitHub 계정 연결

### Google 계정으로 GitHub Copilot 결제 후 VSCode 연결 방법

#### 1. GitHub 계정이 이미 있는 경우

1. **VSCode에서 GitHub 로그인**
   - VSCode 좌측 하단의 계정 아이콘 클릭
   - "GitHub로 로그인" 선택
   - 브라우저가 열리면 GitHub 계정으로 로그인
   - 인증 완료 후 VSCode로 돌아오기

2. **GitHub Copilot 활성화**
   - VSCode에서 `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`)
   - "GitHub Copilot: Sign In" 입력 후 실행
   - GitHub 로그인이 되어있다면 자동으로 활성화됨

3. **Copilot 상태 확인**
   - VSCode 우측 하단에 Copilot 아이콘이 표시되어야 함
   - 아이콘을 클릭하여 상태 확인 가능

#### 2. GitHub Copilot 구독 확인

1. [GitHub Copilot 구독 페이지](https://github.com/settings/copilot)에서 구독 상태 확인
2. Google 계정으로 결제했다면 GitHub 계정에 연결되어 있어야 함
3. 문제가 있다면 GitHub 설정 > Billing에서 결제 정보 확인

#### 3. 저장소 복제 (Clone)

```bash
# HTTPS 방식
git clone https://github.com/edolramba/ProfitOpenSite.git

# 또는 VSCode에서 직접:
# 1. Ctrl+Shift+P (Mac: Cmd+Shift+P)
# 2. "Git: Clone" 입력
# 3. 저장소 URL 입력
# 4. 저장할 폴더 선택
```

## 개발 환경 설정

### 1. Python 설치
- Python 3.8 이상 필요
- [Python 공식 웹사이트](https://www.python.org/downloads/)에서 다운로드

### 2. 가상 환경 생성 (권장)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

현재 프로젝트에서 사용하는 패키지:
- `streamlit` - 웹 애플리케이션 프레임워크
- `pandas` - 데이터 처리 및 분석
- `altair` - 데이터 시각화

### 4. MongoDB 설정 (선택사항)

로컬에서 데이터를 업데이트하려면 MongoDB가 필요합니다:

1. `.streamlit/secrets.toml` 파일 수정:
```toml
[mongo]
host = "your-mongodb-host"
port = 27017
username = "your-username"
password = "your-password"
db = "automatedTrading"
collection = "dj00Trading"
```

## 실행 방법

### 1. Streamlit 앱 실행

```bash
streamlit run streamlit_app.py
```

실행 후 자동으로 브라우저가 열리며 http://localhost:8501 에서 확인 가능합니다.

### 2. 데이터 업데이트 (Windows)

```bash
update_data_and_push.bat
```

이 스크립트는:
1. MongoDB에서 최신 거래 데이터를 추출
2. JSON 파일로 저장
3. Git에 자동으로 커밋 및 푸시

## 📁 프로젝트 구조

```
ProfitOpenSite/
├── .streamlit/
│   └── secrets.toml          # MongoDB 연결 정보 (개인 설정)
├── streamlit_app.py           # 메인 Streamlit 애플리케이션
├── requirements.txt           # Python 패키지 의존성
├── update_data_and_push.bat   # 데이터 업데이트 스크립트 (Windows)
├── *.json                     # 거래 데이터 (자동 생성)
└── README.md                  # 이 파일
```

## 🔧 문제 해결

### VSCode에서 Python을 찾을 수 없는 경우
1. `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`)
2. "Python: Select Interpreter" 입력
3. 설치된 Python 또는 가상환경의 Python 선택

### GitHub Copilot이 작동하지 않는 경우
1. GitHub Copilot 구독이 활성화되어 있는지 확인
2. VSCode를 재시작
3. GitHub에서 로그아웃 후 다시 로그인
4. 확장 프로그램 "GitHub Copilot" 재설치

### Streamlit 실행 시 포트 충돌
```bash
# 다른 포트로 실행
streamlit run streamlit_app.py --server.port 8502
```

## 📞 지원

문제가 발생하면 GitHub Issues에 등록해주세요.

## 📄 라이선스

이 프로젝트는 개인 프로젝트입니다.
