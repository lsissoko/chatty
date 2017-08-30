# chatty
An anonymous chat client/server built on the Tornado library using a combination of standard HTTP (to serve the page) and WebSockets (to handle the realtime chat). 

### setup
##### requirements
[`python 3` + `virtualenv`](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3)

##### clone the project
```
$ git clone git@github.com:lsissoko/chatty.git
```

##### create a virtual environment
```
$ virtualenv -p python3 chatty
```

##### install project dependencies (in the virtual environment)
```
$ source chatty/bin/activate
$ pip install tornado
$ deactivate
```

### run
##### open the virtual environment
```
$ cd chatty
$ source bin/activate
```

##### start the app (use the `--debug` flag to turn on [autoreload](http://www.tornadoweb.org/en/stable/autoreload.html))
```
$ python hello.py
```

##### open http://localhost:8085/
    - new tabs/windows will create new users
    - NOTE: refreshing a page will break every user's connection

##### close the virtual environment when you're done
```
$ deactivate
```
