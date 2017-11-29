from flask import Flask, render_template

def create_app():
    app = Flask(
        __name__,
        static_folder='../static/dist',
        template_folder='../static')
    
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/habits/')
    def list_habits():
        return '[]'
    
    return app
