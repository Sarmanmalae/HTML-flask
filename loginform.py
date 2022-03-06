from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astr = IntegerField('Id астронавта', validators=[DataRequired()])
    passw_astr = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = IntegerField('Id капитана', validators=[DataRequired()])
    passw_cap = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')
