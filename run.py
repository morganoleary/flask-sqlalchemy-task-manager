# to use environment variables w/in this file
import os
from taskmanager import app


# tell app how & where to run the application - checking that name class is = default 'main' string
# if its a match we need the app running - takes 3 arguments (each stored in environment variables):
if __name__ == "__main__":
    app.run(
        host= os.environ.get("IP"),
        # convert to integer
        port= int(os.environ.get("PORT")),
        debug= os.environ.get("DEBUG")
    )
