from flask import Flask, request, render_template, redirect, jsonify, make_response
import jwt
import datetime

app = Flask(__name__)
SECRET = "pasosdegigante"

users = {
    "admin": {"password": "adminpass", "role": "admin"}
}

FLAG = "CTF{netcomdays_jwt_exposed}"

def create_token(username, role):
    payload = {
        "username": username,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form.get("username")
        passwd = request.form.get("password")
        user = users.get(uname)
        if user and user["password"] == passwd:
            token = create_token(uname, user["role"])
            resp = make_response(redirect("/dashboard"))
            resp.set_cookie("token", token)
            return resp
        return "Invalid credentials", 403
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form.get("username")
        passwd = request.form.get("password")
        if uname in users:
            return "Username already exists!", 400
        users[uname] = {"password": passwd, "role": "user"}
        return redirect("/login")
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    token = request.cookies.get("token")
    if not token:
        return redirect("/login")
    try:
        data = jwt.decode(token, SECRET, algorithms=["HS256"])
        is_admin = data.get("role") == "admin"
        return render_template("dashboard.html", user=data["username"], is_admin=is_admin, flag=FLAG if is_admin else None)
    except jwt.ExpiredSignatureError:
        return "Token expired", 403
    except jwt.InvalidTokenError:
        return "Invalid token", 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context=("cert.pem", "key.pem"))
