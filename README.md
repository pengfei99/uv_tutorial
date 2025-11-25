# uv_tutorial

In this tutorial, we will learn:
- what is uv?
- how to install uv?
- how to use uv to manage a python project?

## What is uv?

**UV** is a `python package and project manager` implemented with **Rust**. For package installation, uv is `10 to 100
times faster than pip`(not tested by me, so not sure).

Additionally, uv has the most of the functionality provided by tools like `pip, pip-tools, pipx, poetry, pyenv, twine, 
virtualenv, and more`. Therefore, uv is an `all-in-one solution`.

### Key uv features for managing your Python projects

- **Fast dependency installation**: Installs dependencies really fast, which is especially useful for large dependency trees.
- **Virtual environment management**: Automatically creates and manages virtual environments.
- **Python version management**: Allows the installation and management of multiple Python versions.
- **Project initialization**: Scaffolds a full Python project, including the root directory, Git repository, virtual environment, pyproject.toml, README, and more.
- **Dependency management**: Installs, updates, removes, and locks direct and transitive dependencies, which allows for environment reproducibility.
- **Package builds and publication management**: Allows you to build and publish packages to package repositories like the Python Package Index (PyPI).
- **Developer tooling support**: Installs and lets you run development tools, such as pytest, Black, and Ruff.


`uv is a standalone binary` that allows for a smooth installation and quick upgrades. 

> You don’t need to have Python installed on your system to install uv.

## Install uv 

Based on your OS, the installation guide is different. You can find the official doc [here](https://github.com/astral-sh/uv)


### Linux/MacOS

Under Linux, it's quite simple. Just use the provided installation script.


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

# you may need to restart your shell

# check uv version
uv --version

```

## Use uv to create a python project

Go to the root folder where you want to put your project. Then run the below commands

```bash
# create a project
uv init my-app

# goto the project folder
cd my-app

# check the generated files
> tree -L 3 -a .
.
├── main.py
├── pyproject.toml
├── .python-version
└── README.md

1 directory, 4 files
```

You should see the below files

- **pyproject.toml**: The new standard for defining dependencies (replaces requirements.txt).
- **.python-version**: Locks the Python version for this specific project.
- **main.py**: A simple "Hello World" entry point.
- **README.md**: Read me of your project

### Set up python version and dependencies

```bash
# Set a specific Python version for your project
uv python pin 3.14

# add packages to your project
uv add notebook

# add dev packages to your project
uv add --dev ruff pytest 
```




