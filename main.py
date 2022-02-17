from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from random import randint
from urllib.parse import urlparse , urljoin

hostName = "0.0.0.0"
serverPort = 40003
serverUrl = "koodi.ml"
codes = dict()

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            f = open("main.txt")
            code = f.read()
            f.close()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            code = code.replace("%{URL}%", serverUrl)
            self.wfile.write(bytes(code, "utf-8"))
        elif self.path == "/favicon.ico":
            print("Page opening...")
        elif "codeEndpoint" in self.path:
            # get the code from the query
            query = urlparse(self.path).query
            query_components = dict(qc.split("=") for qc in query.split("&"))
            codeQuery = query_components["code"]
            if codeQuery in codes:
                theLnk = codes[codeQuery]
                print("Code: "+codeQuery+" Link: "+codes[codeQuery])
                self.send_response(301)
                self.send_header("Location", theLnk)
                self.end_headers()
            else:
                print("Code: " + codeQuery + " Not found!")
                self.send_response(404)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(bytes("Code not found!", "utf-8"))
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            url = self.path
            f = open("seelink.txt")
            code = f.read()
            f.close()
            # Make PIN a random 4 number number (Github Copilot)
            pin = randint(1000, 9000)
            # add pin with the value url to codes (Github Copilot)
            # make pin a string (Github Copilot)
            pin = str(pin)
            url = url[1:]
            if "script" in url:
                url = serverUrl
            elif "http" in url:
                url = url
            elif "https" in url:
                url = url
            else:
                url = "http://"+url
            codes[pin] = url
            code = code.replace("%{CODE}%", pin)
            code = code.replace("%{URL}%", serverUrl)
            self.wfile.write(bytes(code, "utf-8"))
            print("Link created! Pin: "+pin+" Link: "+codes[pin])

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
