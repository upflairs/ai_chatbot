from nltk.chat.util import Chat, reflections
from flask import Flask, render_template, request

pairs = (
    (r'i like (.*)', 
        (
            'Surely, you can like %1',
            'why, do you like %1?'
        )
    ),
    (r'will you please (.*)', 
        (
            'yeah, sure',
            'no, i can not do this'
        )
    ),
    (r'(.*)python(.*)',
         (
             'python is an interpreted language',
             'python is 4th generation language',
             'python is language of today and tomorrow'             
         )    
    ),
    (r'(.*)machine learning(.*)',
         (
             'machine learning is a branch of AI',
             'machine learning is essential part of data science',  
         )    
    )
)

cb = Chat(pairs, reflections)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(cb.respond(userText))    
