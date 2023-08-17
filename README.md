# Twitter Clone

Twitter clone project.

# Running the code

1. Make local instance of the project: `git clone https://github.com/bitcamp-ge/twitter-clone-py-t1`
0. Change directory into the project: `cd twitter-clone-py-t1`
0. Create a Python environment: `python -m venv venv`
0. Activate Python environment
0. Install Python dependencies: `pip install -r requirements.txt`
0. Make Django migration: `python manage.py makemigrations`
0. Run Django migrations: `python manage.py migrate`
0. Load initial database: `python manage.py loaddata initial_data.json`
0. Start the Django server: `python manage.py runserver localhost:8000`

> #### Note
> - Superuser username: `root`
> - Superuser password: `root`

# How to activate a Python environment

### For Linux/Unix users
- bash/zsh - `source ./venv/bin/activate`
- fish - `source ./venv/bin/activate.fish`
- csh/tcsh - `source ./venv/bin/activate.csh`

### For Windows users
- PowerShell
- - Enable script execution - `Set-ExecutionPolicy RemoteSigned`
- - Run activation script - `.\venv\Scripts\Activate.ps1`
- cmd.exe - `.\venv\Scripts\activate.bat`