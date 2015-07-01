# wiki-climber
Climb wiki pages with this web crawler turned RESTFUL-API.
Uses Zmq, Python, Node.js to Pipe parsing of wiki page (Python) to Node.js (Restful Api)

#TODO:
Need to make a way to install using npm, update the capabilities of the "climber" to gather mor einfor from wiki.
Need to create gulp or grunt method to start both servers simeultaneosly seeing as they are dependedt on each other to function.
May go to lower level controls on zeromq connection for more extensibility and incorporate socket.io for updates from a user interface on the client side.

#Install 
1. `git clone <repo>
2. `cd <repo>`
3. `npm install`
4. `Terminal1: python climber.py`
5. `Terminal2: node chimera.js`
