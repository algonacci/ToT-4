from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'your_secret_key'

csrf = CSRFProtect(app)


class CSRFDemoForm(FlaskForm):
    name = StringField('Nama:')
    submit = SubmitField('Kirim')


class NoCSRFDemoForm(FlaskForm):
    name = StringField('Nama:')
    submit = SubmitField('Kirim')


@app.route('/csrf', methods=['GET', 'POST'])
def csrf_demo():
    form = CSRFDemoForm()
    if form.validate_on_submit():
        flash(f'Hello, {form.name.data} (dengan CSRF)!', 'success')
        return redirect(url_for('csrf_demo'))
    return render_template('03_csrf/csrf_demo.html', form=form)


@app.route('/no_csrf', methods=['GET', 'POST'])
def no_csrf_demo():
    form = NoCSRFDemoForm()
    if form.validate_on_submit():
        flash(f'Hello, {form.name.data} (tanpa CSRF)!', 'success')
        return redirect(url_for('no_csrf_demo'))
    return render_template('03_csrf/no_csrf_demo.html', form=form)


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return str(name)
    else:
        return render_template('03_csrf/form.html')


if __name__ == '__main__':
    app.run(debug=True)
