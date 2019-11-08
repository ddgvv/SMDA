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
	
@app.route('/acc/create', methods=['GET','POST'])
def accountsCreation():
	return render_template('/acc/CreateAcc.html',accType=accTypes)	

@app.route('/acc/modify', methods=['GET','POST'])
def accountsModify():
	list=sql.selectData(1,"show",'')
	return render_template('/acc/ModifyAcc.html',list=list,res='',accType=accTypes)	
	
@app.route('/acc/del', methods=['GET','POST'])
def accountsDeletion():
	res=sql.selectData(1,"show",'')
	return render_template('/acc/DeleteAcc.html',list=res)	

@app.route('/acc/show', methods=['GET','POST'])
def accountsShow():
	res=sql.selectData(1,"show",'')
	return render_template('/acc/ShowAcc.html',list=res)	
	
@app.route('/insertAcc', methods=['GET','POST'])
def accountsInsert():
	name = request.form['name']
	accType = request.form['accType']
	sql.runQueryWithArgs(1,"insert",(name,accType))
	return redirect('/acc/show')	

@app.route('/delAcc', methods=['GET','POST'])
def accountsDelete():
	btn = request.form['btn']
	input = request.form['input']
	if btn=='delete':
		sql.runQueryWithArgs(1,"delete",(input,))
	if btn=='Update':
		input = request.form['input']
		list=sql.selectData(1,"show",'')
		res=sql.selectData(1,"showQuery",(input,))
		return render_template('/acc/ModifyAcc.html',list=list,res=res[0],accType=accTypes)
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
	return render_template('/entry/doEntry.html',fromAcc=fromAcc,toAcc=toAcc)
	
@app.route('/insertEntry', methods=['GET','POST'])
def entryInsert():
	desc = request.form['desc']
	fromA = request.form['from']
	toA = request.form['to']
	amt = request.form['amt']
	eDate = request.form['eDate']
	sql.runQueryWithArgs(2,"insert",(fromA,toA,amt,eDate,desc))
	return redirect('/entry/show')	

@app.route('/entry/show', methods=['GET','POST'])
def entryShow():
	res=sql.selectData(2,"show",'')
	print(res)
	return render_template('/entry/ShowEntry.html',list=res)		
	
@app.route('/updateEntry', methods=['GET','POST'])
def updateEntry():
	btn = request.form['btn']
	input = request.form['input']
	if btn=='delete':
		sql.runQueryWithArgs(2,"delete",(input,))
	if btn=='Update':
		fromAcc=sql.selectData(1,"from",'')
		toAcc=sql.selectData(1,"to",'')
		res=sql.selectData(2,"showWhere",(input,))
		print(res)
		return render_template('/entry/ModifyEntry.html',res=res[0],fromAcc=fromAcc,toAcc=toAcc)		
	return redirect('/entry/show')	

@app.route('/entry/update', methods=['GET','POST'])
def entryUpdate():
	desc = request.form['desc']
	fromA = request.form['from']
	toA = request.form['to']
	amt = request.form['amt']
	eDate = request.form['eDate']
	id = request.form['id']
	sql.runQueryWithArgs(2,"update",(fromA,toA,amt,eDate,desc,id))
	return redirect('/entry/show')	
	
@app.route('/pdf', methods=['GET','POST'])
def pdf():
    return render_template('txt.jsp')	
	
def create_app():
	return app
		
	
app.run()
