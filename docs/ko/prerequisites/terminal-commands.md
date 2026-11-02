# 터미널 기본 명령어

터미널에서 자주 사용되는 명령어를 배워봅시다.

## pwd: 현재 위치 확인하기 {#pwd}

터미널은 항상 특정 폴더 안에서 작업합니다. 먼저 현재 어느 폴더에 있는지 확인해 봅시다.

```shell
pwd
```

`pwd`는 **현재 작업 중인 폴더의 경로**를 보여 줍니다. `print working directory`의 줄임말입니다.

---

## ls / dir: 파일과 폴더 목록 보기 {#list-files}

현재 폴더 안에 있는 파일과 폴더를 확인할 때는 다음 명령어를 사용합니다.

=== "macOS"

    ```shell
    ls
    ```

=== "Windows PowerShell"

    ```powershell
    dir
    ```

`ls`와 `dir`은 **현재 폴더 안에 있는 파일과 폴더의 목록**을 보여 줍니다. `ls`는 list(목록), `dir`은 directory(디렉터리)의 줄임말입니다.

---

## mkdir: 폴더 만들기 {#make-directory}

`mkdir`로 `playground` 폴더를 만들어 봅시다.

```shell
mkdir playground
```

`mkdir`은 **새 폴더를 만드는 명령어**입니다. make directory(디렉터리 만들기)의 줄임말입니다.

---

## cd: 폴더 이동하기 {#change-directory}

`cd`로 방금 만든 `playground` 폴더 안으로 이동해 봅시다.

```shell
cd playground
```

`cd`는 **다른 폴더로 이동**하는 명령어입니다. change directory(디렉터리 변경)의 줄임말입니다. 명령어를 입력한 뒤 `pwd`를 실행하면 경로 끝에 `playground`가 표시됩니다.

상위 폴더로 돌아가고 싶을 때는 `..`을 사용합니다.

```shell
cd ..
```

---

## touch / ni: 파일 만들기 {#create-file}

현재 `playground` 폴더 안에서 `memo.txt` 파일을 만들어 봅시다.

=== "macOS"

    ```shell
    touch memo.txt
    ```

=== "Windows PowerShell"

    ```powershell
    ni memo.txt
    ```

`touch`는 파일이 없으면 **새 파일을 만들고, 이미 있으면 수정 시간을 갱신**합니다. 파일을 건드린다는 뜻에서 온 명령어입니다. `ni`는 **New-Item(새 항목 만들기)의 별칭**입니다.

마지막으로 `ls` 또는 `dir`을 실행하면 새로 만든 `memo.txt` 파일이 목록에 표시됩니다.

---

## rm / rmdir: 파일과 폴더 삭제하기 {#remove-files}

방금 만든 파일과 폴더를 삭제해 봅시다. 먼저 파일을 삭제하고, 상위 폴더로 이동한 뒤 빈 `playground` 폴더를 삭제합니다.

=== "macOS"

    ```shell
    rm memo.txt
    cd ..
    rmdir playground
    ```

=== "Windows PowerShell"

    ```powershell
    rm memo.txt
    cd ..
    rm playground
    ```

`rm`과 `rmdir`은 **파일과 폴더를 삭제**하는 명령어입니다. `rm`은 remove(제거), `rmdir`은 remove directory(디렉터리 제거)의 줄임말입니다. Windows PowerShell에서 `rm`은 Remove-Item의 별칭입니다. `rmdir`은 비어 있는 폴더만 삭제할 수 있습니다. 파일이 남아 있는 폴더를 한 번에 삭제하는 명령어도 있지만, 실수로 중요한 파일을 지울 수 있으므로 이 과정에서는 다루지 않습니다.

## :material-pencil: 실습 과제 {#exercises}

터미널에서 아래 순서대로 `playground` 폴더와 `note.txt` 파일을 만들었다가 삭제해 보세요.

1. `playground` 폴더를 만듭니다.
2. `playground` 폴더로 이동합니다.
3. `note.txt` 파일을 만듭니다.
4. 파일 목록에서 `note.txt`를 확인합니다.
5. `note.txt`와 `playground` 폴더를 차례로 삭제합니다.

??? success "정답·해설"
    먼저 공통 명령어로 폴더를 만들고 이동합니다.

    ```shell
    mkdir playground
    cd playground
    ```

    운영체제에 맞는 명령어로 파일을 만들고, 목록을 확인한 뒤 삭제합니다.

    === "macOS"

        ```shell
        touch note.txt
        ls
        rm note.txt
        ```

    === "Windows PowerShell"

        ```powershell
        ni note.txt
        dir
        rm note.txt
        ```

    상위 폴더로 돌아가는 명령어는 두 운영체제에서 같습니다.

    ```shell
    cd ..
    ```

    마지막으로 운영체제에 맞는 명령어로 빈 `playground` 폴더를 삭제합니다.

    === "macOS"

        ```shell
        rmdir playground
        ```

    === "Windows PowerShell"

        ```powershell
        rm playground
        ```

    파일과 폴더를 삭제한 뒤 `dir` 또는 `ls`로 목록을 확인해 보세요. `playground`가 더 이상 표시되지 않으면 성공입니다.
