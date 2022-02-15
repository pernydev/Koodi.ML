from http.server import BaseHTTPRequestHandler, HTTPServer
import time
code = dict()

hostName = "0.0.0.0"
serverPort = 40003

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path is set:
            self.wfile.write(bytes("<p>created.</p>", "utf-8"))
        else:
            self.wfile.write(bytes("<p>code?</p>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
