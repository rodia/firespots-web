from flask import Flask, render_template

app = Flask(__name__)   

@app.route('/')
def main():
    return render_template('laPointMap.html')

@app.route('/heat')
def heat():
    return render_template('laHeatmap.html')

if __name__ == '__main__':
    app.run()