import os
from app import create_app


settings_name = os.getenv('FLASK_CONFIG')
app = create_app(settings_name)

if __name__ == '__main__':
    app.run()