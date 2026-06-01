from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return render_template('login.html', 
                               method=request.method,
                               username=username,
                               password=password,
                               show_result=True)
    else:
        return render_template('login.html', show_result=False)

if __name__ == '__main__':
    app.run(debug=True)