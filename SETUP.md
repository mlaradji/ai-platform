# Environment Setup

## Import environment
As `ai-platform` does not currently have a `conda.yaml` file, you should use either 'Anaconda setup with requirements.txt' or 'PIP virtualenv setup with requirements.txt'. Some of the tasks in `ai-platform` do have a `conda.yaml` file, and for those you can follow 'Anaconda setup with conda.yaml'.

### Anaconda setup with conda.yaml
1. Download [anaconda](https://www.anaconda.com/distribution/) (Python 3.7) and run the installer:

```
wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
sh Anaconda3-2019.03-Linux-x86_64.sh # Answer the installer prompts.
conda init # Only necessary if you want to be able to use `conda activate` from your shell.
```

This will install many popular but unnecessary packages, such as `pandas`. If you prefer to only install the packages you need yourself, you can install the much smaller [miniconda](https://docs.conda.io/en/latest/miniconda.html), which has all of the features of the full version. Note that you'll have to manually install `python` in `miniconda`.

2. Install the `conda.yaml` file:

```
# From the root directory of the ai-platform repo
conda env create -f conda.yaml
```
This will install all the packages listed in `conda.yaml` into the environment name mentioned in `conda.yaml`. If you prefer to use a differently named environment, use:
```
conda env create -n nameofenv -f conda.yaml
```

3. You can now start using your new environment through

```
conda activate ai-platform # substitute ai-platform with your environment name
python # or whatever command you want to run
```
You can install new packages through `conda install PACKAGE`. You can find a list of installable packages in [anaconda.org](anaconda.org).
To keep the `ai-platform` intact, you can clone it via
```
conda create -n newenvironment --clone ai-platform
```

### Anaconda setup with requirements.txt
Follow step 1 above. Then, execute the following commands:
```
conda create -n ai-platform
conda activate ai-platform
conda install python # If the environment doesn't already include python.
pip install -r requirements.txt
```

### PIP virtualenv setup with requirements.txt
This method is probably the most portable, as anyone with python will be able to use it. However, unlike with `conda`, using only `pip` restricts one to python packages.

Execute:
```
python -m venv venv # Replace the second `venv` with the directory in which you want to set up the virtual environment.
source venv/bin/activate # Replace `venv` as above.
pip install -r requirements.txt
```

## Export environment
If you want to export your current environment (to upload to the github repo, for example), do the following for pip:
```
source yourvenv/bin/activate # Switch to your pip virtualenv first
pip freeze > requirements.txt
```
For conda, use:
```
conda activate yourenvironment # Switch to your conda env first
conda env export > conda.yaml
```
