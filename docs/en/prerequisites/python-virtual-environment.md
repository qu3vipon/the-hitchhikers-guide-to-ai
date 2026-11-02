# Python virtual environments

Python lets you reuse code written by other developers. These reusable collections of code are called **libraries**. For example, installing FastAPI gives you ready-made functionality for building web APIs.

Installing every library into one shared Python environment can cause conflicts when different projects need different versions. Some Python distributions, including Homebrew’s, also protect their global environment from direct package installation.

Instead, create a **virtual environment** for each project. Starting a Python project by creating its virtual environment is standard practice.

## Creating a virtual environment {#create-virtual-environment}

Python includes a module named `venv` for this purpose. Create a project folder, enter it, and create an environment named `.venv`.

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

The final command creates a `.venv` folder containing the project’s Python environment and its own library installation directory.

!!! info "Naming your environment"
    `.venv` is a widely used convention. The name is short for “virtual environment.”

    On macOS and Linux, a leading dot (`.`) marks a file or folder as hidden in normal listings. This helps keep the environment separate from your main project files. Windows does not treat a leading dot as a hidden attribute, but the same name works there too.

## Activating a virtual environment {#activate-virtual-environment}

Activate the environment to make `python` and `pip` in your terminal use the project’s environment rather than global Python.

=== "macOS"

    ```shell
    source .venv/bin/activate
    ```

=== "Windows PowerShell"

    ```powershell
    .venv\Scripts\Activate.ps1
    ```

Your prompt will normally gain a `(.venv)` prefix:

```console
(.venv) playground $
```

Python now runs in the project’s isolated environment. Installing libraries here will not change the libraries in other projects’ environments.

## Deactivating a virtual environment {#deactivate-virtual-environment}

When you are finished, return to the previous environment with the same command on either operating system:

```shell
deactivate
```

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. Creating a virtual environment is a common first step in a new Python project.
2. After activation, the `python` command still uses the global Python environment.
3. `deactivate` ends the active virtual environment session.

??? success "Answers and explanations"
    1. **True** — Separate environments keep each project’s library versions independent.
    2. **False** — Activation makes the terminal use Python from `.venv`.
    3. **True** — It deactivates the environment and restores the previous command search path.
