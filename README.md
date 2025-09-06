# pylib

A simple CLI tool to randomly pick Auckland libraries.

---

## Features

- Pick 1 or more random libraries from Auckland.  
- Display all available libraries.  
- Easy-to-use command-line interface.

---

## Installation (Global)

You can install `pylib` globally so the `pylib` command works anywhere.  

1. Clone the repository and navigate into it:  
`git clone https://github.com/yourusername/pylib.git`  
`cd pylib`  

2. Install the package globally:  
`pip install .`  

> If you don’t have admin privileges, you can install for your user only:  
`pip install --user .`  

> On macOS/Linux, if using `--user`, make sure your local bin directory is in your PATH:  
`export PATH="$HOME/.local/bin:$PATH"`  
Add that line to your `~/.zshrc` or `~/.bashrc` to make it permanent.

---

## Usage

- Show all libraries: `pylib -a or pylib --all`  
- Pick 3 random libraries: `pylib -n 3 or pylib --number 3`  
- Pick the default (1) random library: `pylib`

---

## Uninstallation

To remove `pylib` completely:  
`pip uninstall pylib`

- Confirm when prompted. This removes the CLI command and package files.

---

## Developer Installation (Optional)

If you want to **edit the code** and test changes without reinstalling:

1. Clone the repository and navigate into it:  
`git clone https://github.com/yourusername/pylib.git`  
`cd pylib`

2. Create and activate a virtual environment:  
`python -m venv .venv`  
`source .venv/bin/activate`

3. Install in editable mode:  
`pip install -e .`

- Changes to `cli.py` will be reflected immediately.  
- Run the CLI with: `pylib -a` or `python -m pylib.cli -a`