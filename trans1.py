import MySQLdb as mdb
import datetime

class Transfer:
	RefSN = None
	def GetData(self, index):
		conn = mdb.connect(host='127.0.0.1', port=3306, user='root', passwd='trumon123', db='Trumon')
		cur = conn.cursor()
		query = ("SELECT * FROM Trumon.Image where RefSN = %s");
		cur.execute(query, (index,))
		records = cur.fetchall()
       		self.RefSN = records[0][0]
        	conn.close()
        	cur.close()
        	self.UpdateData(index)

    	def UpdateData(self, index):
        	conn = mdb.connect(host='127.0.0.1', port=3306, user='root', passwd='trumon123', db='Trumon')
		cur = conn.cursor()
		query = ("""UPDATE Trumon.Teks set RefSNimage = %s where RefSN = %s""");
		cur.execute(query, (self.RefSN, index))
		# accept changes 
        	conn.commit()
        	conn.close()
        	cur.close()


# Main Script
conn = mdb.connect(host='127.0.0.1', port=3306, user='root', passwd='trumon123', db='Trumon')
cur =conn.cursor()
cur.execute("""SELECT * FROM Trumon.Teks""")
record = cur.fetchall()
i = 0

for row in record:
	print "hore"
	i=i+1
	print i
	indexman = row[2]
	trans  = Transfer()
    	trans.GetData(indexman)

cur.close()
conn.close()
print "selesai"
