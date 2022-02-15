from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostname = "localhost"
serverPort = "40003"

print("Käynnistetääm Linkki.ML paneelia portissa "+PORT+"!")

class Linkserver(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<h1>Toimii!</h1>", "utf-8")
                         
   if __name__ == "__main__"
                         webServer = HTTPServer((hostName, serverPort), Linkserver)
                         print("Linkki.ML käynnistetty onnistuneedti!")
                         webServer.serve_forever()
