import http.server

PORTTI="40003"

print("Käynnistetääm Linkki.ML paneelia portissa "+PORTTI+"!")

class LinkkiServu(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<h1>Toimii!</h1>", "utf-8")

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Linkki.ML käynnistetty onnistuneedti!")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Sammutetaan...")
