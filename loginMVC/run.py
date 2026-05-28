from flask import Flask, render_template, redirect, url_for, session, request, jsonify
from models import LoginForm
import random
import string
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'   # CSRF密钥

# ========== 验证码生成 ==========
def generate_captcha():
    """生成4位随机验证码（字母数字混合）"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

# ========== 数据库配置 ==========
DB_CONFIG = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',          
    'database': 'login_demo',
    'charset': 'utf8mb4'
}

def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

# ========== 路由 ==========
@app.route('/')
def index():
    """登录成功后的主页"""
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None

    # 生成或获取验证码（存入session）
    if 'captcha' not in session:
        session['captcha'] = generate_captcha()

    if form.validate_on_submit():
        # 验证码校验
        if form.captcha.data.upper() != session.get('captcha', '').upper():
            error = '验证码错误'
        else:
            username = form.username.data
            password = form.password.data

           
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
            row = cursor.fetchone()
            cursor.close()
            conn.close()

            if row and password == row[0]:   # 明文比较
                session['username'] = username
                session.pop('captcha', None)
                return redirect(url_for('index'))
            else:
                error = '用户名或密码错误'
        # 验证失败时刷新验证码
        if error:
            session['captcha'] = generate_captcha()

    return render_template('login.html', form=form, error=error, captcha=session.get('captcha'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# 验证码刷新接口（AJAX）
@app.route('/refresh-captcha')
def refresh_captcha():
    new_captcha = generate_captcha()
    session['captcha'] = new_captcha
    return jsonify({'captcha': new_captcha})

if __name__ == '__main__':
    app.run(debug=True)