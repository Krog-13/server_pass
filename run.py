from wsgiref.simple_server import make_server
import datetime
from src.app import application

def func():
    pass

if __name__ == '__main__':
    with make_server('', 5001, application) as httpd:
        print(" * Serving on http://{0}:{1} (Press CTRL+C to quit)"
              .format(*httpd.server_address))
        try:
            httpd.handle_request()
        except KeyboardInterrupt:
            httpd.server_close()