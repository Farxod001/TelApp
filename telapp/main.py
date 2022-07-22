from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
import sqlite3
import pyttsx3



engine = pyttsx3.init()
engine.setProperty("rate", 80)

Window.size = (270,540)

qadam = 0
daraja=0
tekshir ='yuq'

ikki=[ [0,1], [0,1], [1,0], [0,1], [1,0] ]
uch=[ [0,2,1], [1,0,2], [2,0,1], [1,2,0], [2,1,0] ]
turt=[ [0,1,3,2],[0,2,3,1],[1,0,2,3],[2,1,3,0],[3,1,2,0] ]
besh=[ [0,1,2,4,3], [0,1,3,4,2], [1,0,2,3,4], [3,1,2,0,4], [1,0,4,2,3] ]
olti=[ [0,1,2,4,3,5], [0,1,3,4,5,2], [1,0,2,5,3,4], [3,1,5,2,0,4], [1,0,5,4,2,3] ]
yetti=[ [0,1,2,3,5,4,6], [0,1,2,4,5,3,6], [1,0,6,2,5,3,4], [6,3,1,5,2,0,4], [1,0,5,4,2,3,6] ]
sakkiz=[ [0,1,2,3,4,6,5,7], [0,1,2,4,3,5,6,7], [1,2,6,0,5,3,4,7], [6,3,1,5,7,2,0,4], [1,7,5,4,2,0,3,6] ] 
collor=[[0,.7,.1,1],[1,0,0,1]]



Builder.load_string('''
<GUI>:
    BoxLayout:
        orientation: "vertical"
        canvas:

            Rectangle:
                size: self.size
                pos: self.pos
                source: "123.jpg"

        BoxLayout:
            orientation: "vertical"
            Label:
                text: ''

            BoxLayout:
                orientation: "horizontal"
                Label:
                    id: asli
                    text: root.oldingiENG
                    bold: True
                    font_size: 20
                    canvas.before:
                        Color:
                            rgba: 0,.7,.1,.7
                        Rectangle:
                            size: self.size
                            pos: self.pos
                Label:
                    id: javob
                    text: root.javob
                    bold: True
                    font_size: 20

                    canvas.before:
                        Color:
                            rgba: 0,.7,.1,.7
                        Rectangle:
                            size: self.size
                            pos: self.pos 
            Label:
                text: ''

        BoxLayout:
            orientation: "vertical"

            Label:
                id: manosi
                text: root.uzbek
                color: 0,0,0,1
                font_size: 20
            Label:
                id: jamlash
                text: root.jamlanma
                bold: True
                color: 0,.4,.8,1
                font_size: 20


        BoxLayout:
            orientation: "vertical"
            BoxLayout:
                orientation: "horizontal"

                Button:
                    id: aa
                    text: root.A
                    bold: True
                    color: 0,.4,.8,1
                    font_size: 20
                    background_color: 0,0,0,.1
                    on_press: root.btn1()
                Button:
                    id: bb
                    text: root.B
                    bold: True
                    color: 0,.4,.8,1
                    font_size: 20
                    background_color: 0,0,0,.1
                    on_press: root.btn2()
                Button:
                    id: cc
                    text: root.C
                    bold: True
                    color: 0,.4,.8,1
                    font_size: 20
                    background_color: 0,0,0,.1
                    on_press: root.btn3()
                Button:
                    id: dd
                    text: root.D
                    bold: True
                    color: 0,.4,.8,1
                    font_size: 20
                    background_color: 0,0,0,.1   
                    on_press: root.btn4()
                Button:
                    id: ee
                    text: root.E
                    bold: True
                    color: 0,.4,.8,1
                    font_size: 20
                    background_color: 0,0,0,.1
                    on_press: root.btn5()
                Button:
                    id: ff
                    text: root.F
                    bold: True
                    color: 0,.4,.8,1
                    font_size: 20
                    background_color: 0,0,0,.1
                    on_press: root.btn6()
                Button:
                    id: gg
                    text: root.G
                    bold: True
                    color: 0,.4,.8,1
                    font_size: 20
                    background_color: 0,0,0,.1
                    on_press: root.btn7()
                Button:
                    id: hh
                    text: root.H
                    bold: True
                    color: 0,.4,.8,1
                    font_size: 20                
                    background_color: 0,0,0,.1
                    on_press: root.btn8()
            Label:
                id: vaqtincha
                text: root.english
                color: 0,0,0,1
                font_size: 20


            BoxLayout:
                orientation: "horizontal"

                Button:
                    text: 'Yordam'
                    color: 0,0,0,1
                    font_size: 25 
                    background_color: 0,0,0,.3
                    on_press: root.ovozchiq()
                Button:
                    text: 'Keyingi'
                    color: 0,0,0,1
                    font_size: 25 
                    background_color: 0,0,0,.3
                    on_press: root.tekshirish()
            Label:
                text: ''

''')


class GUI(FloatLayout):


    english= StringProperty()
    uzbek= StringProperty()
    oldingiENG=StringProperty()
    harf=StringProperty()
    A=StringProperty()
    B=StringProperty()
    C=StringProperty()
    D=StringProperty()
    E=StringProperty()
    F=StringProperty()
    G=StringProperty()
    H=StringProperty()
    jamlanma=StringProperty()
    javob=StringProperty()



    def __init__(self, **kwargs):
        super(GUI, self).__init__(**kwargs)
        return self.sekil()


    def btn1(self):
        self.jamlanma += self.ids.aa.text   
        self.ids.aa.text=''
        self.ids.vaqtincha.text=''

    def btn2(self):
        self.jamlanma += self.ids.bb.text
        self.ids.bb.text=''
        self.ids.vaqtincha.text=''
    
    def btn3(self):
        self.jamlanma += self.ids.cc.text
        self.ids.cc.text=''
        self.ids.vaqtincha.text=''
    
    def btn4(self):
        self.jamlanma += self.ids.dd.text
        self.ids.dd.text=''
        self.ids.vaqtincha.text=''

    def btn5(self):
        self.jamlanma += self.ids.ee.text
        self.ids.ee.text=''
        self.ids.vaqtincha.text=''

    def btn6(self):
        self.jamlanma += self.ids.ff.text
        self.ids.ff.text=''
        self.ids.vaqtincha.text=''

    def btn7(self):
        self.jamlanma += self.ids.gg.text
        self.ids.gg.text=''
        self.ids.vaqtincha.text=''

    def btn8(self):
        self.jamlanma += self.ids.hh.text
        self.ids.hh.text=''
        self.ids.vaqtincha.text=''

    def ovozchiq(self):
        engine.say(self.english)
        engine.runAndWait()   


    def sekil(self): 

        global qadam       
        global english    
        global daraja      
        global uzbek
        global tekshir

        self.jamlanma = ''

        conn = sqlite3.connect('suzlar.db')
        c = conn.cursor()

        c.execute("SELECT id FROM suuz  WHERE daraja < 5 and id > "+ str(qadam))
        qadam= int(c.fetchone()[0])
        c.execute("SELECT ing FROM suuz  WHERE id= "+ str(qadam))
        self.english= str(c.fetchone()[0])
        c.execute("SELECT daraja FROM suuz  WHERE id = "+ str(qadam))
        daraja= int(c.fetchone()[0])
        c.execute("SELECT q1 FROM suuz  WHERE id = "+ str(qadam))
        self.uzbek= str(c.fetchone()[0]) 

        qd=0   

        word=self.english
        if len(word)==2:
            for x in ikki[daraja]:
               
                qd+=1
                if qd==1:
                    self.D=word[x]            
                if qd==2:
                    self.E=word[x]
                    self.ids.aa.text=''
                    self.ids.bb.text=''
                    self.ids.cc.text=''
                    self.ids.ff.text=''
                    self.ids.gg.text=''
                    self.ids.hh.text=''

        if len(word)==3:
            for x in uch[daraja]:
               
                qd+=1
                if qd==1:
                    self.C=word[x]            
                if qd==2:
                    self.D=word[x]
                if qd==3:
                    self.E=word[x]                        
                    self.ids.aa.text=''
                    self.ids.bb.text=''
                    self.ids.ff.text=''
                    self.ids.gg.text=''
                    self.ids.hh.text=''

        if len(word)==4:
            for x in turt[daraja]:
               
                qd+=1
                if qd==1:
                    self.C=word[x]            
                if qd==2:
                    self.D=word[x]
                if qd==3:
                    self.E=word[x]
                if qd==4:
                    self.F=word[x]
                    self.ids.aa.text=''
                    self.ids.bb.text=''
                    self.ids.gg.text=''
                    self.ids.hh.text=''                


        if len(word)==5:
            for x in besh[daraja]:
               
                qd+=1
                if qd==1:
                    self.B=word[x]            
                if qd==2:
                    self.C=word[x]
                if qd==3:
                    self.D=word[x]
                if qd==4:
                    self.E=word[x]                
                if qd==5:
                    self.F=word[x] 
                    self.ids.aa.text=''
                    self.ids.gg.text=''
                    self.ids.hh.text='' 

        if len(word)==6:
            for x in olti[daraja]:
               
                qd+=1
                if qd==1:
                    self.B=word[x]            
                if qd==2:
                    self.C=word[x]
                if qd==3:
                    self.D=word[x]
                if qd==4:
                    self.E=word[x]                
                if qd==5:
                    self.F=word[x] 
                if qd==6:
                    self.G=word[x]
                    self.ids.aa.text=''
                    self.ids.hh.text=''  


        if len(word)==7:
            for x in yetti[daraja]:
               
                qd+=1
                if qd==1:
                    self.A=word[x]            
                if qd==2:
                    self.B=word[x]
                if qd==3:
                    self.C=word[x]
                if qd==4:
                    self.D=word[x]                
                if qd==5:
                    self.E=word[x] 
                if qd==6:
                    self.F=word[x] 
                if qd==7:
                    self.G=word[x]
                    self.ids.hh.text=''                      

        if len(word)==8:
            for x in sakkiz[daraja]:
               
                qd+=1
                if qd==1:
                    self.A=word[x]            
                if qd==2:
                    self.B=word[x]
                if qd==3:
                    self.C=word[x]
                if qd==4:
                    self.D=word[x]                
                if qd==5:
                    self.E=word[x] 
                if qd==6:
                    self.F=word[x] 
                if qd==7:
                    self.G=word[x]
                if qd==8:
                    self.H=word[x]

        conn.commit()
        conn.close() 

    def tekshirish(self):

        self.javob=self.jamlanma
        self.oldingiENG=self.english
        conn = sqlite3.connect('suzlar.db')
        c = conn.cursor()


        if self.jamlanma == self.english:
            sanoq=str(daraja + 1)
            c.execute("""UPDATE suuz SET daraja = :cc WHERE id = :qadam """,{'cc': sanoq,'qadam':qadam+1})      
            self.ids.asli.text= self.oldingiENG 
            self.ids.javob.text=self.javob
 

        else:
            self.ids.asli.text= self.oldingiENG 
            self.ids.javob.text=self.javob  

        conn.commit()
        conn.close() 
        return self.sekil()












class GUIApp(App):
    def build(self):
        return GUI()


if __name__ == '__main__':
    GUIApp().run()
