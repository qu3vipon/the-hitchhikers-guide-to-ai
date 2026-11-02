# Terminal

A terminal is **a program that lets you control your computer by typing commands**. You can create and move files and folders, run programs, install development tools, and much more.

Instead of clicking icons and menus with a mouse, you tell the computer what to do by entering a command. We will use the terminal frequently to set up Python and run our programs.

<img src="../assets/images/prerequisites/01-terminal.png" alt="A terminal showing commands and a list of files" class="terminal-image">

!!! info "CLI and GUI"
    A **command-line interface (CLI)** lets you interact with a computer through typed commands. You enter a command, and the computer runs it and displays the result.

    A **graphical user interface (GUI)** lets you interact through visual elements such as icons, windows, menus, and buttons. This is how you normally use apps and web browsers.

## Why use the terminal? {#why-use-terminal}

The terminal makes many tasks quick and precise. Creating several files, starting a project, or installing a package can be as simple as running a command.

Most development tools provide command-line commands. You can create Python virtual environments, install libraries, and start a server from the terminal.

Having to remember commands may feel unfamiliar at first. But you will use a small set of commands most often, and it is perfectly fine to look up others as you need them.

## Opening a terminal {#open-terminal}

Each operating system provides its own terminal applications.

### macOS {#macos}

- Press `Command + Space` to open Spotlight, type `Terminal`, and launch it.
- You can also open it from `Applications > Utilities > Terminal`.

### Windows {#windows}

- Press `Windows + R` to open the Run dialog, type `powershell`, and press Enter.
- You can also search for `PowerShell` in the Start menu.

!!! info "PowerShell"
    Windows provides both Command Prompt (`cmd`) and PowerShell as command-line environments. This guide uses PowerShell, which offers more features and works well with modern development tools.

## :material-pencil: Exercises {#exercises}

Open a terminal and enter the command below. If it lists the files and folders in your current location, you are ready to go.

=== "macOS"

    ```bash
    ls
    ```

=== "Windows PowerShell"

    ```powershell
    dir
    ```

??? success "Answer and explanation"
    On macOS and Linux, `ls` lists the files and folders in the current location. In Windows PowerShell, use `dir`. PowerShell also supports `ls` as an alias for the same operation.
