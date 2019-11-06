import flask
from flask import request, jsonify,render_template
import cgi  

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {"id": 0,
     "title": "A Fire Upon the Deep",
     "author": "Vernor Vinge",
     "first_sentence": "The coldsleep itself was dreamless.",
     "year_published": "1992"},
    {"id": 1,
     "title": "The Ones Who Walk Away From Omelas",
     "author": "Ursula K. Le Guin",
     "first_sentence": "With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.",
     "published": "1973"},
    {"id": 2,
     "title": "Dhalgren",
     "author": "Samuel R. Delany",
     "first_sentence": "to wound the autumnal city.",
     "published": "1975"}
]


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)
	

@app.route('/ddlb', methods=['GET'])
def dropdown():
    colours = ['Red', 'Blue', 'Black', 'Orange']
    return render_template('test.html', colours=colours)
	
@app.route('/', methods=['GET'])
def smda():
    return render_template('home.html')
	
@app.route('/acc', methods=['GET'])
def accounts():
    return render_template('acc.html')
	
@app.route('/acc/create', methods=['GET'])
def accountsCreation():
    return render_template('CreateAcc.html')	

@app.route('/acc/modify', methods=['GET'])
def accountsModify():
    return render_template('ModifyAcc.html',list=books,res=books[0])	
	
@app.route('/getAcc', methods=['GET','POST'])
def accountsModifyGetSelected():
	text = request.form['list']
	return render_template('ModifyAcc.html',list=books,res=books[int(text)])		

@app.route('/acc/del', methods=['GET'])
def accountsDeletion():
    return render_template('DeleteAcc.html',list=books)	

@app.route('/acc/show', methods=['GET'])
def accountsShow():
    return render_template('ShowAcc.html',list=books)	
	
@app.route('/insertAcc', methods=['GET'])
def accountsInsert():
    return render_template('CreateAcc.html',colours='success')	
	
@app.route('/pdf', methods=['GET'])
def pdf():
    return render_template('txt.jsp')	
	
	
app.run()
