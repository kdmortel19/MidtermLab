from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('phoneNumber')
        message = request.form.get('message')
        subject = request.form.get('subject')
        preferredContactMethod = request.form.get('preferredContactMethod')
        agreement = request.form.get('agreement')


        print(f"New message from {name} ({email}):{number} {message} {subject} {preferredContactMethod} {agreement}")


        return redirect(url_for('success'))


    return render_template('contact.html')


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run()