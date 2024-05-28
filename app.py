from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def clubeterra():
    return render_template('index.html')

@app.route('/containers', methods=['GET'])
def containers():
    return render_template('container.html')


if __name__ == '__main__':
    app.run(debug=True)