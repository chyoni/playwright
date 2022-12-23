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

설치 다 끝나면, 이제 프로젝트 루트 경로에서 파일 하나를 만듬 `test_my_application.py`

```bash
테스트 실행시 아래와 같이 입력

pytest

만약, 파일이 여러개고 특정 파일을 실행하려면 
pytest filename.py

만약, 브라우저를 띄우는게 보여지게 하려면
pytest --headed filename.py

만약, 브라우저를 여러개로 테스트 하려면
pytest --headed filename.py --browser firefox --browser webkit
```


