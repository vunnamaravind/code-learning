from app import create_app
from flask_mail import Mail

app = create_app()
Mail = Mail(app)

if __name__ == '__main__':
    app.run(debug=True)