  # Web application to have a video conference
  
  I am using WebRTC protocols to stablish a connection in real time between client, you can find more information at https://webrtc.org/
  * Note. There are several libraries to create a WebRTC server, for this project we'll use [EasyRTC](https://easyrtc.com/) that simplifies the process of start a WewbRTC server.
  * Note. You need Nodejs installed to start a WebRTC server. You can download and install it from [this link](https://nodejs.org/es/)
  
    Installing the node server
======
  
  When you are done with nodejs, you can proceed to install the WebRTC Server.
  * First open a terminal in Linux or MAC, or a CMD window in Windows, and type Inline `cd RTC`
  * Then use the `npm install` command to install all the packages needed to start the server
  * Use the `cd server_example` to move to the server directory, and use `npm install` again
  * Finally use `node server.js` to start the server
  
  * If everything is already working, you'll see an `Initiated` message in the console.
  * Check the node server going to localhost:8080 in the web browser.
  * If everything's ok you will see a message like this: **You have installed EasyRTC!**
  
  The other part of the project is a DJango application to have user control.
  
  
  Install the web application
======
* First, ensure you have installed python 2 or python 3; using the `python -V` in a command prompt. For this project we are using [Python 3.5.2](https://www.python.org/downloads/release/python-352/)
* Note. I recommend you to have a virtual environment because you could have more python projects, and in a virtual environment, you can install several python libraries and they won't affect the other python instances.
* Then install DJango library. For this project I'm using **Django 2.1.2**. To install that version you can use `python -m pip install django==2.1.2`
* Use `python -m pip freeze` to know the python packages installed in your machine or virtual environment, if everything's ok, you will see **Django==2.1.2** in the list.
* Navigate to **hospital** directory through `cd hospital` if you are in the root directory.
* Run the `manage.py makemigrations` and `manage.py migrate` to create database migrations.
* User `manage.py runserver` to start the django server.*
* If everything's ok you'll see the **Starting development server at http://127.0.0.1:8000/** message
* Open a new tab in web browser and navigate to localhost:8000

    bug log
======

1. If you create a super user 
