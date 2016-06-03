from bs4 import BeautifulSoup
import requests
import MySQLdb
conn = MySQLdb.connect("localhost","root","justgoogleit","results" )
cursor = conn.cursor()
arr = [17,13,9,5]
def push_students(rollno,name,cgpi):
	try:
	    cursor.execute('''UPDATE students SET cgpi=%s where roll_no=%s''',(cgpi, rollno))
	   # cursor.execute('''INSERT into students (roll_no,name,cgpi) values (%s,%s,%s)''',(rollno,name,cgpi))
	    conn.commit()
	except:
	    print conn.rollback()
	    print ("MKK")
def push_semester(rollno,semester,sgpi,cgpi):
	try:
	    cursor.execute('''INSERT into semesters (roll_no,sgpi,cgpi,semester_no) values (%s,%s,%s,%s)''',(rollno,sgpi,cgpi,semester))
	    conn.commit()
	except:
	    print conn.rollback()
def push_subjects(id1,rollno,semester,subname,obtainCR,totalCR):
	try:
	    cursor.execute('''INSERT into subjects (id,roll_no,semester_no,subject_name,obtainCR,TotalCR) values (%s,%s,%s,%s,%s,%s)''',(id1,rollno,semester,subname,obtainCR,totalCR))
	    conn.commit()
	except:
	    print conn.rollback()

def btech():
	roll_2="1"
	for year in range(4):
		roll_2 = roll_2+str(year+3)
		print "Year"+roll_2
		roll2 = roll_2
		for branch in range(7):
			roll_2 = roll_2 + str(branch+1)
			print "Branch"+roll_2
			roll3 = roll_2
			for roll_no in range(99):
				if roll_no<9:
					roll_2 = roll_2 + "0" + str(roll_no+1)
				else:
					roll_2 = roll_2 + str(roll_no+1)
				print roll_2 + " Site "+ roll2
				form_data={
					'RollNumber' : roll_2
				}
				url = "http://14.139.56.15/scheme"+str(roll2)+"/studentresult/details.asp"
				response = requests.post(url, data = form_data)
				page=BeautifulSoup(response.text)
				#print page.prettify()
				table=page.find_all('table', class_='ewTable')
				roll="1"+str(year+3)

				if len(table)<arr[year+1]:
					roll_2 = roll3
					continue
				tr=table[arr[year+1]-1].find_all('tr')
				td=tr[1].find_all('td', class_='auto-style5')
				nametr=table[0].find_all('tr')
				nametd=nametr[0].find_all('td', class_='auto-style5')
				print (nametd[1].text).strip()	
				x = (td[2].text)	
				print x[x.find("=")+1:]
				push_students(roll_2,(nametd[1].text).strip(),x[x.find("=")+1:])
				print "Name: "+ (nametd[1].text).strip()+" SGPI: "+ x[x.find("=")+1:]
				for k in range(arr[year+1]/2):
					tables = page.find_all('table',class_='ewTable')
					trs = tables[k*2+2].find_all('tr')
					tds = trs[1].find_all('td',class_='auto-style5')
					x1 = (tds[0].text)
					y1 = (tds[2].text)
					print x1
					print y1
					push_semester(roll_2,roll_2+str(k+1),x1[x1.find("=")+1:],y1[y1.find("=")+1:])
					trs2 = tables[k*2+1].find_all('tr')
					#print trs2
					subjectnum = len(trs2)
					#print type(subjectnum)
					#print subjectnum
					#print "MKKKKK"
					for l in range(subjectnum-1):
						tds2 = trs2[1+l].find_all('td',class_='auto-style5')
						subname = (tds2[1].text).strip()
						#subptr = int(tds2[5].text)/
						push_subjects(roll_2+str(k+1)+tds2[0].text,roll_2,roll_2+str(k+1),subname,tds2[5].text,str(10*int(tds2[3].text)))
				roll_2 = roll3
			roll_2 = roll2
		roll_2 = "1"
def dual():
	roll_2="1"
	site = "1"
	for year in range(2):
		roll_2 = roll_2+str(year+4)+"MI"
		site = site+str(year+4)
		print "Year"+roll_2
		roll2 = roll_2
		for branch in range(2):
			roll_2 = roll_2 + str(branch+4)
			roll3 = roll_2
			print "Branch"+roll3
			for roll_no in range(60):
				if roll_no<9:
					roll_2 = roll_2 + "0" + str(roll_no+1)
				else:
					roll_2 = roll_2 + str(roll_no+1)
				print roll_2 + " Site "+site
				form_data={
					'RollNumber' : roll_2
				}
				url = "http://14.139.56.15/scheme"+str(site)+"/studentresult/details.asp"
				response = requests.post(url, data = form_data)
				page=BeautifulSoup(response.text)
				#print page.prettify()
				table=page.find_all('table', class_='ewTable')
				roll="1"+str(year+3)
				#print "Table Length: "+ str(len(table))
				if len(table)<arr[year+2]:
					roll_2 = roll3
					continue
				tr=table[arr[year+2]-1].find_all('tr')
				td=tr[1].find_all('td', class_='auto-style5')
				nametr=table[0].find_all('tr')
				nametd=nametr[0].find_all('td', class_='auto-style5')
				print (nametd[1].text).strip()	
				x = (td[2].text)	
				print x[x.find("=")+2:]
				push_students(roll_2,(nametd[1].text).strip(),x[x.find("=")+1:])
				print "Name: "+ (nametd[1].text).strip()+" SGPI: "+ x[x.find("=")+1:]
				for k in range(arr[year+2]/2):
					tables = page.find_all('table',class_='ewTable')
					trs = tables[k*2+2].find_all('tr')
					tds = trs[1].find_all('td',class_='auto-style5')
					x1 = (tds[0].text)
					y1 = (tds[2].text)
					print x1
					print y1
					push_semester(roll_2,roll_2+str(k+1),x1[x1.find("=")+1:],y1[y1.find("=")+1:])
					trs2 = tables[k*2+1].find_all('tr')
					#print trs2
					subjectnum = len(trs2)
					#print type(subjectnum)
					#print subjectnum
					#print "MKKKKK"
					for l in range(subjectnum-1):
						tds2 = trs2[1+l].find_all('td',class_='auto-style5')
						subname = (tds2[1].text).strip()
						#subptr = int(tds2[5].text)/
						push_subjects(roll_2+str(k+1)+tds2[0].text,roll_2,roll_2+str(k+1),subname,tds2[5].text,str(10*int(tds2[3].text)))
				roll_2 = roll3
			roll_2 = roll2
		roll_2 = "1"
		site = "1"
def iiit():
	roll_2="IIITU1"
	site = "iiituna1"
	for year in range(2):
		roll_2 = roll_2+str(year+4)
		site = site+str(year+4)
		print "Year"+roll_2
		roll2 = roll_2
		for branch in range(2):
			roll_2 = roll_2 + str(branch+1)
			print "Branch"+roll_2
			roll3 = roll_2
			print "ROll3 " +roll3;
			for roll_no in range(30):
				if roll_no<9:
					roll_2 = roll_2 + "0" + str(roll_no+1)
				else:
					roll_2 = roll_2 + str(roll_no+1)
				print roll_2
				form_data={
						'RollNumber' : roll_2
				}
				url = "http://14.139.56.15/"+str(site)+"/studentresult/details.asp"
				response = requests.post(url, data = form_data)
				page=BeautifulSoup(response.text)
				table=page.find_all('table', class_='ewTable')
				roll="IIITU1"+str(year+4)

				if len(table)<arr[year+2]:
					roll_2 = roll3
					continue
				tr=table[arr[year+2]-1].find_all('tr')
				td=tr[1].find_all('td', class_='ewTableAltRow')
				nametr=table[0].find_all('tr')
				nametd=nametr[0].find_all('td', class_='ewTableAltRow')
				print (nametd[0].text).strip()	
				x = (td[2].text)	
				print "Name: "+ (nametd[0].text).strip()+" SGPI: "+ x[x.find("=")+1:]
				push_students(roll_2,(nametd[0].text).strip(),x[x.find("=")+1:])
				for k in range(arr[year+2]/2):
					tables = page.find_all('table',class_='ewTable')
					trs = tables[k*2+2].find_all('tr')
					tds = trs[1].find_all('td',class_='ewTableAltRow')
					x1 = (tds[0].text)
					y1 = (tds[2].text)
					print x1
					print y1
					push_semester(roll_2,roll_2+str(k+1),x1[x1.find("=")+1:],y1[y1.find("=")+1:])
					trs2 = tables[k*2+1].find_all('tr')
					#print trs2
					subjectnum = len(trs2)
					#print type(subjectnum)
					#print subjectnum
					#print "MKKKKK"
					for l in range(subjectnum-1):
						tds2 = trs2[1+l].find_all('td',class_='ewTableAltRow')
						subname = (tds2[1].text).strip()
						#subptr = int(tds2[5].text)/
						push_subjects(roll_2+str(k+1)+tds2[0].text,roll_2,roll_2+str(k+1),subname,tds2[5].text,str(10*int(tds2[3].text)))
				roll_2 = roll3
			roll_2 = roll2
		roll_2 = "IIITU1"
		site = "iiituna1"
def mtech():
	roll_2="1"
	site = "1"
	for year in range(2):
		roll_2 = roll_2+str(year+4)+"M"
		site = site+str(year+4)
		print "Year"+roll_2
		roll2 = roll_2
		for branch in range(7):
			roll_2 = roll_2 + str(branch+6)
			roll3 = roll_2
			print "Branch"+roll3
			for roll_no in range(60):
				if roll_no<9:
					roll_2 = roll_2 + "0" + str(roll_no+1)
				else:
					roll_2 = roll_2 + str(roll_no+1)
				print roll_2 + " Site "+site
				form_data={
					'RollNumber' : roll_2
				}
				url = "http://14.139.56.15/mtech"+str(site)+"/studentresult/details.asp"
				response = requests.post(url, data = form_data)
				page=BeautifulSoup(response.text)
				#print page.prettify()
				table=page.find_all('table', class_='ewTable')
				roll="IIITU1"+str(year+5)

				if len(table)<arr[year+3]:
					roll_2 = roll3
					continue
				tr=table[arr[year+3]-1].find_all('tr')
				td=tr[1].find_all('td', class_='ewTableAltRow')
				nametr=table[0].find_all('tr')
				nametd=nametr[0].find_all('td', class_='ewTableAltRow')
				print (nametd[0].text).strip()	
				x = (td[2].text)	
				print "Name: "+ (nametd[0].text).strip()+" SGPI: "+ x[x.find("=")+1:]
				push_students(roll_2,(nametd[0].text).strip(),x[x.find("=")+1:])
				for k in range(arr[year+3]/2):
					tables = page.find_all('table',class_='ewTable')
					trs = tables[k*2+2].find_all('tr')
					tds = trs[1].find_all('td',class_='ewTableAltRow')
					x1 = (tds[0].text)
					y1 = (tds[2].text)
					print x1
					print y1
					push_semester(roll_2,roll_2+str(k+1),x1[x1.find("=")+1:],y1[y1.find("=")+1:])
					trs2 = tables[k*2+1].find_all('tr')
					#print trs2
					subjectnum = len(trs2)
					#print type(subjectnum)
					#print subjectnum
					#print "MKKKKK"
					for l in range(subjectnum-1):
						tds2 = trs2[1+l].find_all('td',class_='ewTableAltRow')
						subname = (tds2[1].text).strip()
						#subptr = int(tds2[5].text)/
						push_subjects(roll_2+str(k+1)+tds2[0].text,roll_2,roll_2+str(k+1),subname,tds2[5].text,str(10*int(tds2[3].text)))
				roll_2 = roll3
			roll_2 = roll2
		roll_2 = "1"
		site = "1"
btech()
dual()
iiit()
mtech()
			
