import jupyterlab

if jupyterlab.__version__:
    print(f"You have JupyterLab version {jupyterlab.__version__} installed.")
else:
    print("JupyterLab is not installed.")