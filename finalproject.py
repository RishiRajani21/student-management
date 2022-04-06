from tkinter import *
from tkinter import messagebox
from webbrowser import*
from tkinter import scrolledtext
from cx_Oracle import *
import socket
import requests
import bs4
import matplotlib.pyplot as plt
import numpy as np

root = Tk()
root.title("S.M.S")
root.geometry("700x700+300+100")
root.configure(background='beige')

try:
	socket.create_connection(("www.google.com",80))
	print("You are connected to the CX_ORACLE DATABASE SUCCESFULLY")
	res = requests.get("http://ipinfo.io")
	data = res.json()
	city = data['city']
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q="+ city
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	api_address = a1 + a2 + a3
	res1 = requests.get(api_address)
	data = res1.json()
	main = data['main']
	temp = main['temp']
	str1 = "Temp: "+str(temp)+"\u00b0"+"C in "+city
	res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
	print("This is response of request of the quote of the day", res)
	soup = bs4.BeautifulSoup(res.text,'lxml')
	quote = soup.find('img',{"class":"p-qotd"})
	quote = quote['alt']

	
except OSError:
	print("check network")

j =0 
templist1 = []
templist2 = []
qList = quote.split(' ')
for i in range(len(qList)//2):
	templist1.append(qList[i])
	j = i
for i in range(j+1,len(qList)):
	templist2.append(qList[i])

msga = ' '.join(templist1)
msgb = ' '.join(templist2)

msg1 = "QOTD: "+ msga+"\n"+msgb

def f1():
	root.withdraw()
	adst.deiconify()
def f2():
	adst.withdraw()
	root.deiconify()
def f3():
	stViewData.delete(1.0,END)
	root.withdraw()
	vist.deiconify()
	con = None
	try:
		con = connect("system/abc123")
		cursor = con.cursor()
		sql = "select * from sms"
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = ""
		for d in data:	
			msg = msg + "Roll Number: = " + str(d[0])+ "| Name: " + str(d[1]) + "\n" + "Mobile Number: " + str(d[2]) + "| Division= " + str(d[3])+ "\n" + "Physics Marks: " +str(d[4])+ "| Chemistry Marks: " +str(d[5]) + "\n" + "Maths Marks: " +str(d[6]) + "\n" + "\n" 
		stViewData.insert(INSERT,msg)
	except DatabaseError as e:
		messagebox.showerror("Try Again",e)
	finally:
		cursor.close()
		if con is not None:
			con.close()
def f4():
	vist.withdraw()
	root.deiconify()

def f5():
	root.withdraw()
	upst.deiconify()
def f6():
	upst.withdraw()
	root.deiconify()
def f7():
	con = None
	try:
		con = connect("system/abc123")
		rno = entAddRno.get()
		if rno.isdigit():
			rno = int(rno)
		else:
			raise Exception("Roll no. cannot contain characters")
		if rno == 0:
			raise Exception("Rno cannot be zero")
		if rno < 1:
			raise Exception("Rno cannot be negative")
		 
		names = entAddName.get()
		name = names.split(' ')
		if not name[0].isalpha():
			raise Exception("Name cannot contain numbers")
		if len(name) < 2: 
			raise Exception("name should consists of 2 char")

        	
		mob = entAddMob.get()
		if mob.isdigit():
			mobstr = str(mob)
			mobl = len(str(mobstr))
			mob = int(mob)

		else:
			raise Exception("mob no. cannot contain characters")

		if mobl == 0:
			raise Exception("mob cannot be zero")
		elif mobl <10:
          		raise Exception("mob no. should be of 10 digits")  
		elif mobl >10:
          		raise Exception("mob no. should not be greater than 10 digits") 
		
		divs = entAddDiv.get()
		div = divs.split(' ')
		if not div[0].isalpha():
			raise Exception("Division cannot contain numbers")
		
		phymarks = int(entAddPhy.get())
		if phymarks < 0 or phymarks > 100:
			raise Exception("Marks out of range 0-100")
		chemmarks = int(entAddChem.get())
		if chemmarks < 0 or chemmarks > 100:
			raise Exception("Marks out of range 0-100")
		mathsmarks = int(entAddMath.get())
		if mathsmarks < 0 or mathsmarks > 100:
			raise Exception("Marks out of range 0-100")
		args = (rno,names,mob,divs,phymarks,chemmarks,mathsmarks)
		cursor = con.cursor()
		sql = "insert into sms values('%d','%s','%d','%s','%d','%d','%d')"
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Done",str(cursor.rowcount) + " Rows Inserted")
	except DatabaseError as e:
		messagebox.showerror("Try Again",e)
		con.rollback()
	except Exception as e:
		messagebox.showerror("Bad Input",e)
	finally:
		if con is not None:
			con.close()
			entAddRno.delete(0, END)
			entAddName.delete(0, END)
			entAddMob.delete(0, END)
			entAddDiv.delete(0, END)
			entAddPhy.delete(0, END)
			entAddChem.delete(0, END)
			entAddMath.delete(0, END)
			entAddRno.focus()

def f8():
	con = None
	try:
		con = connect("system/abc123")
		rno = entUpdateRno.get()
		cursor = con.cursor()
		if rno.isdigit():
			rno = int(rno)
		else:
			raise Exception("Roll no. cannot contain characters")
		if rno is 0:
			raise Exception("Roll no. cannot be zero")
		if rno < 0:
			raise Exception("Roll no. should be positive")
		names = entUpdateName.get()
		name = names.split(' ')
		if not name[0].isalpha():
			raise Exception("Name cannot contain numbers")
		elif len(name[0])<2:
			raise Exception("Name cannot be of one character")

		mob = entUpdateMob.get()
		if mob.isdigit():
			mobstr = str(mob)
			mobl = len(str(mobstr))
			mob = int(mob)
			
			
		else:
			raise Exception("mob no. cannot contain characters")

		if mobl == 0:
			raise Exception("mob cannot be zero")
		elif mobl <10:
          		raise Exception("mob no. should be of 10 digits")  
		elif mobl >10:
          		raise Exception("mob no. should not be greater than 10 digits") 
		
		divs = entUpdateDiv.get()
		div = divs.split(' ')
		if not div[0].isalpha():
			raise Exception("Division cannot contain numbers")
	
		
		phymarks = entUpdatePhyMarks.get()
		if phymarks.isdigit():
			phymarks = int(phymarks)
			
		else:
			raise Exception("Marks cannot contain Characters")
		if phymarks < 0:
			raise Exception("Marks cannot be negative")
		elif phymarks>100:
			raise Exception("Marks cannot be more than 100")
		
		chemmarks = entUpdateChemMarks.get()
		if chemmarks.isdigit():
			chemmarks = int(chemmarks)
		else:
			raise Exception("Marks cannot contain Characters")
		
		if chemmarks < 0:
			raise Exception("Marks cannot be negative")
		elif chemmarks>100:
			raise Exception("Marks cannot be more than 100")

		mathsmarks = entUpdateMathMarks.get()
		if mathsmarks.isdigit():
			mathsmarks = int(mathsmarks)
		else:
			raise Exception("Marks cannot contain Characters")

		if mathsmarks < 0:
			raise Exception("Marks cannot be negative")
		elif mathsmarks>100:
			raise Exception("Marks cannot be more than 100")
		

		sql = "update sms set name ='%s',mobileno='%d',div='%s',physics ='%d',chemistry = '%d', maths = '%d' where rno='%d'"
		args = (names,mob,divs,phymarks,chemmarks,mathsmarks,rno)
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Done",str(cursor.rowcount) + " Rows Updated")
		
			
		
	except Exception as e:
		messagebox.showerror("Bad Input",e)

	except DatabaseError as e:
		messagebox.showerror("Try Again", e)
		con.rollback()
			
		
	finally:
		if con is not None:
			con.close()
			entUpdateRno.delete(0, END)
			entUpdateName.delete(0, END)
			entUpdateMob.delete(0, END)
			entUpdateDiv.delete(0, END)
			entUpdatePhyMarks.delete(0, END)
			entUpdateChemMarks.delete(0, END)
			entUpdateMathMarks.delete(0, END)
			entUpdateRno.focus()








def f9():
	root.withdraw()
	dest.deiconify()

def f10():
	dest.withdraw()
	root.deiconify()

def f11():
	con = None
	try:
		con = connect("system/abc123")
		rno = entDeleteRno.get()
		if rno.isdigit():
			rno = int(rno)
		else:
			raise Exception("Roll no. cannot contain characters")
		if rno is 0:
			raise Exception("Roll no. can't be 0")
		if rno < 0:
			raise Exception("Roll no. can't be negative")
		args = (rno)
		cursor = con.cursor()
		sql = "delete from sms where rno ='%d'"
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Done",str(cursor.rowcount) + " Rows Deleted")
	except DatabaseError as e:
		messagebox.showerror("Try Again", e)
		con.rollback()
	except Exception as e:
		messagebox.showerror("Bad Input",e) 		
		
	finally:
		if con is not None:
			con.close()
			entDeleteRno.delete(0, END)
			entDeleteRno.focus()

def f12():
	con = None
	try:
		con = connect("system/abc123")
		cursor = con.cursor()
		sql = "select * from sms"
		cursor.execute(sql)
		data = cursor.fetchall()
		rno = []
		name = []
		#marks = []
		phy = []
		chem = []
		maths = []
		#for d in data:
		#	marks.append(round(int((d[4])+int(d[5])+int(d[6]))/3,2))
		for d in data:
			phy.append(d[4])
		for d in data:
			chem.append(d[5])
		for d in data:
			maths.append(d[6])
		for d in data:
			name.append(d[1])
		for d in data:
			rno.append(d[0])
		
		x = np.arange(len(rno))
		plt.bar(x,phy,width = 0.25,label="Marks of Physics",color = "r", alpha = 0.3)
		plt.bar(x + 0.25,chem,width = 0.25,label="Marks of Chemistry",color = "b", alpha = 0.5)
		plt.bar(x + 0.50,maths,width = 0.25,label="Marks of Maths",color = "m", alpha = 0.8)
		plt.xticks(x,name, fontsize = 10, rotation = 30)
		plt.title('Percentages of Students')
		plt.xlabel('Names ',fontsize = 10)
		plt.ylabel('Percentage ',fontsize = 10)
		plt.legend()
		plt.grid()
		plt.show()
	except Exception as e:
		messagebox.showerror("Try Again",e)

def f13():
	root.withdraw()
	graphs.deiconify()

def f14():
	graphs.withdraw()
	root.deiconify()

def f15():
    con = None
    try:
        con = connect("system/abc123")
        cursor = con.cursor()
        sql = "select * from sms"
        cursor.execute(sql)
        data = cursor.fetchall()
        rno = []
        name = []
        marks = []
        for d in data:
            marks.append(round(int((d[4])+int(d[5])+int(d[6]))/3,2))
        for d in data:
            name.append(d[1])
        for d in data:
            rno.append(d[0])
        x = np.arange(len(rno))
        plt.bar(name,marks,label="Marks of smss",width = 0.20)
        plt.title('Percentages of Students')
        plt.xlabel('Names ',fontsize = 10)
        plt.ylabel('Percentage ',fontsize = 10)
        plt.legend()
        plt.grid()
        plt.show()
    except Exception as e:
        messagebox.showerror("Try Again",e)




btnAdd = Button(root,text="Add",width=10,font=("italic",18,"bold"),command=f1)
btnView = Button(root,text="View",width=10,font=("italic",18,"bold"),command=f3)
btnUpdate = Button(root,text="Update",width=10,font=("italic",18,"bold"),command=f5)
btnDelete = Button(root,text="Delete",width=10,font=("italic",18,"bold"),command=f9)
btnGraph = Button(root,text="Graph",width=10,font=("italic",18,"bold"),command=f13)
lblTemp = Label(root,width=30,text=str1,font=("italic",18,"bold"))
lblquote = Label(root,width=40,text=msg1,font=("italic",18,"bold"))

btnAdd.pack(pady=20),
btnView.pack(pady=20)
btnUpdate.pack(pady=20)
btnDelete.pack(pady=20)
btnGraph.pack(pady=20)
lblTemp.pack(pady=20)
lblquote.pack(pady=20)

adst = Toplevel(root)
adst.title("ADD St.")
adst.geometry("600x600+300+300")
adst.configure(background='beige')
adst.withdraw()



lblAddRno = Label(adst,text="Enter Roll Number",font=("times",14,'italic'))
entAddRno = Entry(adst,bd=14,font=("times",14,'italic'))
lblAddName = Label(adst,text="Enter Name",font=("times",14,'italic'))
entAddName = Entry(adst,bd=14,font=("times",14,'italic'))
lblAddMob = Label(adst,text="Enter Mobile Number",font=("times",14,'italic'))
entAddMob = Entry(adst,bd=14,font=("times",14,'italic'))
lblAddDiv = Label(adst,text="Enter Division",font=("times",14,'italic'))
entAddDiv = Entry(adst,bd=14,font=("times",14,'italic'))
#lblAddMarks = Label(adst,text="Enter Marks",font=("times",14,'italic'))
#entAddMarks = Entry(adst,bd=14,font=("times",14,'italic'))
#btnAddMarks = Button(adst,text="Save",width=14,font=("italic",14,"italic"),command=f7)
lblAddPhy = Label(adst,text="Enter Physics Marks",font=("times",14,'italic'))
entAddPhy = Entry(adst,bd=14,font=("times",14,'italic'))
lblAddChem = Label(adst,text="Enter Chemistry Marks",font=("times",14,'italic'))
entAddChem = Entry(adst,bd=14,font=("times",14,'italic'))
lblAddMath = Label(adst,text="Enter Maths Marks",font=("times",14,'italic'))
entAddMath = Entry(adst,bd=14,font=("times",14,'italic'))

btnAddSave = Button(adst,text="Save",width=10,font=("italic",14,"bold"),command=f7)
btnAddBack = Button(adst,text="Back",width=10,font=("italic",14,"bold"),command=f2)



lblAddRno.pack(pady=5)
entAddRno.pack(pady=5)
lblAddName.pack(pady=5)
entAddName.pack(pady=5)
lblAddMob.pack(pady=5)
entAddMob.pack(pady=5)
lblAddDiv.pack(pady=5)
entAddDiv.pack(pady=5)
lblAddPhy.pack(pady=5)
entAddPhy.pack(pady=5)
lblAddChem.pack(pady=5)
entAddChem.pack(pady=5)
lblAddMath.pack(pady=5)
entAddMath.pack(pady=5)
btnAddSave.pack(pady=5)
btnAddBack.pack(pady=5)

vist =Toplevel(root)
vist.title("View St.")
vist.geometry("600x600+300+300")
vist.configure(background='beige')
vist.withdraw()

stViewData = scrolledtext.ScrolledText(vist,width=50,height=30)
btnViewBack = Button(vist,text='Back',font=("arial",18,'bold'),command=f4)

stViewData.pack(pady=10)
btnViewBack.pack(pady=10)

upst = Toplevel(root)
upst.title("UPDATE St.")
upst.geometry("600x600+300+300")
upst.configure(background='beige')
upst.withdraw()

lblUpdateRno = Label(upst,text="Enter rno",font=("arial",14,'bold'))
entUpdateRno = Entry(upst,bd=10,font=("arial",14,'bold'))
lblUpdateName = Label(upst,text="Enter name",font=("arial",14,'bold'))
entUpdateName = Entry(upst,bd=10,font=("arial",14,'bold'))
lblUpdateMob = Label(upst,text="Enter Mobile no",font=("arial",14,'bold'))
entUpdateMob = Entry(upst,bd=10,font=("arial",14,'bold'))
lblUpdateDiv = Label(upst,text="Enter Division",font=("arial",14,'bold'))
entUpdateDiv = Entry(upst,bd=10,font=("arial",14,'bold'))
lblUpdatePhyMarks = Label(upst,text="Enter Physics Marks",font=("arial",14,'bold'))
entUpdatePhyMarks = Entry(upst,bd=10,font=("arial",14,'bold'))
lblUpdateChemMarks = Label(upst,text="Enter Chemistry Marks",font=("arial",14,'bold'))
entUpdateChemMarks = Entry(upst,bd=10,font=("arial",14,'bold'))
lblUpdateMathMarks = Label(upst,text="Enter Maths Marks",font=("arial",14,'bold'))
entUpdateMathMarks = Entry(upst,bd=10,font=("arial",14,'bold'))
btnUpdateSave = Button(upst,text="Save",width=10,font=("italic",14,"bold"),command=f8)
btnUpdateBack = Button(upst,text="Back",width=10,font=("italic",14,"bold"),command=f6)

lblUpdateRno.pack(pady=5)
entUpdateRno.pack(pady=5)
lblUpdateName.pack(pady=5)
entUpdateName.pack(pady=5)
lblUpdateMob.pack(pady=5)
entUpdateMob.pack(pady=5)
lblUpdateDiv.pack(pady=5)
entUpdateDiv.pack(pady=5)
lblUpdatePhyMarks.pack(pady=5)
entUpdatePhyMarks.pack(pady=5)
lblUpdateChemMarks.pack(pady=5)
entUpdateChemMarks.pack(pady=5)
lblUpdateMathMarks.pack(pady=5)
entUpdateMathMarks.pack(pady=5)
btnUpdateSave.pack(pady=5)
btnUpdateBack.pack(pady=5)

dest = Toplevel(root)
dest.title("DELETE St.")
dest.geometry("600x600+300+300")
dest.configure(background='beige')
dest.withdraw()

lblDeleteRno = Label(dest,text="Enter rno",font=("arial",18,'bold'))
entDeleteRno = Entry(dest,bd=10,font=("arial",18,'bold'))
btnDeleteSave = Button(dest,text="Save",width=10,font=("italic",18,"bold"),command=f11)
btnDeleteBack = Button(dest,text="Back",width=10,font=("italic",18,"bold"),command=f10)

lblDeleteRno.pack(pady=10)
entDeleteRno.pack(pady=10)
btnDeleteSave.pack(pady=10)
btnDeleteBack.pack(pady=10)

graphs = Toplevel(root)
graphs.title("ADD St.")
graphs.geometry("600x600+300+300")
graphs.configure(background='beige')
graphs.withdraw()

btnSubgrp = Button(graphs,text="Subject Wise Bar Graph",width=23,font=("italic",18,"bold"),command=f12)
btnPer = Button(graphs,text="Percentage Wise Bar Graph",width=23,font=("italic",18,"bold"),command=f15)
btnDeleteBack = Button(graphs,text="Back",width=10,font=("italic",18,"bold"),command=f14)

btnSubgrp.pack(pady=10)
btnPer.pack(pady=10)
btnDeleteBack.pack(pady=10)


root.mainloop()
