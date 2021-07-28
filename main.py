import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt , QThread, pyqtSignal,QPropertyAnimation, QPoint, QEasingCurve
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon, QCursor , QImage, QPixmap

import webbrowser

# main libraries
import requests
from bs4 import BeautifulSoup as bs
import json
import os
import ctypes
import random

class ThreadDownloadPhoto(QThread):
  CONTENT = pyqtSignal(str)
  
  def __init__(self,Main_Self,link,parent=None):
    QThread.__init__(self, parent)

    self.Main_Self = Main_Self
    self.link      = link
    self.Main_Self.status.setText('Opening Session ...')
        
    self.session   = requests.Session()
    
  def run(self):
    self.Main_Self.status.setText('Please Wait ...')
    path      = self.save_pic()
    self.CONTENT.emit(path)


  def SaveID(self):
    Homedir           = os.path.expanduser('~')
    directory         = os.path.join(Homedir , 'Pictures')
    wallDir           = os.path.join(directory,'Wallpaper')
    fileDir           = os.path.join(wallDir,'image_IDs.txt')
    file_exists  = False
    #Check for dir and create new file if no folder found
    if os.path.isdir(wallDir) == False :
      self.Main_Self.status.setText('Creating Wallpaper Directory')
      os.mkdir(wallDir)
      with open(fileDir,'w') as f :
        f.write(self.Main_Self.id+'\n')
      self.Main_Self.status.setText('Writing Data to file')
    elif os.path.isdir(wallDir) == True and os.path.isfile(fileDir) == False:
      self.Main_Self.status.setText('Creating ID file for logging')
      with open(fileDir,'w') as f :
        f.write(self.Main_Self.id+'\n')
    else:
     
      with open(fileDir,'r') as f :
        lines = f.readlines()
      Lines = [line.strip('\n').strip() for line in lines ]
      if self.Main_Self.id in Lines:
         self.Main_Self.status.setText('ID already exists')
         file_exists = True
        
      else:
          self.Main_Self.status.setText('Writing Data to file')
          with open(fileDir,'a+') as f :
            f.write(self.Main_Self.id+'\n')
          print(self.Main_Self.id,' Added')
          
    return wallDir, file_exists
    
        
   

  def save_pic(self):

    #FILE SAVE + LOCATION
      
    path,file_exists = self.SaveID()
    if file_exists :
      self.Main_Self.status.setText('File Exists...')
      Filename = '{}.{}'.format(self.Main_Self.id,ext)
      PicPath  = os.path.join(path,Filename)
      
    else:
      
      #WRITE TO FILE
      try:
        self.content, ext = self.get_PicContents()
      except requests.exceptions.ConnectionError:
        self.Main_Self.status.setText('Download Failed')
        self.content = '03'
        ext          = ''
      PicPath = ''
      if self.content == '03' :
        pass
      elif len(self.content) < 2 :
        pass
      else:
        self.Main_Self.status.setText('Writing Contents to file')
        Filename = '{}.{}'.format(self.Main_Self.id,ext)
        PicPath  = os.path.join(path,Filename)
        with open(PicPath,'wb') as f:
          f.write(self.content)
          self.Main_Self.status.setText('File Successfully Written and Saved')
    return PicPath

    
  def get_PicContents(self):
  
    if self.link == '' or self.link == None:
      self.Main_Self.status.setText('No Link to Fetch')
    else:

      #GET CTOKEN
    
      self.Main_Self.status.setText('Fetching CSRF code')
      r     = self.session.get(self.link)
      soup  = bs(r.content,'lxml')
      
      fsize = float(soup.find('div',{'class':'stats clearfix'}).find('i',{'class':'icon-doc'}).find_next().text.strip().replace(' MB',''))
      self.Main_Self.size.setText('  File Size : {} MB'.format(str(fsize)))
      self.Main_Self.size.show()
      self.Main_Self.csrf  = soup.find('input',{'name':'_csrf'}).get('value')
      
      self.Main_Self.status.setText('CSRF code fetched')
      
      #POST METHOD

      post_url = 'https://stocksnap.io/photo/download'
      payloads = {
          '_csrf': self.Main_Self.csrf,
          'photoId': self.Main_Self.id
          }
      self.Main_Self.status.setText('Gathering Post requests...')
      header = {
        'authority': 'stocksnap.io',
        'method': 'POST',
        'path': '/photo/download',
        'scheme': 'https',
        'origin': 'https://stocksnap.io',
        'referer': self.link,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
      }
      self.Main_Self.status.setText('Downloading ...')
      p = self.session.post(post_url,data=payloads,headers=header)
    
      if p.status_code == 200 :
        self.Main_Self.status.setText('Post Fetch Successful ... ')
        return p.content, p.headers['Content-Disposition'].split('.')[1]
      else :
        self.Main_Self.status.setText('Post Fetch Failed ... ')
        return '03', ''
    return '03','' 


class ThreadgetStockioData(QThread):
  DATA = pyqtSignal(str)
  
  def __init__(self,Main_Self,parent=None):
    QThread.__init__(self, parent)
    self.session   = requests.Session()
    self.Main_Self = Main_Self
    self.Finish    = False
    self.Main_Self.size.hide()
    
  def run(self):
    self.Main_Self.status.setText('Please Wait ...')
    link      = self.get_Data()
    
    self.DATA.emit(link)

  def errorM(error):
    # Error Codes : 
    code = [400,401,403,404,500,502,503,504]
    meaning = ['Bad Request','Unauthorized','Forbidden','Not Found','Internal Server Error','Bad Gateway','Service Unavailable','Gateway Timeout']

    try:
      loc = code.index(error)
      return meaning[loc]
    except ValueError:
      return f'{error} in list'

  def get_Data(self):
    page = random.randint(1,851)
    if True :
      try :
        r = self.session.get(f'https://stocksnap.io/api/load-photos/date/desc/{page}')
        soup    = bs(r.content,'lxml')
        if r.status_code == 200:
          J = json.loads(soup.text)
          self.Finish == False
        else:
          self.Main_Self.status.setText(str(r.status_code) + str(self.errorM(r.status_code)))
      except requests.exceptions.ConnectionError:
        self.Main_Self.status.setText('Please Check Your Internet Connection')
    else:
      pass
    try :
      
      if len(J['results']) > 0 :
        
        try:
          num = random.randint(0,len(J['results'])-1)
          self.Main_Self.id = J['results'][num]['img_id']
            
          keys           = J['results'][num]['keywords'][:2]
          
          self.downloads = J['results'][num]['downloads']
          self.width     = J['results'][num]['img_width']
          self.height    = J['results'][num]['img_height']
          self.link = f'https://cdn.stocksnap.io/img-thumbs/280h/{self.Main_Self.id}.jpg'
          
          self.creatingthumbnail()
          dlink = f'https://stocksnap.io/photo/{keys[0]}-{keys[1]}-{self.Main_Self.id}'
          
        except:
          dlink = '00'
      else:
        dlink = '01'
    except UnboundLocalError:
      self.Main_Self.status.setText('Possibly Your Internet Connection Bad')
      self.link = '02'
      dlink = ''
    return dlink
  
  def creatingthumbnail(self):
    if self.link == '00':
      self.Main_Self.status.setText('Error Generate Again')
      
    elif self.link == '01':
      self.Main_Self.status.setText('Please Click Generate Again')
      
    elif self.link == '02':
      self.Main_Self.status.setText('Please Connect to Internet')
      
    elif len(self.link)>2 :
      self.Main_Self.status.setText('Generating Thumbnail')
      r = self.session.get(self.link)
      if r.status_code == 200 :
        pic = QImage()
        pic.loadFromData(r.content)
        self.Main_Self.pic_View.setPixmap(QPixmap(pic))
        self.Main_Self.pic_View.show()
        
        self.Main_Self.status.setText('Generated Thumbnail')
        self.Main_Self.No_Downloads.setText(str(self.downloads))
        self.Main_Self.Width.setText(str(self.width))
        self.Main_Self.Height.setText(str(self.height))
      else:
        print('Error %a : %a' %str(r.status_code) %self.errorM(r.status_code))
        self.Main_Self.status.setText(f'Error {str(r.status_code)} : {self.errorM(r.status_code)}')

    else:
      self.Main_Self.status.setText('No Link Generated..')
    
    
class StartScreen(QMainWindow):
  def __init__(self):
    super(StartScreen, self).__init__()
    loadUi("Main.ui",self)
    self.id   = ''
    self.link = None
    self.Preview.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=2,yOffset=2))
    self.Main.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=2,yOffset=2))
    self.Title.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=10,xOffset=3,yOffset=3))
    self.pic_View.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=10,xOffset=3,yOffset=3))

    self.btn_generatePic.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=10,xOffset=3,yOffset=3))                                   
    self.btn_downloadPic.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=10,xOffset=3,yOffset=3))                                   
    self.btn_setWallpaper.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=10,xOffset=3,yOffset=3))                                   

    self.Preview_ImageOut.setText('Open Preview')
    self.Minimize.hide()
    self.size.hide()
    
    #Preview Expander
    self.Expand.clicked.connect(self.OpenTabFunc)
    #Close Expander
    self.Minimize.clicked.connect(self.CloseTabFunc)
        
    #Download Picture
    self.btn_downloadPic.clicked.connect(self.getPicture)
    self.btn_setWallpaper.clicked.connect(self.getPicture)
    
    #Generate Picture
    self.btn_generatePic.clicked.connect(self.getDATA)
      
    #Exit Program
    self.Closed.clicked.connect(self.exitprogram)
    
    #Follow Social Media
    self.fButton.clicked.connect(self.facebook)
    self.tButton.clicked.connect(self.twitter)
    self.iButton.clicked.connect(self.LinkedIn)

    
    sizeObject = QDesktopWidget().screenGeometry(-1)
    print(" Screen size : "  + str(sizeObject.height()) + "x"  + str(sizeObject.width()))   

  def getPicture(self):
    if self.link is None :
      self.status.setText('Please Generate New Picture')
    else:
      self.getPicPath = ThreadDownloadPhoto(Main_Self = self,link = self.link)
      self.getPicPath.CONTENT.connect(self.getPath)
      self.getPicPath.start()

  def getPath(self,path):
    if len(path) > 2:
      
      self.status.setText('Setting Wallpaper')
      SPI_SETDESKWALLPAPER = 20
      SPIF_UPDATEINIFILE = 1
      ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, SPIF_UPDATEINIFILE)
      self.status.setText('Wallpaper Set Successfully')
    else:
      self.status.setText('Wallpaper Not Set')

  def getDATA(self):
    self.getID = ThreadgetStockioData(Main_Self = self)
    self.getID.DATA.connect(self.setID)
    self.getID.start()

  def setID(self,link):
    self.link = link

  #Methods for closing the Preview Tab
    
  def CloseTabFunc(self):
    self.Minimize.hide()
    self.Preview_ImageOut.setText('Open Preview')
    self.btn_setWallpaper.show()
    self.Expand.show()
    self.animation = QPropertyAnimation(self.Preview, b"size")
    self.animation.setDuration(250)
    self.animation.setEndValue(QtCore.QSize(0,330))
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
    self.animation.start()
    
  def OpenTabFunc(self):
    self.btn_setWallpaper.hide()
    self.Expand.hide()
    self.Preview_ImageOut.setText('Close Preview')
    self.Minimize.show()
    self.animation = QPropertyAnimation(self.Preview, b"size")
    self.animation.setDuration(1000)
    self.animation.setEndValue(QtCore.QSize(310,330))
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
    self.animation.start()

  
  #Social Media Functions
  def facebook(self):
    webbrowser.open('https://www.facebook.com/surenjanath.singh/')
    
  def twitter(self):
    webbrowser.open('https://twitter.com/surenjanath')
    
  def LinkedIn(self):
    webbrowser.open('https://www.linkedin.com/in/surenjanath/')
    
  def exitprogram(self):
    sys.exit()

  # DRAGGLESS INTERFACE
  
  def mousePressEvent(self, event):
      if event.button() == Qt.LeftButton:
          self.m_drag = True
          self.m_DragPosition = event.globalPos() - self.pos()
          event.accept()
          self.setCursor(QCursor(Qt.ClosedHandCursor))

  def mouseMoveEvent(self, QMouseEvent):
      if Qt.LeftButton and self.m_drag:
          self.move(QMouseEvent.globalPos() - self.m_DragPosition)
          QMouseEvent.accept()
    
  def mouseReleaseEvent(self, QMouseEvent):
      self.m_drag = False
      self.setCursor(QCursor(Qt.ArrowCursor))

# main
if __name__=="__main__":
    
    app = QApplication(sys.argv)
    widget = StartScreen()
    widget.setFixedHeight(400)
    widget.setFixedWidth(550)
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        pass

