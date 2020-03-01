# Requirements
* git (+credentials configured in your bash environment)
* python3

# The first time you want to run these notebooks
1) Clone this repository
    `git clone https://github.com/BLannoo/LocationAnalysis.git`
2) Enter the root directory
    `cd LocationAnalysis`
3) Create an virtual environment under the folder .venv
    `python3 -m venv .venv`
4) Activate that venv
    `source ./.venv/bin/activate`
5) Install the dependencies to this project
    `pip install -r requirements.txt`
6) Start the jupyter server
    `jupyter lab`

# When you want to run these notebooks again
1) Activate that venv
    `source ./.venv/bin/activate`
2) Start the jupyter server
    `jupyter lab`
    
# Configuring Jupytext
## Context
Jupytext is a tool that allows seperating the code in your notebooks from the output cells.  
This allows to keep your output and commit your notebooks to git without those outputs.

## Initial setup (to generate a .py when you create/save a .ipynb)
1) Install jupytext (included in requirements.txt)
2) Generate a jupyter config on your local machine (TODO make this project specific)
    ```bash
    jupyter notebook --generate-config
    ```
3) Add the following config to `~/.jupyter/jupyter_notebook_config.py`
    ```python
    c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"
    c.ContentsManager.default_jupytext_formats = "ipynb,py:percent"
    ```

## Opening .py as notebooks
1) Right click *.py > Open With > Notebook
2) Save the notebook (this will generate an .ipynb)
