# Playwright for Python


### Installation

```bash
python(python3), pip(pip3)가 설치되어 있는지 확인

python3 --version

pip3 --version

입력시, 현재 로컬에 설치된 각 버전을 보여줘야함, 아닌 경우 설치해주기
```

```bash
설치가 다 끝나면, 필요 패키지를 설치해야함

pip3 install pytest-playwright

playwright install
```

설치 다 끝나면, 이제 프로젝트 루트 경로에서 파일 하나를 만듦 `test_my_application.py`

```bash
테스트 실행시 아래와 같이 입력

pytest

만약, 디버깅을 하고 싶으면
PWDEBUG=1 pytest -s
이렇게 커맨드를 쓰면 Playwright Inspector가 띄워진다. 이걸로 Debugging할 수 있음

만약, 파일이 여러개고 특정 파일을 실행하려면 
pytest filename.py

만약, 여러 test file을 실행하려면
pytest tests/todo-page/ tests/landing-page/

만약, 특정 function name을 테스트 하려면
pytest -k "function name"

만약, 브라우저를 띄우는게 보여지게 하려면
pytest --headed filename.py

만약, 브라우저를 여러개로 테스트 하려면
pytest --headed filename.py --browser firefox --browser webkit

만약, 실패한 테스트에 한해서만 스크린샷 캡쳐를 하고 싶다면,
--screenshot only-on-failure 옵션을 추가
```

### pytest.fixture

- browser context의 특성상 모든 각 테스트들마다 페이지(page)는 isolated environment이다.
그래서 한 개의 브라우저에서만 여러개의 테스트를 돌려도 이 제약은 모두 동일한데 이를 위해 fixture라는 녀석이 있음
얘는 context를 제공해주는 녀석인데 beforeEach, afterEach, beforeAll, afterAll 같은 기능을한다.
즉, beforeEach는 각 Test function을 실행하기 전 실행되는 녀석이 된다고 보면 된다.

```python
@pytest.fixture(scope="function", autouse=True)
# 이렇게 작성하게 되면, scope가 function이라 beforeEach / afterEach와 같은 역할을하고,

@pytest.fixture(scope="module", autouse=True)
# 이렇게 작성하게 되면 beforeAll, afterAll같은 역할을 한다고 보면 된다.

```

### Test Generator

- 쉽게 생각하면 Recording and Playback 방식이다.
```bash
playwright codegen "테스트 할 웹 브라우저 URL"

이렇게 입력하면, 해당 URL로 이동된 브라우저 하나랑 나의 액션 하나하나에 반응하는 Debugger가 뜨는데, Recoding and Playback 방식을 사용할 수 있다.
```

