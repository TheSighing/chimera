# Climber "Why Crawl when you can Climb?"
Climb wiki pages with this web crawler turned API.
Uses Zmq, Python, Node.js to pipe the parsing of a wiki page into "Bolts" (Python) to Node.js (API)

Gathers context and text and stores these in relation to each other with level identifiers.

#TODO:
Need to make a way to install using npm, update the capabilities of the "climber" to gather more info from wiki.

Need to create gulp or grunt method to start both servers simultaneously seeing as they are dependent on each other to function.

May go to lower level controls on zeromq connection for more extensibility and incorporate socket.io for updates from a user interface on the client side.

Need to make a node js program that runs both servers as child process' and acts as the entry point for bower/npm to make this a stand alone API that can be added to any project needing it (npm).

#Install 
1. `git clone <repo>`
2. `cd <repo>`
3. `npm install`
4. `Terminal1: python climber.py`
5. `Terminal2: node climber.js`
