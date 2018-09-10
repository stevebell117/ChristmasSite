from flask import Flask, render_template
try:
    from ChristmasSite.config import Config
except:
    from config import Config
app = Flask(__name__)

config = Config()

def main():
    """ Primary access point """

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='bind address', type=str, default=config.host)
    parser.add_argument('--port', help='bind port', type=int, default=config.port)
    args = parser.parse_args()

    app.jinja_env.globals.update(parse_endpoint=config.endpoint)

    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    
    app.run(host=args.host, port=args.port)

@app.route("/", methods=['GET'])
def server():
    return render_template('main_page.html', name='Steven')

if __name__ == '__main__':
    main()