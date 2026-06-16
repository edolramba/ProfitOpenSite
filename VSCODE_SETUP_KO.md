# VSCode IDE 도구 연결 가이드

## Google 계정으로 결제한 GitHub Copilot을 VSCode에 연결하는 방법

이 가이드는 Google 계정으로 GitHub Copilot을 결제한 후, VSCode IDE에서 사용하는 방법을 단계별로 설명합니다.

---

## 🚀 빠른 시작 가이드

### 1단계: VSCode 설치 및 기본 설정

#### VSCode 설치
1. https://code.visualstudio.com/ 접속
2. 운영체제에 맞는 버전 다운로드 및 설치
3. VSCode 실행

#### 필수 확장 프로그램 설치
VSCode 좌측 사이드바에서 확장 프로그램 아이콘(□ 모양) 클릭 또는 `Ctrl+Shift+X` 단축키

다음 확장 프로그램들을 검색하여 설치:
- **Python** (Microsoft 제작) - 필수
- **Pylance** (Microsoft 제작) - 필수
- **GitHub Copilot** - 필수 (AI 코딩 도우미)
- **GitHub Copilot Chat** - 권장 (AI 채팅 기능)

---

### 2단계: GitHub 계정 연결

#### GitHub에 로그인
1. VSCode 좌측 하단의 **사람 모양 아이콘** 클릭
2. "GitHub로 로그인(Sign in with GitHub)" 선택
3. 웹브라우저가 자동으로 열림
4. GitHub 계정으로 로그인
   - Google 계정으로 GitHub에 가입했다면, "Sign in with Google" 선택
5. VSCode 접근 권한 승인
6. 브라우저에서 "성공(Success)" 메시지 확인 후 VSCode로 돌아오기

---

### 3단계: GitHub Copilot 활성화

#### Copilot 로그인
1. VSCode에서 `Ctrl+Shift+P` 눌러 명령 팔레트 열기
   - Mac: `Cmd+Shift+P`
2. "GitHub Copilot: Sign In" 입력 후 엔터
3. 이미 GitHub에 로그인했다면 자동으로 연결됨

#### Copilot 작동 확인
- VSCode 우측 하단에 **Copilot 아이콘** (✓ 모양) 확인
- 아이콘이 보이고 체크 표시가 있으면 정상 작동 중
- 아이콘 클릭하면 상태 확인 가능

---

### 4단계: 구독 상태 확인 (문제 발생 시)

#### GitHub 웹사이트에서 확인
1. https://github.com/settings/copilot 접속
2. 구독 상태(Subscription) 확인
   - "Active" 상태여야 함
3. 결제 정보 확인: https://github.com/settings/billing
   - Google Pay를 통한 결제 내역 확인

#### 구독이 활성화되지 않은 경우
1. GitHub에서 로그아웃 후 다시 로그인 시도
2. Google 계정으로 로그인했는지 확인
3. 결제가 제대로 처리되었는지 Google Pay 내역 확인

---

## 💻 이 프로젝트에서 작업하기

### 프로젝트 복제 (Clone)

#### 방법 1: VSCode에서 직접 복제
1. VSCode에서 `Ctrl+Shift+P` 누르기
2. "Git: Clone" 입력 후 엔터
3. 저장소 URL 입력: `https://github.com/edolramba/ProfitOpenSite.git`
4. 저장할 폴더 선택
5. 복제 완료 후 "폴더 열기" 클릭

#### 방법 2: 터미널에서 복제
```bash
git clone https://github.com/edolramba/ProfitOpenSite.git
cd ProfitOpenSite
code .
```

### Python 가상 환경 설정

#### Windows
```bash
# VSCode 터미널 열기 (Ctrl+`)
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### Mac/Linux
```bash
# VSCode 터미널 열기 (Ctrl+`)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Streamlit 앱 실행

#### VSCode 터미널에서 실행
```bash
streamlit run streamlit_app.py
```

실행 후 http://localhost:8501 에서 앱을 확인할 수 있습니다.

#### VSCode 디버거로 실행
1. VSCode 좌측의 "실행 및 디버그" 아이콘 클릭 (▷ 모양)
2. "Python: Streamlit" 선택
3. F5 키를 눌러 디버그 모드로 실행

---

## 🔧 자주 묻는 질문 (FAQ)

### Q1: "GitHub Copilot이 작동하지 않아요"

**해결 방법:**
1. VSCode 우측 하단 Copilot 아이콘 클릭
2. "Check Status" 선택하여 오류 메시지 확인
3. GitHub에서 로그아웃 후 다시 로그인
   ```
   Ctrl+Shift+P → "GitHub: Sign Out"
   Ctrl+Shift+P → "GitHub: Sign In"
   ```
4. VSCode 재시작
5. GitHub Copilot 확장 프로그램 재설치

### Q2: "Python 인터프리터를 찾을 수 없어요"

**해결 방법:**
1. `Ctrl+Shift+P` 누르기
2. "Python: Select Interpreter" 입력
3. 가상환경(venv) 또는 설치된 Python 선택
4. 선택 후 VSCode 우측 하단에 Python 버전 표시 확인

### Q3: "Google 계정으로 결제했는데 GitHub 계정과 연결이 안 돼요"

**해결 방법:**
1. GitHub에 Google 계정으로 로그인되어 있는지 확인
2. https://github.com/settings/billing 에서 결제 수단 확인
3. GitHub Copilot 구독이 해당 GitHub 계정에 연결되어 있는지 확인
4. 필요시 GitHub 고객 지원에 문의

### Q4: "포트 8501이 이미 사용 중이에요"

**해결 방법:**
```bash
# 다른 포트 사용
streamlit run streamlit_app.py --server.port 8502
```

### Q5: "가상 환경이 활성화되지 않아요"

**해결 방법 (Windows):**
PowerShell 실행 정책 변경 필요
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📚 추가 리소스

### VSCode 단축키 (필수)
- `Ctrl+Shift+P`: 명령 팔레트 열기
- `Ctrl+\``: 터미널 열기/닫기
- `Ctrl+B`: 사이드바 토글
- `Ctrl+P`: 파일 빠른 열기
- `F5`: 디버그 시작
- `Ctrl+F5`: 디버그 없이 실행

### GitHub Copilot 사용법
- **자동 완성**: 코드 입력 중 자동으로 제안
- **Tab 키**: 제안 수락
- **Esc 키**: 제안 무시
- **Alt+\**: 다음 제안 보기
- **Copilot Chat**: `Ctrl+Shift+I` (채팅창에서 AI에게 질문)

### 도움이 되는 링크
- [VSCode 공식 문서](https://code.visualstudio.com/docs)
- [GitHub Copilot 문서](https://docs.github.com/en/copilot)
- [Streamlit 문서](https://docs.streamlit.io/)
- [Python 가상환경 가이드](https://docs.python.org/ko/3/tutorial/venv.html)

---

## ✅ 설정 완료 체크리스트

다음 항목들을 모두 확인하세요:

- [ ] VSCode가 설치되어 있다
- [ ] Python 확장 프로그램이 설치되어 있다
- [ ] GitHub Copilot 확장 프로그램이 설치되어 있다
- [ ] GitHub 계정에 로그인되어 있다
- [ ] VSCode 우측 하단에 Copilot 아이콘이 표시된다
- [ ] 프로젝트를 복제(clone)했다
- [ ] Python 가상환경을 생성하고 활성화했다
- [ ] `pip install -r requirements.txt`를 실행했다
- [ ] `streamlit run streamlit_app.py`가 정상 실행된다

모든 항목을 체크했다면 개발 환경 설정이 완료되었습니다! 🎉

---

## 📞 문제가 계속되나요?

여전히 문제가 해결되지 않는다면:
1. [GitHub Issues](https://github.com/edolramba/ProfitOpenSite/issues)에 문제 등록
2. 오류 메시지 스크린샷 첨부
3. 운영체제 및 Python 버전 명시

도움이 필요하면 언제든지 질문해주세요!
