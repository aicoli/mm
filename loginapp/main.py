from flask import Blueprint, session

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    if 'username' in session:
        return f'欢迎 {session["username"]}！ <a href="/logout">退出</a>'
    return '<a href="/login">登录</a>'