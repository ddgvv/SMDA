import json
import sqlite3

	
def getQuery(index,queryName):
	with open('data.txt') as json_file:
		data = json.load(json_file)
		return data['query'][index][queryName]

def runQuery(index,queryName):
	conn = sqlite3.connect('test.db')
	conn.execute(getQuery(index,queryName))
	conn.commit()
	print ("Table created successfully")

def runQueryWithArgs(index,queryName,args):
	conn = sqlite3.connect('test.db')
	conn.execute(getQuery(index,queryName),args)
	conn.commit()
	conn.close()

def selectData(index,queryName,args):
	conn = sqlite3.connect('test.db')
	cursor = conn.execute(getQuery(index,queryName),args)
	res= cursor.fetchall()
	conn.close()
	print(res)
	return res
#-----------------------TABLE CREATION -------------------------
#runQuery(0,"create")
#runQuery(1,"create")
#runQuery(2,"create")


#----------------------TABLE INSERT------------------------------

#runQueryWithArgs(0,"insert",(1,'Expence'))
#runQueryWithArgs(0,"insert",(2,'Income'))
#runQueryWithArgs(0,"insert",(3,'Future Expence'))
#runQueryWithArgs(0,"insert",(4,'Future Income'))
#runQueryWithArgs(0,"insert",(5,'Loan Account'))
#runQueryWithArgs(0,"insert",(6,'Bank Account'))

#runQueryWithArgs(1,"insert",("coffee",1))
#runQueryWithArgs(1,"insert",("tea",1))
#runQueryWithArgs(1,"insert",("BS",2))

#runQueryWithArgs(2,"insert",(3,1,300,"2019-11-07","tea break"))

#----------------------TABLE DELETE ------------------------------


#----------------------TABLE UPDATE ------------------------------

#runQueryWithArgs(1,"update",("gvvigneswar",4,6))

#----------------------TABLE SHOW --------------------------------

#print(selectData(0,"show",''))
#print(selectData(1,"show",''))
#print(selectData(2,"show",''))


