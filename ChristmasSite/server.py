from flask import Flask
try:
    from ChristmasSite.config import Config
except:
    from config import Config
app = Flask(__name__)

config = Config()

@app.route("/")
def main():
    """ Primary access point """

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='bind address', type=str, default=config.host)
    parser.add_argument('--port', help='bind port', type=int, default=config.port)
    args = parser.parse_args()

    app.jinja_env.globals.update(parse_endpoint=config.endpoint)
    
    app.run(host=args.host, port=args.port)
    return "Hello World!"

if __name__ == '__main__':
    main()