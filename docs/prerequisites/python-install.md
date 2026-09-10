# Python 설치

Python 코드를 실행하기 위해서는 사람이 작성한 Python 코드를 읽고 실행하는 **Python 인터프리터(Interpreter)**가 컴퓨터에 설치되어 있어야 합니다.

## Python 설치하기 {#install-python}

[Python 공식 다운로드 페이지](https://www.python.org/downloads/)에서 사용하는 운영체제에 맞는 Python 3 설치 방법을 선택하세요. 가장 최신 **Bugfix release**를 설치합니다.

| 상태 | 의미 |
| --- | --- |
| Pre-release | 다음 버전을 미리 시험하는 alpha·beta·release candidate 버전입니다. |
| Bugfix release | 안정화된 버전에 오류 수정과 보안 개선을 반영한 버전입니다. |
| Security release | 새 기능이나 일반 오류 수정 없이 보안 문제만 수정하는 오래된 버전입니다. |
| End-of-life | 더 이상 지원이나 보안 업데이트를 제공하지 않는 버전입니다. |


### macOS

1. [macOS용 Python 다운로드 페이지](https://www.python.org/downloads/macos/)에서 최신 안정 버전의 macOS installer를 내려받습니다.
2. 내려받은 `.pkg` 파일을 열고 설치 프로그램의 안내에 따라 설치합니다.
3. 터미널을 열고 아래 명령어로 설치를 확인합니다.

    ```shell
    python3 --version
    ```

### Windows

1. [Windows용 Python 다운로드 페이지](https://www.python.org/downloads/windows/)에서 **Python Install Manager**를 내려받아 설치합니다.
2. PowerShell을 열고 아래 명령어를 실행해 최신 Python 3 버전을 설치합니다.

    ```powershell
    py install 3
    ```

3. 설치가 끝나면 아래 명령어로 설치를 확인합니다.

    ```powershell
    python --version
    ```

## Python 설치 위치 {#python-location}

Python을 설치하면 인터프리터는 컴퓨터의 정해진 위치에 저장됩니다. 터미널에서 `python` 또는 `python3`를 입력하면 운영체제는 미리 등록된 경로에서 Python 인터프리터를 찾아 실행합니다.

이렇게 컴퓨터 전체에서 사용할 수 있도록 설치한 Python을 **전역 Python(Global Python)**이라고 부릅니다. 전역 Python은 어느 폴더에서든 실행할 수 있습니다.

터미널에서 아래 명령어를 실행하면 Python 실행 위치를 확인할 수 있습니다. 설치 방식과 사용자 이름에 따라 경로는 달라질 수 있습니다.

=== "macOS"

    ```console
    $ which python3
    /Library/Frameworks/Python.framework/Versions/3.14/bin/python3
    ```

=== "Windows"

    ```console
    PS> where.exe python
    C:\Users\사용자이름\AppData\Local\Microsoft\WindowsApps\python.exe
    ```

## Python 버전 {#python-version}

Python 버전은 `Python 3.14.0`처럼 세 개의 숫자로 표시합니다.

| 구분 | 예시 | 의미 |
| --- | --- | --- |
| 메이저 버전 | `3` | 큰 변화가 포함되는 버전입니다. 현재는 Python 3를 사용합니다. |
| 마이너 버전 | `14` | 새 기능과 개선 사항이 추가되는 버전입니다. |
| 패치 버전 | `0` | 오류 수정과 보안 개선이 포함되는 버전입니다. |

같은 Python 3라도 마이너 버전에 따라 사용할 수 있는 기능이나 라이브러리의 지원 여부가 달라질 수 있습니다. 프로젝트에서 특정 Python 버전을 안내한다면 그 버전을 사용해야 하며, 별도 안내가 없다면 최신 안정 버전의 Python을 사용하면 됩니다.

## :material-pencil: 실습 과제 {#exercises}

다음 문장이 맞으면 O, 틀리면 X를 선택하세요.

1. Python을 설치한다는 것은 Python 코드를 실행하는 인터프리터를 설치하는 일이다.
2. 전역 Python에 설치한 라이브러리는 여러 프로젝트에 영향을 줄 수 있다.
3. `Python 3.13.1`에서 `13`은 메이저 버전 번호다.

??? success "정답·해설"
    1. **O** — Python 인터프리터가 작성한 Python 코드를 읽고 실행합니다.
    2. **O** — 전역 Python은 여러 프로젝트가 함께 사용하므로, 라이브러리 버전이 서로 충돌할 수 있습니다.
    3. **X** — `3`이 메이저 버전이고, `13`은 마이너 버전, `1`은 패치 버전입니다.
