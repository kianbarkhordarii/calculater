from tkinter import*
top = Tk()
top.geometry("210x175")
top.title("mashin")
hasl=""
def dkm(sth):
    global hasl
    hasl=hasl+str(sth)
    nmaesh.delete("1.0","end")
    nmaesh.insert("1.0",hasl)
def mohasbe():
    global hasl
    result=str(eval(hasl))
    nmaesh.delete("1.0", "end")
    nmaesh.insert("1.0", result)
def pak():
    global hasl
    hasl=""
    nmaesh.delete("1.0", "end")
nmaesh=Text(top,height=2,width=25)
nmaesh.grid(row=1,column=1,columnspan=4)
#///////////////اعمال///////////////////////
jm=Button( top,text="+",command=lambda: dkm("+"),width=5)
jm.grid(row=4,column=4)
mnha=Button( top,text="-",command=lambda: dkm("-"),width=5)
mnha.grid(row=5,column=4)
zrb=Button( top,text="*",command=lambda: dkm("*"),width=5)
zrb.grid(row=3,column=4)
tq=Button( top,text="/",command=lambda: dkm("/"),width=5)
tq.grid(row=2,column=4)
dat=Button( top,text=".",command=lambda: dkm("."),width=5)
dat.grid(row=5,column=2)
msav=Button( top,text="=",command=lambda: mohasbe(),width=13)
msav.grid(row=6,column=3,columnspan=2)
hzf=Button(top,text="pak",command=lambda: pak(),width=5)
hzf.grid(row=5,column=3)
#///////////////عدد////////////////////////
yk=Button( top,text="1",command=lambda: dkm(1),width=5)
yk.grid(row=4,column=1)
do=Button( top,text="2",command=lambda: dkm(2),width=5)
do.grid(row=4,column=2)
se=Button( top,text="3",command=lambda: dkm(3),width=5)
se.grid(row=4,column=3)
char=Button( top,text="4",command=lambda: dkm(4),width=5)
char.grid(row=3,column=1)
pang=Button( top,text="5",command=lambda: dkm(5),width=5)
pang.grid(row=3,column=2)
sh=Button( top,text="6",command=lambda: dkm(6),width=5)
sh.grid(row=3,column=3)
hft=Button( top,text="7",command=lambda: dkm(7),width=5)
hft.grid(row=2,column=1)
hasht=Button( top,text="8",command=lambda: dkm(8),width=5)
hasht.grid(row=2,column=2)
noh=Button( top,text="9",command=lambda: dkm(9),width=5)
noh.grid(row=2,column=3)
sfr=Button( top,text="0",command=lambda: dkm(0),width=5)
sfr.grid(row=5,column=1)
mainloop()