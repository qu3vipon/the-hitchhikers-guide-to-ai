# Python 가상환경

Python에서는 다른 사람이 미리 작성해 둔 코드를 가져와 사용할 수 있습니다. 이렇게 가져다 쓰는 코드 묶음을 **라이브러리(library)**라고 합니다. 예를 들어 웹 서버를 만들 때는 FastAPI 같은 라이브러리를 설치해 다른 개발자들이 미리 만들어둔 기능을 간편하게 사용할 수 있습니다.

그런데 기본적으로 Python 라이브러리를 설치하면 컴퓨터 전체에서 사용하는 전역 Python에 설치됩니다. 전역 Python은 여러 프로젝트가 함께 쓰기 때문에, 프로젝트마다 필요한 라이브러리의 버전이 다르면 나중에 충돌할 수 있습니다.

그래서 Python에서는 전역 Python에 라이브러리를 직접 설치하기보다, 프로젝트마다 **가상환경(virtual environment)**을 만들어 사용합니다. 새 Python 프로젝트를 시작할 때 가상환경부터 만드는 것은 거의 표준적인 과정입니다.

## 가상환경 생성 {#create-virtual-environment}

Python에는 가상환경을 만드는 `venv` 모듈이 기본으로 포함되어 있습니다. 먼저 프로젝트 폴더를 만들고 그 안으로 이동한 뒤, `.venv`라는 이름의 가상환경을 만들어 보겠습니다.

=== "macOS"

    ```shell
    mkdir playground
    cd playground
    python3 -m venv .venv
    ```

=== "Windows PowerShell"

    ```powershell
    mkdir playground
    cd playground
    py -m venv .venv
    ```

마지막 명령어를 실행하면 현재 폴더 안에 `.venv` 폴더가 만들어집니다. 이 폴더에는 이 프로젝트만을 위한 Python과 라이브러리가 저장됩니다.

!!! info "가상환경 이름 짓기"
    가상환경 폴더는 `.venv`라고 이름 짓는 것이 널리 쓰이는 관례입니다. `venv`는 virtual environment의 줄임말입니다.

    이름 앞의 점(`.`)은 macOS와 Linux에서 폴더를 **숨김으로 표시**한다는 뜻입니다. 프로젝트의 주요 파일과 가상환경 폴더를 구분하기 쉬워서 `.venv`라는 이름을 자주 사용합니다. Windows에서는 점으로 시작해도 숨김 폴더가 되지는 않지만, 같은 이름을 사용해도 문제없습니다.

## 가상환경 활성화 {#activate-virtual-environment}

새로 만든 가상환경을 실제로 사용하려면 활성화해야 합니다. 활성화한 뒤 실행하는 `python`과 `pip` 명령어는 전역 Python이 아닌 `.venv` 안의 Python을 사용합니다.

=== "macOS"

    ```shell
    source .venv/bin/activate
    ```

=== "Windows PowerShell"

    ```powershell
    .venv\Scripts\Activate.ps1
    ```

활성화에 성공하면 터미널 프롬프트 앞에 `(.venv)`가 표시됩니다.

```console
(.venv) playground $
```

이제 이 터미널에서 Python을 실행하면 .venv 안에 마련된 독립된 Python 환경을 사용합니다. 이후 라이브러리를 추가하더라도 다른 프로젝트에는 영향을 주지 않습니다.

## 가상환경 비활성화 {#deactivate-virtual-environment}

가상환경 사용을 마치고 전역 Python으로 돌아가려면 운영체제와 관계없이 아래 명령어를 실행합니다.

```shell
deactivate
```

## :material-pencil: 실습 과제 {#exercises}

다음 문장이 맞으면 O, 틀리면 X를 선택하세요.

1. 새 Python 프로젝트를 시작할 때 가상환경부터 만드는 것은 일반적인 방법이다.
2. 가상환경을 활성화하면, 이후 실행하는 Python은 전역 Python을 사용한다.
3. `deactivate`를 실행하면 가상환경 사용을 끝낼 수 있다.

??? success "정답·해설"
    1. **O** — 프로젝트마다 가상환경을 만들면 라이브러리와 버전을 독립적으로 관리할 수 있습니다.
    2. **X** — 활성화한 뒤에는 `.venv` 안의 Python을 사용합니다.
    3. **O** — `deactivate`는 가상환경을 비활성화하고 전역 Python으로 돌아가는 명령어입니다.
