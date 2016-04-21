from math import pi
from os import system
def main(answer,chance):
	guess=raw_input("Enter shape(rectangle,square,circle,triangle):")
	if guess in ("rectangle","square","circle","triangle"):
		if guess==answer:
			system('clear')
			print "Correct!" 
		else:
			system('clear')
			if chance==1:
				print "Wrong...you have %s try left"%(chance)
				main(answer,chance-1)
			else:
				print "Game Over"
	else:
		print "Not in the choices"
		main(answer,chance)
def multiplier(count,number,number1):
	return number if count==1 else multiplier(count-1,number+number1,number1,)
def rectangle():
	l,w=raw_input("Rectangle\nLength:"),raw_input("Width:")
	if l.isdigit() and w.isdigit() and 1<=int(l)<=995 and 1<=int(w)<=995 :
		return multiplier(int(l),int(w),int(w))
	else:
		print "Only integers from 1 to 995 are allowed"
		return rectangle()
def square():
	s=raw_input("\nSquare\nSide:")
	if s.isdigit()and 1<=int(s)<=995:
		return multiplier(int(s),int(s),int(s))
	else:
		print "Only integers from 1 to 995 are allowed"
		return square()
def circle():
	r=raw_input("\nCircle\nEnter radius:")
	if r.isdigit() and 1<=int(r)<=31:
		return multiplier(multiplier(int(r),int(r),int(r)),pi,pi)
	else:
		print "Only integers from 1 to 31 are allowed"
		return circle()
def triangle():
	b,h=raw_input("\nTriangle\nBase:"),raw_input("Height:")
	if b.isdigit() and h.isdigit() and 1<=int(b)<=31 and 1<=int(h)<=31:
		return multiplier(multiplier(int(b),int(h),int(h)),0.5,0.5)
	else:
		print "Only integers from 1 to 31 are allowed"
		return triangle()
def begin():	
	r,s,c,t=rectangle(),square(),circle(),triangle()
	system('clear')
	if 4!=len(set([r,s,c,t])):
		system('clear')
		print "Two shapes shouldn't have the same area"
		begin()
	elif r==max(r,s,c,t):
		main("rectangle",1)
	elif s==max(r,s,c,t):
		main("square",1)
	elif c==max(r,s,c,t):
		main("circle",1)
	else:
		main("triangle",1)
begin()


