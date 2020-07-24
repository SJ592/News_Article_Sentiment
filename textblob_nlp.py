from textblob import TextBlob
import flask
from flask import Flask, render_template, request 


app = Flask(__name__)

@app.route('/') # default route
@app.route('/form')

def form():
    return flask.render_template('textblob.html')

@app.route('/result',methods = ['POST'])

def result():
    if request.method == 'POST':
        Title=len(TextBlob(request.form['title']).words)
        Content=len(TextBlob(request.form['content']).words)
        Title_sentiment=TextBlob(request.form["title"]).sentiment.polarity
        Content_sentiment=TextBlob(request.form["content"]).sentiment.polarity
        Title_subjectivity=TextBlob(request.form["title"]).sentiment.subjectivity
        Content_subjectivity=TextBlob(request.form["content"]).sentiment.subjectivity

        return flask.render_template("textblob_result.html",Title=Title,Content=Content,Title_sentiment=Title_sentiment,Content_sentiment=Content_sentiment,Title_subjectivity=Title_subjectivity,Content_subjectivity=Content_subjectivity)

if __name__=='__main__':
	app.run()
