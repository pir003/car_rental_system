#Project Flask MVC

from Project import app

app.secret_key = "veldighemmelig"

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)