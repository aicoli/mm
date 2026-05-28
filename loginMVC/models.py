from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    """用户登录表单，包含CSRF保护"""
    username = StringField('用户名', validators=[
        DataRequired(message='用户名不能为空'),
        Length(1, 20, message='用户名长度为1-20字符')
    ])
    password = PasswordField('密码', validators=[
        DataRequired(message='密码不能为空'),
        Length(6, 20, message='密码长度为6-20字符')
    ])
    captcha = StringField('验证码', validators=[
        DataRequired(message='请输入验证码')
    ])
    submit = SubmitField('登录')