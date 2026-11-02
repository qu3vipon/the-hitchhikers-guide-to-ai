# Basic terminal commands

Let’s learn the commands you will use most often in the terminal.

## pwd: check your current location {#pwd}

The terminal always works in a particular folder. First, find out which folder you are in.

```shell
pwd
```

`pwd` stands for **print working directory**. It displays the path of your current folder.

---

## ls / dir: list files and folders {#list-files}

Use the following command to see what is in the current folder.

=== "macOS"

    ```shell
    ls
    ```

=== "Windows PowerShell"

    ```powershell
    dir
    ```

`ls` and `dir` **list the files and folders in the current directory**. The names are short for “list” and “directory.”

---

## mkdir: create a folder {#make-directory}

Create a folder named `playground`.

```shell
mkdir playground
```

`mkdir` stands for **make directory**: it creates a new folder.

---

## cd: change folders {#change-directory}

Move into the `playground` folder you just created.

```shell
cd playground
```

`cd` stands for **change directory**. Run `pwd` afterward and you should see `playground` at the end of the path.

Use `..` to return to the parent folder.

```shell
cd ..
```

---

## touch / ni: create a file {#create-file}

Move back into `playground` with `cd playground`, then create a file named `memo.txt`.

=== "macOS"

    ```shell
    touch memo.txt
    ```

=== "Windows PowerShell"

    ```powershell
    ni memo.txt
    ```

`touch` **creates the file if it does not exist, or updates its modification time if it does**. In PowerShell, `ni` is an alias for **New-Item**.

Run `ls` or `dir` to check that `memo.txt` appears in the list.

---

## rm / rmdir: delete files and folders {#remove-files}

Delete the file you just created, move to the parent folder, then delete the empty `playground` folder.

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

`rm` means **remove**, and `rmdir` means **remove directory**. In PowerShell, `rm` is an alias for `Remove-Item`. On macOS, `rmdir` removes only empty folders. Commands also exist for deleting folders together with their contents, but we will leave those aside here to avoid accidentally deleting important files.

## :material-pencil: Exercises {#exercises}

Use the terminal to create and then delete a `playground` folder and a `note.txt` file in this order.

1. Create a folder named `playground`.
2. Move into `playground`.
3. Create `note.txt`.
4. Check that `note.txt` appears in the file list.
5. Delete `note.txt`, then delete the `playground` folder.

??? success "Answer and explanation"
    Create and enter the folder using commands that work on both operating systems.

    ```shell
    mkdir playground
    cd playground
    ```

    Use the commands for your operating system to create the file, list it, and delete it.

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

    Return to the parent folder. This command is the same on both systems.

    ```shell
    cd ..
    ```

    Finally, delete the empty `playground` folder.

    === "macOS"

        ```shell
        rmdir playground
        ```

    === "Windows PowerShell"

        ```powershell
        rm playground
        ```

    Run `ls` or `dir` again. If `playground` is no longer listed, you have completed the exercise.
