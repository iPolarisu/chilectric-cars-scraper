# chilectric-cars-scraper
Simple Python script what web scrapes the chilean electric vehicles catalogue and dumps the information into a csv file.

### Installing

It is highly advised that you use a **Python Virtual Environment** to install the modules.

1. Creating the virtual environment

    ```bash
    # installing virtualenv
    pip install virtualenv

    # create a virtual env for the project
    virtualenv .venv
    ```

2. Activating the virtual environment

    Windows

    ```powershell
    .venv\Scripts\activate
    ```

    Linux/MacOS

    ```bash
    source .venv/bin/activate
    ```

3. Installing modules via pip

    ```bash
    pip install -r requirements.txt
    ```

### Executing

```bash
python main.py
```
