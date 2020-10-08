#Mute Music
def mutemusic():
    global currentvol
    root.MuteButton.grid_remove()
    root.UnMuteButton.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)
######################################################################################
#UnMute Music
def unmutemusic():
    global currentvol
    root.UnMuteButton.grid_remove()
    root.MuteButton.grid()
    mixer.music.set_volume(currentvol)
######################################################################################   
# Volume Down
def volumedown():
    vol = mixer.music.get_volume()    
    mixer.music.set_volume(vol-0.05)
    ProgressBarVolLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressBarVol['value']=mixer.music.get_volume()*100
######################################################################################
#Volume Up
def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.05)
    ProgressBarVolLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressBarVol['value']=mixer.music.get_volume()*100
######################################################################################
#Music Resume
def musicresume():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    AudioStatus.configure(text='Playing.............')
######################################################################################
#Music Stop
def musicstop():
    mixer.music.stop()
    AudioStatus.configure(text='Stoped.............')
######################################################################################
#Music Pause
def musicpause():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    AudioStatus.configure(text='Pause.............')
######################################################################################
#Play Music
def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    root.MuteButton.grid()
    ProgressbarMusicLabel.grid()
    mixer.music.set_volume(0.4)
    ProgressBarVol['value']=40
    ProgressBarVolLabel['text']='40%'
    mixer.music.play() 
    AudioStatus.configure(text='Playing.............')   
    #Music Progressbar
    song = MP3(ad)
    totalsonglength = int(song.info.length)
    ProgressbarMusic['maximum']=totalsonglength
    ProgressbarMusicEndLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
    def Progressbarmusictick():
        currentsonglength = mixer.music.get_pos()//1000
        ProgressbarMusic['value'] = currentsonglength
        ProgressbarMusicStartLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=currentsonglength))))
        ProgressbarMusic.after(2,Progressbarmusictick)
    Progressbarmusictick()    
######################################################################################
#Music Url
def musicurl():
    try:
        dd = filedialog.askopenfilename(initialdir='D:/Songs',title='Select Audio File',filetype=(('MP3','mp3'),('WAV','*.wav')))
    except:
        dd = filedialog.askopenfilename(title='Select Audio File',filetype=(('MP3','mp3'),('WAV','*.wav')))
    audiotrack.set(dd)
######################################################################################
def createwidthes():
    global AudioStatus,ProgressbarLabel,ProgressBarVol,ProgressBarVolLabel,ProgressbarMusicLabel,ProgressbarMusic,ProgressbarMusicStartLabel,ProgressbarMusicEndLabel
    #Labels
    Tracklabel = Label(root,text='Select Song:-',background='lightpink',font=('arial',15,'italic bold'))
    Tracklabel.grid(row=0,column=0,padx=20,pady=20)

    AudioStatus = Label(root,text='',background='lightpink',font=('arial',15,'italic bold'),width=20)
    AudioStatus.grid(row=2,column=1)

    #Entry box
    TrackLabelEntry = Entry(root,font=('arial',15,'italic bold'),width=30,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)
    #Buttons
    BrowseButton = Button(root,text='Browse',background='lightblue',font=('arial',12,'italic bold'),width=15,bd=5,activebackground='pink',command=musicurl)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)

    PlayButton = Button(root,text='Play',background='lightgreen',font=('arial',12,'italic bold'),width=15,bd=5,activebackground='pink',command=playmusic)
    PlayButton.grid(row=1,column=0,padx=20,pady=20)

    root.PauseButton = Button(root,text='Pause',background='lightyellow',font=('arial',12,'italic bold'),width=15,bd=5,activebackground='pink',command=musicpause)
    root.PauseButton.grid(row=1,column=1,padx=20,pady=20)

    root.ResumeButton = Button(root,text='Resume',background='lightyellow',font=('arial',12,'italic bold'),width=15,bd=5,activebackground='pink',command=musicresume)
    root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
    root.ResumeButton.grid_remove()

    VolumeUpButton = Button(root,text='VolumeUp',background='blue',font=('arial',12,'italic bold'),width=15,bd=5,activebackground='pink',command=volumeup)
    VolumeUpButton.grid(row=1,column=2,padx=20,pady=20)

    StopButton = Button(root,text='Stop',background='red',font=('arial',12,'italic bold'),width=15,bd=5,activebackground='pink',command=musicstop)
    StopButton.grid(row=2,column=0,padx=20,pady=20)

    VolumeDownButton = Button(root,text='VolumeDown',background='blue',font=('arial',12,'italic bold'),width=15,bd=5,activebackground='pink',command=volumedown)
    VolumeDownButton.grid(row=2,column=2,padx=20,pady=20)

    root.MuteButton = Button(root,text="Mute",font=('arial',12,'italic bold'),width=10,bg='yellow',activebackground='pink',bd=5,command=mutemusic)
    root.MuteButton.grid(row=3,column=3)
    root.MuteButton.grid_remove()

    root.UnMuteButton = Button(root,text="UnMute",font=('arial',12,'italic bold'),width=10,bg='yellow',activebackground='pink',bd=5,command=unmutemusic)
    root.UnMuteButton.grid(row=3,column=3)
    root.UnMuteButton.grid_remove()
##################################################################################
# Progressbar Volume    
    ProgressbarLabel = Label(root,text='',bg='red')
    ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    ProgressbarLabel.grid_remove()

    ProgressBarVol = Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',value=0,length=190)
    ProgressBarVol.grid(row=0,column=0,ipadx=5)

    ProgressBarVolLabel = Label(ProgressbarLabel,text='0%',bg='lightgrey',width=3)
    ProgressBarVolLabel.grid(row=0,column=0)
#################################################################################
#ProgressBar Music
    ProgressbarMusicLabel = Label(root,text='',bg='red')
    ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
    ProgressbarMusicLabel.grid_remove()

    ProgressbarMusicStartLabel = Label(ProgressbarMusicLabel,text='0.00.0',bg='red',width=6)
    ProgressbarMusicStartLabel.grid(row=0,column=0)

    ProgressbarMusic = Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=0)
    ProgressbarMusic.grid(row=0,column=1,ipadx=300,ipady=3)
    
    ProgressbarMusicEndLabel = Label(ProgressbarMusicLabel,text='0.00.0',bg='red')
    ProgressbarMusicEndLabel.grid(row=0,column=2)
#################################################################################
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar 
import datetime
from mutagen.mp3 import MP3

root  = Tk()
root.geometry('950x370+200+50')
root.title('Minesh Music Player')
root.iconbitmap('music.ico')
root.resizable(False,False)
root.configure(bg="lightpink")
#global variable
audiotrack = StringVar()
currentvol = 0
totalsonglength=0
count = 0
text = ''
#CreateSlider
st= "Developed By Minesh Patel"
SliderLabel=Label(root,text=st,bg='lightpink',font=('arial',20,'italic bold'))
SliderLabel.grid(row=4,column=0,padx=20,pady=20,columnspan=3)
def IntroLabel1Trick():
    global count,text
    if (count>=len(st)):
        count= -1
        text = ''
        SliderLabel.configure(text=text)
    else:
        text = text +st[count]
        SliderLabel.configure(text=text)
    count += 1
    SliderLabel.after(200,IntroLabel1Trick)
IntroLabel1Trick()  
mixer.init()  
createwidthes()
root.mainloop()