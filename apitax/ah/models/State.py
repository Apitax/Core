class State:
    config = None
    options = None
    log = None
    paths = {
        "config": "",  # Path to config file
        "root": "",  # Path to root of the app
        "apitax": "",  # Path to apitax/ah folder
        "log": "",  # Path to log file
    }
    baseUrl = "/apitax/2/"
