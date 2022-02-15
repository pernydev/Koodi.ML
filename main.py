from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from random import randint

hostName = "0.0.0.0"
serverPort = 40003
codes = dict()

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path == "/":
            f = open("main.txt")
            code = f.read()
            f.close()
            self.wfile.write(bytes(code, "utf-8"))
        else:
            url = self.path[1:]
            f = open("seelink.txt")
            code = f.read()
            f.close()
            # Make PIN a random 4 number number (Github Copilot)
            pin = randint(1000, 9000)
            # add pin with the value url to codes (Github Copilot)
            codes[pin] = url
            code = code.replace("%{CODE}%", pin)
            self.wfile.write(bytes(code, "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")