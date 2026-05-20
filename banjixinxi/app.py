from flask import Flask, render_template
from model import get_all_class

app = Flask(__name__)

@app.route("/")
def index():
    classes = get_all_class()
    print(f"从数据库获取到 {len(classes)} 条数据")   # 调试输出
    return render_template("index.html", classes=classes)

if __name__ == "__main__":
    app.run(debug=True)