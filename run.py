#!/home/usernamehere/miniconda3/envs/flaskblog_env/bin/python
from flaskblog import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
