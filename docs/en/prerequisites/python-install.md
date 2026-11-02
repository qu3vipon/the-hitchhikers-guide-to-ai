# Installing Python

To run Python code, your computer needs a **Python interpreter**: the program that reads and executes the code you write.

## Installing Python {#install-python}

On macOS, we use Homebrew. On Windows, we use the official Python install manager. You can check version support on the [official Python download page](https://www.python.org/downloads/). Unless your project requires a particular version, choose a current stable release.

| Status | Meaning |
| --- | --- |
| Pre-release | An alpha, beta, or release candidate for testing an upcoming release. |
| Bugfix release | A stable release receiving bug fixes and security updates. |
| Security release | An older release receiving security fixes, without new features or routine bug fixes. |
| End-of-life | A release that no longer receives support or security updates. |

### macOS

**Homebrew** is a tool for installing and managing software from the command line.

1. If you do not have Homebrew, run the installation command from the [official Homebrew website](https://brew.sh/) in your terminal. When installation finishes, follow the printed **Next steps** to add Homebrew to your `PATH`. Skip this step if Homebrew is already installed.
2. Install Python:

    ```shell
    brew install python
    ```

3. Check the installation:

    ```shell
    python3 --version
    ```

Use `python3` to run the Python installed by Homebrew. See [Homebrew’s Python documentation](https://docs.brew.sh/Language-Runtimes-and-Packages#python) for more information.

### Windows

1. Download and install the **Python install manager** from the [Python downloads page for Windows](https://www.python.org/downloads/windows/).
2. Open PowerShell and install the latest stable Python 3 runtime:

    ```powershell
    py install 3
    ```

3. Check the installation:

    ```powershell
    python --version
    ```

## Where Python is installed {#python-location}

The interpreter is stored in a particular location on your computer. When you type `python` or `python3`, the terminal searches the directories registered in its search path to find that interpreter.

A Python installation available across your computer is often called **global Python**. You can invoke it from different project folders.

Use these commands to see where Python is found. The result depends on your installation method and account.

=== "macOS"

    ```console
    $ which python3
    /opt/homebrew/bin/python3
    ```

    This is a typical Apple Silicon Mac path. On an Intel Mac, it is usually `/usr/local/bin/python3`.

=== "Windows"

    ```console
    PS> where.exe python
    C:\Users\yourname\AppData\Local\Microsoft\WindowsApps\python.exe
    ```

    Windows may show a launcher or app alias that selects the installed runtime.

## Python versions {#python-version}

A version such as `Python 3.14.0` has three components. This is an example version, rather than a requirement to install this exact release.

| Component | Example | Meaning |
| --- | --- | --- |
| Major | `3` | A major generation of the language. This guide uses Python 3. |
| Minor | `14` | A release that adds features and improvements. |
| Patch | `0` | A maintenance release containing fixes. |

Different Python 3 minor versions can support different features and library versions. Use the version a project specifies. Otherwise, choose a current stable release.

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. Installing Python installs an interpreter that executes Python code.
2. Libraries installed into a shared global Python environment can affect multiple projects.
3. In `Python 3.13.1`, `13` is the major version.

??? success "Answers and explanations"
    1. **True** — The interpreter runs the code you write.
    2. **True** — Projects sharing an environment can be affected by changes to its libraries.
    3. **False** — `3` is the major version, `13` is the minor version, and `1` is the patch version.
