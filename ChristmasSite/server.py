from flask import Flask, render_template
import yaml
import os

app = Flask(__name__)

#TODO: Clean this up.
config_file = os.path.join(os.path.join(os.getcwd(), 'config'), 'config.yml')
with open(config_file) as stream:
    config = yaml.load(stream)

def main():
    """ Primary access point """

    import argparse
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--host', help='bind address', type=str, default=config['host'])
    parser.add_argument('--port', help='bind port', type=int, default=config['port'])
    args = parser.parse_args()

    app.jinja_env.globals.update(parse_endpoint=config['endpoint'])

    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    
    app.run(host=args.host, port=args.port)

@app.route("/", methods=['GET'])
def server():
    users = ['']
    users.extend(config['settings']['user_list'])
    return render_template('main_page.html', users=users)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':
    main()