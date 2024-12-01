# Project Charlie Blog

#### This document written by TRB

## Installation

### Clone the repository

1. You will need git to clone the repository. Git is the version control software that allows you to get this code and install it on your machine, make changes, etc. Install it [here](https://git-scm.com/downloads). I highly recommend using homebrew to install git on Mac.
2. With git installed, open a terminal / command prompt.
3. Navigate to the place you would like to store the folder. Your "Documents" folder is a good place to store the project. You can use the "cd" command to get to your documents folder - google "how to change directory to Documents folder on XXX" where XXX is your operating system if you don't know how to do it. If you are using Windows, you might want to consider installing the [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install), which gives you a better file structure for basically everything!
4. Now that you're in the folder you'd like to put the project in, clone this repository using the command in your terminal:
   ```
   git clone https://github.com/crunchytee/charlie-blog.git
   ```
5. You should see a progress tree that indicates the folder has been created. Now the project is on your computer!

### Create a python virtual environment

Now that you have the code on your computer, you need to set up an environment where python can store installations, configurations, and it's own code. Basically, if python was an actual snake, this is setting up the cage for it to live in.

1. [Install python](https://www.python.org/downloads/) if you haven't already.
2. In your terminal / command prompt, wherever you cloned the project folder into (say, Documents), change directories into the project folder:

```
cd charlie-blog
```

3. Now that you're in the project file, create a python virtual environment:

```
python3 -m venv .venv
```

\*_You may encounter an error along the lines of "command python3 not found" - if this happens, replace python3 with python_

### Open the project in your code editor and activate the virtual environment

Now that the code is downloaded, and you have a python virtual environment, it's time to open everything up in an editor. This guide assumes you will use VSCode but you can use anything.

1. [Download VS Code](https://code.visualstudio.com/) if you don't have it already
2. Open VS Code, and select "Open" under the Start section (or, under "File", "Open Folder") and select the charlie-blog folder.
3. This should open up the folder. Confirm on the left hand side that you have the charlie-blog folder as the top level, and all it's subfolders underneath.
4. In VS Code, open the terminal by selecting "Terminal" up at the top, and then "New Terminal". You may already have a terminal open, and that is fine.
5. Your terminal should be open to the project folder already open. On Windows, type "cd" to confirm this, or type "pwd" on Mac to confirm.
6. Finally, activate the python virtual environment:

On Mac:

```
source venv/bin/activate
```

On Windows:

```
venv\Scripts\activate
```

### Install dependencies

Before you can run the actual project, you need to satisfy the projects dependencies. Dependencies are the code libraries that the project requires to run. In general, you can use the "pip install package-name" syntax to install a package. In this example, we'll install all the dependencies at once from a file:

```
pip install -r requirements.txt
```

\*_This may take a minute_

### Configuration file

You will need a configuration file. Add a config.py file to the root directory, and add the required configuration elements. Here is an example:

config.py:

```
import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://', 'postgresql://') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    POSTS_PER_PAGE = 3
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = 'test@gmail.com'  # Use your actual Gmail address
    MAIL_PASSWORD = '12334'     # Use your generated App Password
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
```

### Configure database

This project uses the flask-sqlalchemy ORM for database interactions, and the flask-migrate package for migrations. To initialize the database:

```
flask db init
flask db upgrade

```

### Launch project

Finally, the project is ready to roll! To start the webserve in development mode, simply run the start command:

```
flask --app app run --debug
```

You should get a response warning of development server, and a link to see the live site. This is typically something like:

```
* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Where "http://127.0.0.1:5000" is the site you can copy and paste in to your browser to see the site.

## Version control structure

This project follows the Flask Mega Tutorial. Each chapter is a separate branch. To switch between branches:

```
git checkout branch_name
git pull
```

"git pull" will pull the codebase down to your local machine. When you switch branches, it may not be needed to do this, but it won't hurt to do.
**main is the primary branch**

## Deployment
This project is recommended to be deployed using [Heroku](heroku.com). You will need to download the Heroku CLI, create and account, and then create an app and deploy it using the following commands:
Start by logging in to Heroku
```
heroku login
```
Next, ensure you have a git repository for the project you want to deploy. Heroku relies on Git for deployment
```
git init
```
Create a Heroku App for deployment. The name of the app needs to be universally unique
```
heroku apps:create app-name
```
This project by default relies on SQLite for database, but Heroku uses an Ephemeral file system (erases frequently), so you need to use a persistent database, like the Heroku Postgres database
```
heroku addons:add heroku-postgresql:essential-0
```
You also need to create a Procfile (the command heroku uses to run the app) and update the requirements for deployment - but this repository includes those already. Finally, set your app environment variable: 
```
heroku config:set FLASK_APP=charlie-blog.py
```
And deploy by pushing the app to heroku! 
```
git push heroku main
```

