from flask import Blueprint, request, render_template, redirect, url_for, session
from models import get_conn

# 创建 auth 蓝图
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if user:
            session['username'] = username
            return redirect(url_for('main.index'))
        else:
            return "用户名或密码错误，<a href='/login'>重试</a>"
    # GET 请求时显示登录表单（直接返回HTML，不依赖模板文件）
    return '''
        <form method="post">
            用户名：<input type="text" name="username"><br><br>
            密码：<input type="password" name="password"><br><br>
            <input type="submit" value="登录">
        </form>
    '''

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('auth.login'))