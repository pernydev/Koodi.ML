from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "0.0.0.0"
serverPort = 40003
code = dict()

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path == "/":
            self.wfile.write(bytes(main, "utf-8"))
        else:
            url = self.path[1:]
            self.wfile.write(bytes("<p>created code to "+url+"</p>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

main = "<html lang="en" class="sr js anime-ready"><head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>April Template</title>
    <link href="https://fonts.googleapis.com/css?family=Heebo:400,500,700|Fira+Sans:600" rel="stylesheet">
    <link rel="stylesheet" href="https://cruip.com/wp-content/themes/cruip-2/style.css?ver=1.0.17">
	<script src="https://unpkg.com/animejs@2.2.0/anime.min.js"></script>
    <script src="https://unpkg.com/scrollreveal@4.0.0/dist/scrollreveal.min.js"></script>
</head>
<body class="is-boxed has-animations" style="height: 100%;">
    <div class="body-wrap boxed-container">
        <header class="site-header">
			<div class="header-shape header-shape-1">
				<svg width="337" height="222" viewBox="0 0 337 222" xmlns="http://www.w3.org/2000/svg">
				    <defs>
				        <linearGradient x1="50%" y1="55.434%" x2="50%" y2="0%" id="header-shape-1">
				            <stop stop-color="#E0E1FE" stop-opacity="0" offset="0%"></stop>
				            <stop stop-color="#E0E1FE" offset="100%"></stop>
				        </linearGradient>
				    </defs>
				    <path d="M1103.21 0H1440v400h-400c145.927-118.557 166.997-251.89 63.21-400z" transform="translate(-1103)" fill="url(#header-shape-1)" fill-rule="evenodd"></path>
				</svg>
			</div>
			<div class="header-shape header-shape-2">
				<svg width="128" height="128" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg" style="overflow:visible">
				    <defs>
				        <linearGradient x1="93.05%" y1="19.767%" x2="15.034%" y2="85.765%" id="header-shape-2">
				            <stop stop-color="#FF3058" offset="0%"></stop>
				            <stop stop-color="#FF6381" offset="100%"></stop>
				        </linearGradient>
				    </defs>
				    <circle class="anime-element fadeup-animation" cx="64" cy="64" r="64" fill="url(#header-shape-2)" fill-rule="evenodd" style="opacity: 1; transform: translateY(0px);"></circle>
				</svg>
			</div>
            <div class="container">
                <div class="site-header-inner">
                    <div class="brand header-brand">
                        <h1 class="m-0">
                            <a href="#">
								<svg width="32" height="32" xmlns="http://www.w3.org/2000/svg">
								    <defs>
								        <linearGradient x1="114.674%" y1="39.507%" x2="-52.998%" y2="39.507%" id="logo-a">
								            <stop stop-color="#8D92FA" offset="0%"></stop>
								            <stop stop-color="#8D92FA" stop-opacity="0" offset="100%"></stop>
								        </linearGradient>
								        <linearGradient x1="93.05%" y1="19.767%" x2="15.034%" y2="85.765%" id="logo-b">
								            <stop stop-color="#FF3058" offset="0%"></stop>
								            <stop stop-color="#FF6381" offset="100%"></stop>
								        </linearGradient>
								        <linearGradient x1="32.716%" y1="-20.176%" x2="32.716%" y2="148.747%" id="logo-c">
								            <stop stop-color="#FF97AA" offset="0%"></stop>
								            <stop stop-color="#FF97AA" stop-opacity="0" offset="100%"></stop>
								        </linearGradient>
								    </defs>
								    <g fill="none" fill-rule="evenodd">
								    </g>
								</svg>
                            </a>
                        </h1>
                    </div>
                </div>
            </div>
        </header>

        <main>
            <section class="hero">
                <div class="container">
                    <div class="hero-inner">
						<div class="hero-copy">
	                        <h1 class="hero-title mt-0">Koodi.ML</h1>
	                        <p class="hero-paragraph">Koodi.ML on sivu jolla voit luoda koodin joka uudelleenohjaa linkkiin! Luo koodi kirjoittamalla "koodi.ml" linkkisi eteen. Jos sinulla on jo koodi voit kirjoittaa sen tähä.</p>
							<div class="hero-form field field-grouped">
								<div class="control control-expanded">
									<input class="input" type="number" name="code" placeholder="Koodi">
								</div>
								<div class="control">
									<a class="button button-primary button-block" href="#">Mene!</a>
								</div>
							</div>
						</div>
						<div class="hero-illustration">
							<div class="hero-shape hero-shape-1">
								<svg width="40" height="40" xmlns="http://www.w3.org/2000/svg" style="overflow:visible">
									<circle class="anime-element fadeup-animation" cx="20" cy="20" r="20" fill="#FFD8CD" fill-rule="evenodd" style="opacity: 1; transform: translateY(0px);"></circle>
								</svg>
							</div>
							<div class="hero-shape hero-shape-2">
								<svg width="88" height="88" xmlns="http://www.w3.org/2000/svg" style="overflow:visible">
								    <circle class="anime-element fadeup-animation" cx="44" cy="44" r="44" fill="#FFD2DA" fill-rule="evenodd" style="opacity: 1; transform: translateY(0px);"></circle>
								</svg>
							</div>
							<div class="hero-main-shape">
								<svg width="940" height="647" viewBox="0 0 940 647" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="overflow:visible">
									<defs>
										<linearGradient x1="100%" y1="0%" x2="0%" y2="100%" id="hero-illustration-a">
											<stop stop-color="#261FB6" offset="0%"></stop>
											<stop stop-color="#4950F6" offset="100%"></stop>
										</linearGradient>
										<linearGradient x1="89.764%" y1="16.809%" x2="11.987%" y2="82.178%" id="hero-illustration-b">
											<stop stop-color="#FC8464" offset="0%"></stop>
											<stop stop-color="#FB5C32" offset="100%"></stop>
										</linearGradient>
										<linearGradient x1="100%" y1="23.096%" x2="4.439%" y2="96.586%" id="hero-illustration-c">
											<stop stop-color="#1ADAB7" offset="0%"></stop>
											<stop stop-color="#55EBD0" offset="100%"></stop>
										</linearGradient>
										<filter x="-13%" y="-150%" width="126.1%" height="400%" filterUnits="objectBoundingBox" id="hero-illustration-d">
											<feGaussianBlur stdDeviation="32" in="SourceGraphic"></feGaussianBlur>
										</filter>
										<linearGradient x1="0%" y1="100%" x2="46.694%" y2="42.915%" id="hero-illustration-f">
											<stop stop-color="#EEF1FA" offset="0%"></stop>
											<stop stop-color="#FFF" offset="100%"></stop>
										</linearGradient>
										<rect id="hero-illustration-e" width="800" height="450" rx="4"></rect>
										<linearGradient x1="100%" y1="-12.816%" x2="0%" y2="-12.816%" id="hero-illustration-g">
											<stop stop-color="#D2DAF0" stop-opacity="0" offset="0%"></stop>
											<stop stop-color="#D2DAF0" offset="50.045%"></stop>
											<stop stop-color="#D2DAF0" stop-opacity="0" offset="100%"></stop>
										</linearGradient>
										<linearGradient x1="116.514%" y1="-21.201%" x2="0%" y2="100%" id="hero-illustration-h">
											<stop stop-color="#55EBD0" offset="0%"></stop>
											<stop stop-color="#4950F6" offset="100%"></stop>
										</linearGradient>
										<path id="hero-illustration-j" d="M0 0h308v288H0z"></path>
										<filter x="-15.6%" y="-12.5%" width="139%" height="141.7%" filterUnits="objectBoundingBox" id="hero-illustration-i">
											<feOffset dx="12" dy="24" in="SourceAlpha" result="shadowOffsetOuter1"></feOffset>
											<feGaussianBlur stdDeviation="16" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
											<feColorMatrix values="0 0 0 0 0.0666666667 0 0 0 0 0.062745098 0 0 0 0 0.243137255 0 0 0 0.08 0" in="shadowBlurOuter1"></feColorMatrix>
										</filter>
										<circle id="hero-illustration-k" cx="16" cy="16" r="16"></circle>
										<linearGradient x1="50%" y1="0%" x2="50%" y2="100%" id="hero-illustration-m">
											<stop stop-color="#C6FDF3" offset="0%"></stop>
											<stop stop-color="#C6FDF3" stop-opacity="0" offset="100%"></stop>
										</linearGradient>
										<linearGradient x1="2.875%" y1="89.028%" x2="99.412%" y2="6.885%" id="hero-illustration-n">
											<stop stop-color="#83F0DD" offset="0%"></stop>
											<stop stop-color="#1ADAB7" offset="50.924%"></stop>
											<stop stop-color="#55EBD0" offset="100%"></stop>
										</linearGradient>
										<linearGradient x1="50%" y1="1.569%" x2="50%" y2="97.315%" id="hero-illustration-o">
											<stop stop-color="#FF97AA" offset="0%"></stop>
											<stop stop-color="#FF6381" offset="100%"></stop>
										</linearGradient>
										<linearGradient x1="50%" y1="0%" x2="50%" y2="100%" id="hero-illustration-p">
											<stop stop-color="#FCAC96" offset="0%"></stop>
											<stop stop-color="#FC8464" offset="100%"></stop>
										</linearGradient>
										<circle id="hero-illustration-r" cx="28" cy="28" r="28"></circle>
										<filter x="-85.7%" y="-64.3%" width="314.3%" height="314.3%" filterUnits="objectBoundingBox" id="hero-illustration-q">
											<feOffset dx="12" dy="24" in="SourceAlpha" result="shadowOffsetOuter1"></feOffset>
											<feGaussianBlur stdDeviation="16" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
											<feColorMatrix values="0 0 0 0 0.0666666667 0 0 0 0 0.062745098 0 0 0 0 0.243137255 0 0 0 0.08 0" in="shadowBlurOuter1"></feColorMatrix>
										</filter>
										<circle id="hero-illustration-t" cx="36" cy="36" r="36"></circle>
										<filter x="-66.7%" y="-50%" width="266.7%" height="266.7%" filterUnits="objectBoundingBox" id="hero-illustration-s">
											<feOffset dx="12" dy="24" in="SourceAlpha" result="shadowOffsetOuter1"></feOffset>
											<feGaussianBlur stdDeviation="16" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
											<feColorMatrix values="0 0 0 0 0.0666666667 0 0 0 0 0.062745098 0 0 0 0 0.243137255 0 0 0 0.08 0" in="shadowBlurOuter1"></feColorMatrix>
										</filter>
										<circle id="hero-illustration-v" cx="28" cy="28" r="28"></circle>
										<filter x="-85.7%" y="-64.3%" width="314.3%" height="314.3%" filterUnits="objectBoundingBox" id="hero-illustration-u">
											<feOffset dx="12" dy="24" in="SourceAlpha" result="shadowOffsetOuter1"></feOffset>
											<feGaussianBlur stdDeviation="16" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
											<feColorMatrix values="0 0 0 0 0.0666666667 0 0 0 0 0.062745098 0 0 0 0 0.243137255 0 0 0 0.08 0" in="shadowBlurOuter1"></feColorMatrix>
										</filter>
										<circle id="hero-illustration-x" cx="24" cy="24" r="24"></circle>
										<filter x="-100%" y="-75%" width="350%" height="350%" filterUnits="objectBoundingBox" id="hero-illustration-w">
											<feOffset dx="12" dy="24" in="SourceAlpha" result="shadowOffsetOuter1"></feOffset>
											<feGaussianBlur stdDeviation="16" in="shadowOffsetOuter1" result="shadowBlurOuter1"></feGaussianBlur>
											<feColorMatrix values="0 0 0 0 0.0666666667 0 0 0 0 0.062745098 0 0 0 0 0.243137255 0 0 0 0.08 0" in="shadowBlurOuter1"></feColorMatrix>
										</filter>
									</defs>
									
								</svg>
							</div>
                        </div>
                    </div>
                </div>
            </section>
        </main>
    </div>
    <script src="https://cruip.com/wp-content/themes/cruip-2/dist/js/main.min.js?ver=1.0.17"></script>
</body></html>"