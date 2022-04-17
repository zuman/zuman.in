from zuman import create_app
from dotenv import load_dotenv

app = create_app()

if __name__ == "__main__":
    load_dotenv('../.env')
    app.run(host="0.0.0.0")
