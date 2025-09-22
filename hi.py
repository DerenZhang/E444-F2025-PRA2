from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_moment import Moment
from datetime import datetime, timezone

# ----- Forms -----
class NameEmailForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT Email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

# ----- App -----
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-change-me'   
bootstrap = Bootstrap(app)
moment = Moment(app)

# ----- Routes -----
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameEmailForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        if old_name and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email and old_email != form.email.data:
            flash('Looks like you have changed your email!')

        session['name'] = form.name.data.strip()
        session['email'] = form.email.data.strip()

        is_uoft = 'utoronto' in session['email'].lower()

        return render_template(
            'index.html',
            form=form,
            name=session['name'],
            email=session['email'],
            is_uoft=is_uoft,
            current_time=datetime.now(timezone.utc),
        )

    return render_template(
        'index.html',
        form=form,
        name=None,
        email=None,
        is_uoft=None,
        current_time=datetime.now(timezone.utc),
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
