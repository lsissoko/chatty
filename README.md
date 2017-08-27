# chatty
An anonymous chat client/server built on the Tornado library using a combination of standard HTTP (to serve the page) and WebSockets (to handle the realtime chat). 

### setup
1. [`python 3` + `virtualenv`](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3)
1. clone project
2. `virtualenv -p python3 chatty`

### run
1. `cd chatty`
2. `source ./bin/activate`
3. `python hello.py` (or `python hello.py --debug` if you want to turn on [autoreload](http://www.tornadoweb.org/en/stable/autoreload.html))
4. http://localhost:8085/
    - open new tab(s)/window(s) to create new user(s)
    - messages will be sent to all users
5. `deactivate` (when done using the app)
