#-*-coding: utf-8-*-

#Don't remove the above line

#This program uses a C routine for multiplication and square root
#in the calculator.  Other arithmetic operations are in Python

from Tkinter import *
from ctypes import *
import math

class calc:
	def getandreplace(self):
		"""replace x with * and ÷ with /"""
		
		self.expression = self.e.get()
		self.newtext=self.expression.replace(self.newdiv,'/')
		self.newtext=self.newtext.replace('x','*')

	def equals(self):
		"""when the equal button is pressed"""

		self.getandreplace()
		
		try:
			for i in self.newtext:
				if(i=='*'):
					multi=CDLL('./mul.so')
					y=self.newtext.split('*')
					a=c_float(float(y[0]))
					b=c_float(float(y[1]))
					mul=multi.mul
					mul.restype=c_float
					self.value=mul(a,b)
				if(i=='/'):
					divi=CDLL('./div.so')
					y=self.newtext.split('/')
					a=c_float(float(y[0]))
					b=c_float(float(y[1]))
					div=divi.div
					div.restype=c_float
					self.value=div(a,b)
				if(i=='+'):
					addi=CDLL('./add.so')
					y=self.newtext.split('+')
					a=c_float(float(y[0]))
					b=c_float(float(y[1]))
					add=addi.add
					add.restype=c_float
					self.value=add(a,b)
				if(i=='-'):
					subi=CDLL('./sub.so')
					y=self.newtext.split('-')
					a=c_float(float(y[0]))
					b=c_float(float(y[1]))
					sub=subi.sub
					sub.restype=c_float
					self.value=sub(a,b)			
				if (i=='%'):
					remi=CDLL('./rem.so')
					y=self.newtext.split('%')
					a=c_int(int(y[0]))
					b=c_int(int(y[1]))
					rem=remi.rem
					rem.restype=c_int
					self.value=rem(a,b)
				
					 #else:
					#self.value= eval(self.newtext) #evaluate the expression using the eval function
					
			
		except SyntaxError or NameErrror:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.e.delete(0,END)
			self.e.insert(0,self.value)
			
	def squareroot(self):
		"""squareroot method"""
		
		self.getandreplace()
		try: 
			self.value= eval(self.newtext) #evaluate the expression using the eval function
		except SyntaxError or NameErrror:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			multi=CDLL('./sq_rt.so')
			sq_rt=multi.sq_rt
			sq_rt.restype=c_float
			self.sqrtval=sq_rt(c_float(float(self.value)))
			self.e.delete(0,END)
			self.e.insert(0,self.sqrtval)

	def square(self):
		
		"""square method"""
		
		self.getandreplace()
		try: 
			self.value= eval(self.newtext) #evaluate the expression using the eval function
		except SyntaxError or NameErrror:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			multi=CDLL('./squar.so')
			squar=multi.squar
			squar.restype=c_float
			self.sqrtval=squar(c_float(float(self.value)))
			self.e.delete(0,END)
			self.e.insert(0,self.sqrtval)
			
			
			
			
			
			
	def clearall(self): 
		"""when clear button is pressed,clears the text input area"""
		self.e.delete(0,END)
	
	def clear1(self):
		self.txt=self.e.get()[:-1]
		self.e.delete(0,END)
		self.e.insert(0,self.txt)

	def action(self,argi): 
		"""pressed button's value is inserted into the end of the text area"""
		self.e.insert(END,argi)
	
	def __init__(self,master):
		"""Constructor method"""
		master.title('Calulator') 
		master.geometry()
		self.e = Entry(master)
		self.e.grid(row=0,column=0,columnspan=6,pady=3)
		self.e.focus_set() #Sets focus on the input text area
				
		self.div='÷'
		self.newdiv=self.div.decode('utf-8')

		#Generating Buttons
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text='AC',width=3,command=lambda:self.clearall()).grid(row=1, column=4)
		Button(master,text='C',width=3,command=lambda:self.clear1()).grid(row=1, column=5)
		Button(master,text="+",width=3,command=lambda:self.action('+')).grid(row=4, column=3)
		Button(master,text="x",width=3,command=lambda:self.action('x')).grid(row=2, column=3)
		Button(master,text="-",width=3,command=lambda:self.action('-')).grid(row=3, column=3)
		Button(master,text="÷",width=3,command=lambda:self.action(self.newdiv)).grid(row=1, column=3) 
		Button(master,text="%",width=3,command=lambda:self.action('%')).grid(row=4, column=2)
		Button(master,text="7",width=3,command=lambda:self.action('7')).grid(row=1, column=0)
		Button(master,text="8",width=3,command=lambda:self.action(8)).grid(row=1, column=1)
		Button(master,text="9",width=3,command=lambda:self.action(9)).grid(row=1, column=2)
		Button(master,text="4",width=3,command=lambda:self.action(4)).grid(row=2, column=0)
		Button(master,text="5",width=3,command=lambda:self.action(5)).grid(row=2, column=1)
		Button(master,text="6",width=3,command=lambda:self.action(6)).grid(row=2, column=2)
		Button(master,text="1",width=3,command=lambda:self.action(1)).grid(row=3, column=0)
		Button(master,text="2",width=3,command=lambda:self.action(2)).grid(row=3, column=1)
		Button(master,text="3",width=3,command=lambda:self.action(3)).grid(row=3, column=2)
		Button(master,text="0",width=3,command=lambda:self.action(0)).grid(row=4, column=0)
		Button(master,text=".",width=3,command=lambda:self.action('.')).grid(row=4, column=1)
		Button(master,text="(",width=3,command=lambda:self.action('(')).grid(row=2, column=4)
		Button(master,text=")",width=3,command=lambda:self.action(')')).grid(row=2, column=5)
		Button(master,text="√",width=3,command=lambda:self.squareroot()).grid(row=3, column=4)
		Button(master,text="x²",width=3,command=lambda:self.square()).grid(row=3, column=5)
#Main
root = Tk()
obj=calc(root) #object instantiated
root.mainloop()

