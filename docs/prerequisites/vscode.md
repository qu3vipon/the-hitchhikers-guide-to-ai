# VS Code

프로그래밍을 할 때는 코드를 작성하고, 파일을 관리하고, 실행 결과와 오류를 확인할 수 있는 전용 개발 도구를 사용합니다. 이런 도구를 **IDE(Integrated Development Environment, 통합 개발 환경)** 또는 코드 편집기라고 부릅니다.

여러 개발 도구가 있지만 이 과정에서는 Microsoft에서 만들고 무료로 사용할 수 있는 **Visual Studio Code**, 줄여서 **VS Code**를 사용합니다. VS Code는 가볍게 시작할 수 있는 코드 편집기이며, 필요한 기능을 확장으로 추가하면 Python 개발에 필요한 도구를 한곳에서 사용할 수 있습니다.

## VS Code 설치하기 {#install-vscode}

[VS Code 공식 다운로드 페이지](https://code.visualstudio.com/download)에 접속한 뒤, 사용하는 운영체제에 맞는 설치 파일을 내려받으세요.

### macOS

1. 다운로드 페이지에서 macOS용 `.dmg` 파일을 내려받습니다.
2. 내려받은 `.dmg` 파일을 열고, `Visual Studio Code.app`을 `Applications` 폴더로 드래그합니다.
3. `Applications` 폴더 또는 Spotlight에서 Visual Studio Code를 실행합니다.

### Windows

1. 다운로드 페이지에서 Windows용 **User Installer** 설치 파일을 내려받습니다.
2. 내려받은 `.exe` 파일을 실행합니다.
3. 설치 프로그램의 안내에 따라 설치를 마치고 Visual Studio Code를 실행합니다.

## Python 확장 설치하기 {#install-python-extension}

VS Code는 **확장(Extension) 프로그램**을 설치해 언어별 기능을 추가할 수 있습니다. Python 확장을 설치하면 코드 자동 완성, 오류 확인, 디버깅처럼 Python 개발에 필요한 기능을 사용할 수 있습니다.

1. VS Code 왼쪽의 **Extensions** 아이콘을 선택합니다.

    - macOS에서는 `Command` + `Shift` + `X`를 눌러 열 수도 있습니다.
    - Windows와 Linux에서는 `Ctrl` + `Shift` + `X`를 누릅니다.

2. 검색창에 `Python`을 입력합니다.
3. 게시자가 **Microsoft**인 `Python` 확장을 선택합니다.
4. **Install** 버튼을 선택합니다.

!!! info "Python 확장과 Python은 다릅니다"
    Python 확장은 VS Code에 Python 개발 기능을 추가하는 도구입니다. Python 코드를 실제로 실행하려면 컴퓨터에 Python도 별도로 설치되어 있어야 합니다. 설치 방법은 [Python 설치](python-install.md)에서 자세히 다룹니다.

## :material-pencil: 실습 과제 {#exercises}

다음 문장이 맞으면 O, 틀리면 X를 선택하세요.

1. VS Code는 Microsoft에서 만들고 무료로 사용할 수 있는 코드 편집기다.
2. VS Code의 Python 확장을 설치하면 Python 자체도 자동으로 설치된다.
3. Python 확장은 코드 자동 완성과 디버깅 같은 Python 개발 기능을 추가한다.

??? success "정답·해설"
    1. **O** — 이 과정에서는 무료로 사용할 수 있는 VS Code를 개발 도구로 사용합니다.
    2. **X** — Python 확장은 VS Code의 기능을 추가합니다. Python 실행 환경은 별도로 설치해야 합니다.
    3. **O** — Python 확장은 자동 완성, 오류 확인, 디버깅 같은 기능을 제공합니다.
