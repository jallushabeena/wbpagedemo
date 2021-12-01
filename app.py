from flask import Flask,render_template,url_for
app=Flask(__name__)
@app.route('/show')
def show():
    return render_template('index.html',title='MY OWN WEBSITE')

if __name__=='__main__':
    app.run(debug=True)