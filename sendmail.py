from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Email server configuration
        SMTP_SERVER = "smtp.example.com"
        SMTP_PORT = 587
        SMTP_USERNAME = "username"
        SMTP_PASSWORD = "password"

        # Create the email message
        msg = f"From: {name} <{email}>\n"
        msg += f"To: e2001972@vamk.fi\n"
        msg += "Subject: Form Submission\n\n"
        msg += message

        # Send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(email, "e2001972@vamk.fi", msg)

        return 'Email sent!'
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
