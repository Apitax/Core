#!/usr/bin/env python

from apitax.ah.State import State

State.paths['root'] = '/app'
State.paths['config'] = '/app/config.txt'

from apitax.ah.Setup import Setup
from project import Project

# Put Driver imports here

# End Driver imports
project = Project()

# Setup must run before importing the 'app' object from the API Server
setup = Setup()

# Set drivers
project.loadDrivers()
# End set drivers

# Put your custom logic here

# End custom logic

# These should probably be the last lines of your file
setup.load()
from apitax.ah.api.Server import *
# Uncomment to debug without uwsgi or nginx
#app.run(port=5082, host='0.0.0.0')