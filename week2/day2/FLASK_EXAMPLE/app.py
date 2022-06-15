from flask import Flask
from views import views
# we import our viewws from the views file

app = Flask(__name__)
# we instantiate the app object

app.register_blueprint(views)
# we register the views Blueprint

if __name__ == "__main__":
    app.run(debug=True, port=8000)

# running the application