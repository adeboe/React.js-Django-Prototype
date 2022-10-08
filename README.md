# SER401-Django-React.js-UI-Prototype
This is a small prototype that uses Django and React.js to get myself familiar with those technologies for the larger project my team will be working on.

## Installation Details
First, it is important to install Python (at least version 3.10.7). It is also important to install Node.js (primarily for the Node Package Manager or `npm`, which will be used to help run the front-end).

Next, download the repo, which is a python virtual environment that should work on at least Windows 10. 

## Running The Prototype

### Back-end
Open up a terminal at the directory of the project (i.e. where this file is), and run the following code
```
task-6-ui-back-end\task-6-ui-venv\Scripts\activate.bat
```

After this, you should now be in the virtual environment. At this point, you can simply run
```
py task-6-ui-back-end\prototype\manage.py runserver
```

If successful, you should be able to access `http://localhost:8000/test/` and see the Django REST Framework on
the top left corner.

### Front-end
Open up another terminal at the project directory (i.e. where this file is), and all you have to
do is run the following command
```
npm start
```

If successful, you should be able to see a page containing `SER401 - Task 6 (UI) Prototype` on the top
of the page.