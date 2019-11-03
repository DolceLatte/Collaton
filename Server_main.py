from flask import Flask, redirect, url_for, request
import CompareChannel
import Recommand_Contents

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['myName']
      return redirect(url_for('success', name=user))
   else:
      user = request.args.get('myName')
      return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")