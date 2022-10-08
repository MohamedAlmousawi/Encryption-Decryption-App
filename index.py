import ast
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from sys import argv
from os import path
import os
from PyQt5.QtGui import QIcon
from main import Ui_MainWindow
code={
'a':'b',
'b':'c',
'c':'d',
'd':'e',
'e':'f',
'f':'g',
'g':'h',
'h':'i',
'i':'j',
'j':'k',
'k':'l',
'l':'m',
'm':'n',
'n':'o',
'o':'p',
'p':'q',
'q':'r',
'r':'s',
's':'t',
't':'u',
'u':'v',
'v':'w',
'w':'x',
'x':'y',
'y':'z',
'z':'a',
'A':'B',
'B':'C',
'C':'D',
'D':'E',
'E':'F',
'F':'G',
'G':'H',
'H':'I',
'I':'J',
'J':'K',
'K':'L',
'L':'M',
'M':'N',
'N':'O',
'O':'P',
'P':'Q',
'Q':'R',
'R':'S',
'S':'T',
'T':'U',
'U':'V',
'V':'W',
'W':'X',
'X':'Y',
'Y':'Z',
'Z':'A',
'0':'1',
'1':'2',
'2':'3',
'3':'4',
'4':'5',
'5':'6',
'6':'7',
'7':'8',
'8':'9',
'9':'0',
}
class mainApp(QMainWindow,Ui_MainWindow): 

    def __init__(self):
      
        super().__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.HANDEL_UI()
        self.HANDEL_BUTTONS()
    
    def encryption_text(self,text):
        enc_text= ''
        for char in text:
            if char not in code:
                enc_text+=char
            else:
                enc_text +=code[char]
        return enc_text




    def decryption_text(self,text):
        dec_text= ''
        keys = list(code.keys())
        values = list(code.values())
        for char in text:
            if char not in keys:
                dec_text+=char
            else:
                dec_text +=keys[values.index(char)]
        return dec_text

    def HANDEL_UI(self):
        self.setWindowTitle('eds manager')
        self.setWindowTitle('EAD')
        self.setFixedSize(800,490)
        self.setWindowIcon(QIcon('icon.png'))
        self.checkBox.setChecked(True)   
        self.textEdit_3.setPlainText(str(code)) 
    def HANDEL_BUTTONS(self):
        self.enc_text.clicked.connect(self.ENC_TEXT)
        self.dec_text.clicked.connect(self.DEC_TEXT)
        self.enc_file.clicked.connect(self.ENC_FILE)
        self.dec_file.clicked.connect(self.DEC_FILE)
        self.browse_file.clicked.connect(self.BROWSE_FILE)
        self.save_file.clicked.connect(self.SAVE_FILE)
        self.reset.clicked.connect(self.RESET_SETTINGS)
        self.apply.clicked.connect(self.CHANGE_KEYS)
        # == True:self.lineEdit_2.isEnabled()
    def ENC_TEXT(self):
        text = self.textEdit.toPlainText()
        self.textEdit_2.setPlainText(self.encryption_text(text))  
    def DEC_TEXT(self):
        text = self.textEdit.toPlainText()
        self.textEdit_2.setPlainText(self.decryption_text(text)) 
    def BROWSE_FILE(self):
        path =QFileDialog.getOpenFileName(self)
        self.lineEdit.setText(path[0].replace('/','\\'))
    def SAVE_FILE(self):
        path =QFileDialog.getExistingDirectory(self)
        self.lineEdit_2.setText(path.replace('/','\\'))
    def ENC_FILE(self):
        try:
            path =self.lineEdit.text()
            location1=self.lineEdit_2.text()
            if self.checkBox.isChecked() == False:location =os.path.join(location1,os.path.basename(os.path.normpath(path)))
            else:location = self.lineEdit.text()  
            textchars = bytearray({7,8,9,10,12,13,27} | set (range(0x20,0x100)) - {0x7f})
            is_binery_string = lambda bytes:bool(bytes.translate(None,textchars))
            
            if is_binery_string(open(path,'rb').read(1024)) == True:
            
                f1= open(path,'rb')
                img=f1.read()
                text = img.decode('ansi')
                txt=self.encryption_text(text)
                text=txt.encode('ansi')

                f1=open(location,'wb')
                img=f1.write(text)
            else:
                f1=open(path,'r') 
                file1=f1.read()
                text= self.encryption_text(file1)
                f2=open(location,'w')
                file2=f2.write(text)
            QMessageBox.information(self,'success',f'the file {os.path.basename(os.path.normpath(path))} is encryption successfully')
        except Exception:
            QMessageBox.warning(self,'field',f'the file {os.path.basename(os.path.normpath(path))} field encryption')
            

    def DEC_FILE(self):
        try:
            path =self.lineEdit.text()
            location1=self.lineEdit_2.text()
            if self.checkBox.isChecked() == False:location =os.path.join(location1,os.path.basename(os.path.normpath(path)))
            else:location = self.lineEdit.text()  
            textchars = bytearray({7,8,9,10,12,13,27} | set (range(0x20,0x100)) - {0x7f})
            is_binery_string = lambda bytes:bool(bytes.translate(None,textchars))
            
            if is_binery_string(open(path,'rb').read(1024)) == True:
            
                f1= open(path,'rb')
                img=f1.read()
                text = img.decode('ansi')
                txt=self.decryption_text(text)
                text=txt.encode('ansi')

                f1=open(location,'wb')
                img=f1.write(text)
            else:
                f1=open(path,'r') 
                file1=f1.read()
                text= self.decryption_text(file1)
                f2=open(location,'w')
                file2=f2.write(text)
            QMessageBox.information(self,'success',f'the file {os.path.basename(os.path.normpath(path))} is decryption successfully')
        except Exception:
            QMessageBox.warning(self,'field',f'the file {os.path.basename(os.path.normpath(path))} field decryption')
            
    def RESET_SETTINGS(self):
        global code
        code ={
'a':'b',
'b':'c',
'c':'d',
'd':'e',
'e':'f',
'f':'g',
'g':'h',
'h':'i',
'i':'j',
'j':'k',
'k':'l',
'l':'m',
'm':'n',
'n':'o',
'o':'p',
'p':'q',
'q':'r',
'r':'s',
's':'t',
't':'u',
'u':'v',
'v':'w',
'w':'x',
'x':'y',
'y':'z',
'z':'a',
'A':'B',
'B':'C',
'C':'D',
'D':'E',
'E':'F',
'F':'G',
'G':'H',
'H':'I',
'I':'J',
'J':'K',
'K':'L',
'L':'M',
'M':'N',
'N':'O',
'O':'P',
'P':'Q',
'Q':'R',
'R':'S',
'S':'T',
'T':'U',
'U':'V',
'V':'W',
'W':'X',
'X':'Y',
'Y':'Z',
'Z':'A',
'0':'1',
'1':'2',
'2':'3',
'3':'4',
'4':'5',
'5':'6',
'6':'7',
'7':'8',
'8':'9',
'9':'0'
}  
        self.textEdit_3.setPlainText(str(code))

    def CHANGE_KEYS(self):
        global code
        keys = self.textEdit_3.toPlainText()
        code = eval(keys)
app = QApplication(argv)
window = mainApp()
app.exec_()
    
