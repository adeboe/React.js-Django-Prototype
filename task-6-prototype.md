# Project Creation Document
By Allan DeBoe

This demonstrates the commands done 

## References
```
https://www.geeksforgeeks.org/how-to-connect-django-with-reactjs/
```

## Back-end (Django)
These are commands

### Create Virtual Environment
This assumes that the current directory would be the target directory for the project.
```
py -m venv task-6-UI-env
cd task-6-UI-env\Scripts
activate.bat
```

### Install Dependencies
This is done while in the virtual environment (via activate.bat)
Here are the commands for the Django dependencies:
```
py -m pip install Django
py -m pip install djangorestframework
py -m pip install django-cors-headers
```

### Create Django Project
This is done while in the virtual environment (via activate.bat)
```
django-admin startproject task_6_prototype
cd task_6_prototype
py manage.py startapp prototype
```
