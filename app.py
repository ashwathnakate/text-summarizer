from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load summarization pipeline
summarizer = pipeline("summarization")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    article = request.form['article']
    if article.strip():
        summary = summarizer(article, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    else:
        summary = "Please enter some text to summarize."
    return render_template('index.html', summary=summary, article=article)

if __name__ == '__main__':
    app.run(debug=False, port=5000, host="0.0.0.0")
