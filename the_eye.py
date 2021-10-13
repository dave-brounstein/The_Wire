import threading

from com.dave.app import process
from com.dave.server.server import app

threading.Thread(target=process.worker, daemon=True).start()

# instantiate the app

if __name__ == '__main__':
    app.run(debug=True)
