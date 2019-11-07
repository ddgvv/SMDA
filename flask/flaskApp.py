import flask
from flask import request, jsonify,render_template,redirect
import cgi  
import sqlitDb

sql = sqlitDb
accTypes=sql.selectData(0,"show",'')

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET','POST'])
def smda():
    return render_template('home.html')
	
@app.route('/acc', methods=['GET','POST'])
def accounts():
    return render_template('acc.html')
	
@app.route('/acc/create', methods=['GET','POST'])
def accountsCreation():
	return render_template('CreateAcc.html',accType=accTypes)	

@app.route('/acc/modify', methods=['GET','POST'])
def accountsModify():
	list=sql.selectData(1,"show",'')
	return render_template('ModifyAcc.html',list=list,res='',accType=accTypes)	
	
@app.route('/getAcc', methods=['GET','POST'])
def accountsModifyGetSelected():
	acc = request.form['acc']
	list=sql.selectData(1,"show",'')
	res=sql.selectData(1,"showQuery",(acc))
	return render_template('ModifyAcc.html',list=list,res=res[0],accType=accTypes)		

@app.route('/acc/del', methods=['GET','POST'])
def accountsDeletion():
	res=sql.selectData(1,"show",'')
	return render_template('DeleteAcc.html',list=res)	

@app.route('/acc/show', methods=['GET','POST'])
def accountsShow():
	res=sql.selectData(1,"show",'')
	return render_template('ShowAcc.html',list=res)	
	
@app.route('/insertAcc', methods=['GET','POST'])
def accountsInsert():
	name = request.form['name']
	accType = request.form['accType']
	sql.runQueryWithArgs(1,"insert",(name,accType))
	return redirect('/acc/show')	

@app.route('/delAcc', methods=['GET','POST'])
def accountsDelete():
	acc = request.form['acc']
	sql.runQueryWithArgs(1,"delete",(acc))
	return redirect('/acc/show')	

@app.route('/updateAcc', methods=['GET','POST'])
def accountsUpdate():
	name = request.form['name']
	accType = request.form['accType']
	id = request.form['id']
	sql.runQueryWithArgs(1,"update",(name,accType,id))
	print("hi")
	return redirect('/acc/show')	

@app.route('/entry', methods=['GET','POST'])
def entry():
	fromAcc=sql.selectData(1,"from",'')
	toAcc=sql.selectData(1,"to",'')
	return render_template('doEntry.html',fromAcc=fromAcc,toAcc=toAcc)
	
	

	
	
@app.route('/pdf', methods=['GET','POST'])
def pdf():
    return render_template('txt.jsp')	
	
def create_app():
	return app
		
	
app.run()
