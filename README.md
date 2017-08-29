# chatty
An anonymous chat client/server built on the Tornado library using a combination of standard HTTP (to serve the page) and WebSockets (to handle the realtime chat). 

### setup
1. requirements: [`python 3` + `virtualenv`](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3)

2. clone the project

3. create a virtual environment for the project
```
$ virtualenv -p python3 chatty
```

4. install project dependencies in the virtual environment
```
$ source chatty/bin/activate
$ pip install tornado
$ deactivate
```

### run
1. activate the virtual environment
```
$ cd chatty
$ source bin/activate
```

2. start the app (the `--debug` flag turns on [autoreload](http://www.tornadoweb.org/en/stable/autoreload.html))
```
$ python hello.py
$ python hello.py --debug
```

3. http://localhost:8085/
    - new tabs/windows will create new users
    - NOTE: page refreshes will break every user's connection

4. deactivate the virtual environment when you're done
```
$ deactivate
```
