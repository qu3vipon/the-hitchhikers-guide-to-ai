# VS Code

When programming, we use tools that help us write code, manage files, and inspect results and errors. These tools include **integrated development environments (IDEs)** and code editors.

This guide uses **Visual Studio Code**, or **VS Code**, a free code editor from Microsoft. It is lightweight to get started with, and extensions bring the tools you need for Python development together in one place.

## Installing VS Code {#install-vscode}

Visit the [official VS Code download page](https://code.visualstudio.com/download) and download the installer for your operating system.

### macOS

1. Download the macOS `.dmg` file.
2. Open the disk image, then drag `Visual Studio Code.app` into `Applications`.
3. Launch Visual Studio Code from `Applications` or Spotlight.

### Windows

1. Download the Windows **User Installer**.
2. Run the downloaded `.exe` file.
3. Follow the installation instructions, then launch Visual Studio Code.

## Installing the Python extension {#install-python-extension}

VS Code uses **extensions** to add language-specific features. The Python extension provides tools such as code completion, error checking, and debugging.

1. Select the **Extensions** icon on the left side of VS Code.

    - On macOS, you can also press `Command` + `Shift` + `X`.
    - On Windows and Linux, press `Ctrl` + `Shift` + `X`.

2. Search for `Python`.
3. Select the `Python` extension published by **Microsoft**.
4. Select **Install**.

!!! info "The Python extension is not Python itself"
    The extension adds Python development features to VS Code. You still need to install Python on your computer to run Python code. We cover this in [Installing Python](python-install.md).

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. VS Code is a free code editor made by Microsoft.
2. Installing the VS Code Python extension automatically installs Python itself.
3. The Python extension adds features such as code completion and debugging.

??? success "Answers and explanations"
    1. **True** — We use the free VS Code editor as our development tool.
    2. **False** — The extension adds editor features. You must install the Python runtime separately.
    3. **True** — The extension provides completion, error checking, and debugging tools.
