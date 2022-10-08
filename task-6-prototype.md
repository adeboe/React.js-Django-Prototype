# Project Creation Document
By Allan DeBoe

This demonstrates the commands done 

## References
```
https://www.geeksforgeeks.org/how-to-connect-django-with-reactjs/
```

## Back-end (Django)
These are commands used to create the Django back-end

### Create Virtual Environment
This assumes that the current directory would be the target directory for the project.
```
py -m venv task-6-ui-back-end\task-6-ui-venv
cd task-6-ui-back-end\task-6-UI-env\Scripts
activate.bat
```

### Install Dependencies
This is done while in the virtual environment (via activate.bat)
Here are the commands for the Django dependencies:
```
pip3 install Django
pip3 install djangorestframework
pip3 install django-cors-headers
```

### Create Django Project
This is done while in the virtual environment (via activate.bat)
```
django-admin startproject prototype
cd prototype
py manage.py startapp core
```

## Front-end (React.js)
These are the commands used to create the React.js front-end

### Create React App

```
npx create-react-app task-6-ui-front-end
cd task-6-ui-front-end
npm install axios
```

## Running the program

### Terminal 1 (Back-end)
These commands start up the back end so the front-end can work as intended.
```
task-6-ui-back-end\task-6-UI-env\Scripts\activate.bat
```

### Terminal 2 (Front-end)
These commands start up the front end so that the site becomes accessible
```
cd task-6-ui-front-end
npm start
```