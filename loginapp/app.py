from flask import Flask
from auth import auth_bp
from main import main_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'   # 请修改为随机字符串
    
    # 注册蓝图
    app.register_blueprint(main_bp)       # 主蓝图，前缀默认为 '/'
    app.register_blueprint(auth_bp)       # 认证蓝图，前缀默认为 '/'
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)