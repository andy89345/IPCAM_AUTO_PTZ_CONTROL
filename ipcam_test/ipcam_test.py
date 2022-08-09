
import cv2
import os
import sys
from onvif import ONVIFCamera
import tkinter as tk
from tkinter import ttk
from multiprocessing import Process
from sensecam_control import vapix_control
from sensecam_control import onvif_control
import serial
#import serial.rs485
import time

#import cv2
import sys
import threading
from sensecam_control import onvif_control
import configparser

#ip = '192.168.0.172'
#login = 'admin'
#password = 'lunghwa123'

exit_program = 0
config = configparser.ConfigParser()
config.read('mypy.ini')
#print(config['mypy']['ip'])
#host = config['http']['host']
ip=config['mypy']['ip']
ip=str(ip).strip()
login=config['mypy']['login']
login=str(login).strip()
password=config['mypy']['password']
password=str(password).strip()
print(ip)
print(login)
print(password)
'''
def event_keyboard(k):
    global exit_program
    global ship_name
    global ret
    global frame
    global cap
  
    #cap=cv2.VideoCapture("rtsp://admin:lunghwa123@192.168.0.172/doc/page/login.asp?_1624435194210")
    #ret, frame = cap.read()
    if k == 27:  # esc
        exit_program = 1

    elif k == ord('w') or k == ord('W'):
        X.relative_move(0, -0.1, 0)
        
        #cv2.imwrite("test.jpg",ret)
        print("up")
    elif k == ord('a') or k == ord('A'):
        X.relative_move(0.1, 0, 0)
        
        #cv2.imwrite("test.jpg",ret)
        print("left")
    elif k == ord('s') or k == ord('S'):
        X.relative_move(0, 0.1, 0)
        
        #cv2.imwrite("test.jpg",ret)
        print("down")
    elif k == ord('d') or k == ord('D'):
        X.relative_move(-0.1, 0, 0)
        #ret, frame = cap.read()
        #cv2.imwrite("test.jpg",ret)
        print("right")
    elif k == ord('h') or k == ord('H'):
        X.go_home_position()

    elif k == ord('z') or k == ord('Z'):
        X.relative_move(0, 0, 0.05)

    elif k == ord('x') or k == ord('X'):
        X.relative_move(0, 0, -0.05)

    elif k == ord('c') or k == ord('C'):
        print("please enter name to save your img")
        act_cap=input()
        cap=cv2.VideoCapture("rtsp://admin:lunghwa123@192.168.0.172/doc/page/login.asp?_1624435194210")
        ret, frame = cap.read()
        print("ScreenShot################################################################")
        con_name=ship_name+"\\"+act_cap+".jpg"
        cv2.imwrite(con_name,frame)
'''
  

def capture(ip_camera,dec):
    global exit_program

    #url http login axis camera
    #ip2 = 'http://' + login + ':' + password + '@' + ip_camera + '/mjpg/1/video.mjpg?'

    #url rtsp axis camera
    #ip2 = 'rtsp://192.168.0.172:554' + login + ':' + password + '@' + ip_camera + '/doc/page/login.asp?_1624435194210'
    cap=cv2.VideoCapture("rtsp://admin:lunghwa123@10.0.0.172/doc/page/login.asp?_1659669219794")
    #cap = cv2.VideoCapture(ip2)



    while True:
        if dec==False:
            break
        else:
            ret, frame = cap.read()

            #if exit_program == 1:
            #    sys.exit()

            cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)
            cv2.line(frame, (620,360), (660, 360), (0, 255, 0), 2)
            cv2.line(frame, (640,340), (640, 380), (0, 255, 0), 2)

            #cv2.resizeWindow("Camera", 1300, 1100);
            cv2.imshow('Camera', frame)
            cv2.waitKey(1) & 0xff
        
        #event_keyboard(cv2.waitKey(1) & 0xff)
qq=True
X = onvif_control.CameraControl(ip,login, password)
X.camera_start()

t = threading.Thread(target=capture, args=(ip,qq))
t.start()

kill=True 
y_count=0
def auto_snap(pau):
    #try:
   
    global y_count
    global qq
    global X
    global t
    global file
    global angle_test
    global angle_test_Y
    global kill
    kill=True
    
    if pau==0:
        #print("please enter ship name:")
        #ship_name=input()
        #print("please enter per angle:")
        #angle=input()
        #angle=int(angle)
        ship_name=str(file.get())
        if ship_name=="":
            resultString.set("Please enter File name")
        if not ship_name:
            resultString.set("Please enter File name")
        angle=str(angle_test.get())
        if angle=="":
            resultString.set("Please enter X_Angle")
            angle="0"
        if not angle:
            resultString.set("Please enter X_Angle ")
        angle_y=str(angle_test_Y.get())
        if angle_y=="":
            resultString.set("Please enter Y_Angle")
            angle_y="0"
        if not angle_y:
            resultString.set("Please enter Y_Angle")

        #angle=int(angle)
        angle=int(angle)
        angle_y=int(angle_y)

        folder = os.path.exists(ship_name)
        if not folder:
            os.mkdir(ship_name)
            suc="The "+ship_name+" was build"
            resultString.set(suc)
        #X = onvif_control.CameraControl(ip, login, password)
        #X.camera_start()

        #t = threading.Thread(target=capture, args=(ip,qq))
        #t.start()
        X.go_home_position()
        resultString.set("Go home position,please wait")
        time.sleep(9)
        cap=cv2.VideoCapture("rtsp://admin:lunghwa123@10.0.0.172/doc/page/login.asp?_1659669219794")
        ret, frame = cap.read()
        cv2.line(frame, (620,360), (660, 360), (0, 255, 0), 2)
        cv2.line(frame, (640,340), (640, 380), (0, 255, 0), 2)
        print("ScreenShot################################################################")
        con_name=ship_name+"\\"+"home_position.jpg"
        cv2.imwrite(con_name,frame)
        resultString.set("Your image was saved")
        #angle_count=360/angle
        name_array=[]
        head_y=[]
        count=0
        cy=0
        for j in range(angle,360,angle):
            name_array.append(str(j))
            count=count+1
        new_count=count-1
        name_array.append("360")
        if angle_y!=0:
            for t in range(0,90,angle_y):
                head_y.append(str(t))
                cy=cy+1
            new_cy=cy-1
            head_y.append("90")
        else:
            head_y.append("0")
            
        

        #name_array.append("deviation2")
        haha=angle/180
        haha=float(haha)
        haha_y=angle_y/90
        haha_y=float(haha_y)
            
        for n in head_y:     
            if kill==True:
                file_xy=ship_name+"\\"+n
                folder2 = os.path.exists(file_xy)
                if not folder2:
                    os.mkdir(file_xy)
                
                if n =="90":
                    dataY=head_y[new_cy]
                    dataY=int(dataY)
                    print("the Y dev is :")
                    print(dataY)
                    suby=90-dataY
                    new_suby=suby/90
                    X.relative_move(0,-haha_y_y,0)
                    time.sleep(3)
                    X.relative_move(0, -new_suby, 0)
                    time.sleep(2)
                    cap=cv2.VideoCapture("rtsp://admin:lunghwa123@10.0.0.172/doc/page/login.asp?_1659669219794")
                    ret, frame = cap.read()
                    know=ship_name+"\\"+n+"\\"+"0,"+str(n)+".jpg"
                    cv2.imwrite(know,frame)
                    print("ScreenShot~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    time.sleep(1)
                else:
                    haha_y_y=haha_y*y_count
                    X.relative_move(0,-haha_y_y,0)
                    y_count=y_count+1
                    time.sleep(2)
                    cap=cv2.VideoCapture("rtsp://admin:lunghwa123@10.0.0.172/doc/page/login.asp?_1659669219794")
                    ret, frame = cap.read()
                    know=ship_name+"\\"+n+"\\"+"0,"+str(n)+".jpg"
                    cv2.imwrite(know,frame)
                    Ypo="Position:"+"("+"0"+","+n+")"
                    resultString.set(Ypo)
                    print("ScreenShot~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    time.sleep(1)
                    resultString.set("Your image was saved")
                    time.sleep(1)
                for i in name_array:                   
                    if kill==True:
                        if i=="360":                           
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            #X.absolute_move(-0.09, 0.49, 0)
                            data1=name_array[new_count]
                            data1=int(data1)
                            print("the X dev is :")
                            print(data1)
                            sub=360-data1
                            new_sub=sub/180
                            if new_sub!=0:
                                X.relative_move(-new_sub, 0, 0)
                                resultString.set("Turn remaining angles")
                                time.sleep(3)
                            #if angle>50:
                            #    X.relative_move(0.1, 0, 0)
                            #    time.sleep(3)
                            #X.relative_move(-0.1, 0, 0)
                            #resultString.set("Turn error compensation value")
                            time.sleep(3)
                            cap=cv2.VideoCapture("rtsp://admin:lunghwa123@10.0.0.172/doc/page/login.asp?_1659669219794")
                            ret, frame = cap.read()
                            cv2.line(frame, (620,360), (660, 360), (0, 255, 0), 2)
                            cv2.line(frame, (640,340), (640, 380), (0, 255, 0), 2)
                            print("ScreenShot################################################################")
                            x=ship_name+"\\"+n+"\\"+i+" , "+n+".jpg"
                            cv2.imwrite(x,frame)
                            resultString.set("Your image was saved")
                            time.sleep(1)
                            X.go_home_position()
                            resultString.set("Go home position,please wait")
                            time.sleep(9)
                            
                        else:                                                      
                            X.relative_move(-haha, 0, 0)
                            time.sleep(3)
                            reveal_angle="Position:"+"("+i+","+n+")"
                            resultString.set(reveal_angle)
                            time.sleep(2)                   
                            cap=cv2.VideoCapture("rtsp://admin:lunghwa123@10.0.0.172/doc/page/login.asp?_1659669219794")
                            ret, frame = cap.read()
                            cv2.line(frame, (620,360), (660, 360), (0, 255, 0), 2)
                            cv2.line(frame, (640,340), (640, 380), (0, 255, 0), 2)
                            print("ScreenShot################################################################")
                            x=ship_name+"\\"+n+"\\"+i+" , "+n+".jpg"
                            cv2.imwrite(x,frame)
                            resultString.set("Your image was saved")
                    elif kill==False:
                        X.stop_move() 
                        resultString.set("Motion Stop!!!!!!!!!!!!!!!")
            elif kill==False:
                X.stop_move() 
                resultString.set("Motion Stop!!!!!!!!!!!!!!!")
        #cap.release()
        #cv2.destroyAllWindows()
        qq=False
        print("Finish")
        y_count=0
        resultString.set("Motion Finish!!!")
    elif pau==1:
        X.stop_move() 
        resultString.set("Motion Stop!!!!!!!!!!!!!!!")
    #except:
    #    print("error")


snapx=0
snapy=0
def auto_thread():
    global t2
    t2 = threading.Thread(target=auto_snap, args=(0,))
    #t2=Process(target=auto_snap,args=(0,))
    t2.start()


def right():
    global snapx
    global snapy
    global test
    angle_right=str(angle_test.get())
    if not angle_right:
        resultString.set("Please enter Angle")
    angle_right=int(angle_right)
    if angle_right>180:
        resultString.set("Angle_X need to < = 180")
    elif angle_right<0:
        resultString.set("Angle_X need to > = 0")
    if (angle_right<=180) and (angle_right>=0):
        snapx=snapx+angle_right
        if snapx>360:
            snapx=snapx-360
    
        if snapx<=66:
            if snapx<=0:
                snapx=360+snapx
            else:
                if snapy>=45 and snapy<=90:
                    gaga_abs_R=gaga_array[snapy-45]
                    snapy_R=1-gaga_abs_R
                    absR=float(snapy/1486)
                elif snapy>90:
                    resultString.set("Angle_Y need to <=90")
                else:
                    if snapy==0:
                        absR=1
                        absR=float(absR)
                    else:
                        snapy_R=45-snapy
                        absR=float(snapy_R/45)
                abs_x_R=float(snapx/169)
                X.absolute_move(-abs_x_R,absR,0)
        elif snapx<360:
            if snapy>=45 and snapy<=90:
                gaga_abs_RR=gaga_array[snapy-45]
                snapy_RR=1-gaga_abs_RR
                absRR=float(snapy/1486)
            elif snapy>90:
                resultString.set("Angle_Y need to <=90")
            else:
                if snapy==0:
                    absRR=1
                    absRR=float(absRR)
                else:
                    snapy_RR=45-snapy
                    absRR=float(snapy_RR/45)
            if snapx>=0 and snapx<=6:
                abs_x_RR=float(snapx/169)
                X.absolute_move(-abs_x_RR,absRR,0)
            elif snapx>=354 and snapx<=360:
                abs_x_RRR=float((360-snapx)/169)
                X.absolute_move(abs_x_RRR,absRR,0)
            else:
                new_angle_right=float(angle_right/180)
                X.relative_move(-new_angle_right, 0, 0)
            time.sleep(1)
        elif snapx==360:
            

            if snapy>=45 and snapy<=90:
                gaga_abs_R2=gaga_array[snapy-45]
                snapy_R2=1-gaga_abs_R2
                absR2=float(snapy/1486)
            elif snapy>90:
                resultString.set("Angle_Y need to <=90")
            else:
                if snapy==0:
                    absR2=1
                    absR2=float(absR2)
                else:
                    snapy_R2=45-snapy
                    absR2=float(snapy_R2/45)
                #abs_x_R=float(snapx/169)
            X.absolute_move(0,absR2,0)
        right_txt="Position: "+"("+str(snapx)+","+str(snapy)+")"
        resultString.set(right_txt)
        if snapx>=360:
            snapx=0
        print(snapx)
def up():
    global snapx
    global snapy
    angle_up=str(angle_test_Y.get())
    if not angle_up:
        resultString.set("Please enter Angle")
    angle_up=int(angle_up)
    if angle_up>90:
        resultString.set("Angle_Y need to < = 90")
    elif angle_up<0:
        resultString.set("Angle_Y need to > = 0")
    if (angle_up>=0) and (angle_up<=90):
        snapy=snapy+angle_up
        if snapy>=90:
            snapy=90

        new_angle_up=float(angle_up/90)
        X.relative_move(0, -new_angle_up, 0)
        up_txt="Position: "+"("+str(snapx)+","+str(snapy)+")"
        resultString.set(up_txt)

def left():
    global absX
    global absY
    global snapx
    global snapy
    angle_left=str(angle_test.get())
    if not angle_left:
        resultString.set("Please enter Angle")
    angle_left=int(angle_left)
    if angle_left>180:
        resultString.set("Angle_X need to < = 180")
    elif angle_left<0:
        resultString.set("Angle_X need to > = 0")
    if (angle_left>=0) and (angle_left<=180): 
        snapx=snapx-angle_left
        if snapx<0:
            snapx=snapx+360
            #new_angle_left=float(angle_left/180)
            #X.relative_move(new_angle_left, 0, 0)
        if snapx==0:
            if snapy>=45 and snapy<=90:
                gaga_abs_L=gaga_array[snapy-45]
                snapy_L=1-gaga_abs_L
                absY=float(snapy/1486)
            elif snapy>90:
                resultString.set("Angle_Y need to <=90")
            else:
                if snapy==0:
                    absY=1
                    absY=float(absY)
                else:
                    snapy_L=45-snapy
                    absY=float(snapy_L/45)
            snapx=snapx+360
            X.absolute_move(0,absY,0)
        else:
            if snapy>=45 and snapy<=90:
                gaga_abs_L2=gaga_array[snapy-45]
                snapy_L2=1-gaga_abs_L2
                absY2=float(snapy/1486)
            elif snapy>90:
                resultString.set("Angle_Y need to <=90")
            else:
                if snapy==0:
                    absY2=1
                    absY2=float(absY2)
                else:
                    snapy_L2=45-snapy
                    absY2=float(snapy_L2/45)
            #snapx=snapx+360
            if snapx>=354 and snapx<=360:
                abs_x_R2=float((360-snapx)/169)
                X.absolute_move(abs_x_R2,absY,0)
            elif snapx>=0 and snapx<=6:
                abs_x_R2R=float(snapx/169)
                X.absolute_move(-abs_x_R2R,absY,0)
            else:    
                new_angle_left=float(angle_left/180)
                X.relative_move(new_angle_left, 0, 0)
        left_txt="Position: "+"("+str(snapx)+","+str(snapy)+")"
        resultString.set(left_txt)
        if snapx<=0:
            snapx=0
        print(snapx)
def down():
    global snapx
    global snapy
    angle_down=str(angle_test_Y.get())
    if not angle_down:
        resultString.set("Please enter Angle")
    angle_down=int(angle_down)
    if angle_down>90:
        resultString.set("Angle_Y need to < = 90")
    elif angle_down<0:
        resultString.set("Angle_Y need to > = 0")
    if (angle_down>=0) and (angle_down<=90):
        snapy=snapy-angle_down
        if snapy<=0:
            snapy=0
        new_angle_down=float(angle_down/90)
        X.relative_move(0, new_angle_down, 0)
        down_txt="Position: "+"("+str(snapx)+","+str(snapy)+")"
        resultString.set(down_txt)

def home():
    global snapx
    global snapy
    snapx=0
    snapy=0
    X.go_home_position()
    #time.sleep(9)
    #X.relative_move(-0.4, 0, 0)
    time.sleep(3)
    #X.go_home_position()
    home_pos="Home position: "+"("+str(snapx)+","+str(snapy)+")"
    resultString.set(home_pos)

def snap():
    global cap
    global ret
    global frame
    global active_snap_count
    ship_name_snap=str(file.get())
    path=ship_name_snap+"\\"+"Snapshot"
    if not(ship_name_snap):
        resultString.set("Please enter File name")
    folder_name = os.path.exists(ship_name_snap)
    folder_name2 = os.path.exists(path)
    if not folder_name:
        os.mkdir(ship_name_snap)
        os.mkdir(path)
        cap=cv2.VideoCapture("rtsp://admin:lunghwa123@10.0.0.172/doc/page/login.asp?_1659669219794")
        ret, frame = cap.read()
        cv2.line(frame, (620,360), (660, 360), (0, 255, 0), 2)
        cv2.line(frame, (640,340), (640, 380), (0, 255, 0), 2)
        print("ScreenShot################################################################")
        x=ship_name_snap+"\\"+"Snapshot"+"\\"+"Snapshot_"+"("+str(snapx)+","+str(snapy)+")"+".jpg"
        cv2.imwrite(x,frame)
        active_snap_count=active_snap_count+1
        resultString.set("Your image was saved")
    else:
        if not folder_name2:
            os.mkdir(path)
        cap=cv2.VideoCapture("rtsp://admin:lunghwa123@10.0.0.172/doc/page/login.asp?_1659669219794")
        ret, frame = cap.read()
        cv2.line(frame, (620,360), (660, 360), (0, 255, 0), 2)
        cv2.line(frame, (640,340), (640, 380), (0, 255, 0), 2)
        print("ScreenShot################################################################")
        x=ship_name_snap+"\\"+"Snapshot"+"\\"+"Snapshot_"+"("+str(snapx)+","+str(snapy)+")"+".jpg"
        cv2.imwrite(x,frame)
        active_snap_count=active_snap_count+1
        resultString.set("Your image was saved")
gaga_num=1
gaga_array=[]
for gaga in range(0,46,1):
    gaga_array=gaga_array+[gaga_num]
    gaga_num=gaga_num+33
print(gaga_array)

def stop():
    #global t2
    #t2.terminate()
    global t2
    global kill
    kill=False
    #sys._exit(0)
    X.stop_move() 
    resultString.set("Motion Stop!!!!!!!!!!!!!!!")
absX=0
absY=1
def abs():
    global absX
    global absY
    global snapx
    global snapy
    global gaga_array
    angle_abs_x=str(angle_test.get())
    angle_abs_y=str(angle_test_Y.get())
    angle_abs_y2=str(angle_test_Y.get())
    
    if not angle_abs_x:
        resultString.set("Please enter Angle_X")
    elif not angle_abs_y:
        resultString.set("Please enter Angle_Y")
    angle_abs_x=int(angle_abs_x)
    angle_abs_y=int(angle_abs_y)
    if angle_abs_y>=45 and angle_abs_y<=90:
        gaga_abs=gaga_array[angle_abs_y-45]
        angle_abs_y=1-gaga_abs
        abs_y=float(angle_abs_y/1486)
    elif angle_abs_y>90:
        resultString.set("Angle_Y need to <=90")
    else:
        if angle_abs_y==0:
            abs_y=1
            abs_y=float(abs_y)
        else:
            angle_abs_y=45-angle_abs_y
            abs_y=float(angle_abs_y/45)
    if angle_abs_x<=180:
        #abs_x=float(angle_abs_x/180)
        if angle_abs_x<=66:
            abs_x=float(angle_abs_x/169)
        else:
            abs_x=float(angle_abs_x/169)
    elif angle_abs_x>180:
        abs_x=360-angle_abs_x
        abs_x=-float(abs_x/180)
    

    X.absolute_move(-abs_x,abs_y,0)
    abs_position="Abs :"+"("+str(angle_abs_x)+","+str(angle_abs_y2)+")"
    resultString.set(abs_position)
    snapx=int(angle_abs_x)
    snapy=int(angle_abs_y2)
    absY=abs_y
'''
print("First home position------->>>>")
X.go_home_position()
time.sleep(9)
X.relative_move(-0.05, 0, 0)
time.sleep(3)
X.set_home_position()
print("set home ~~~~~~~~~~~~~`")
time.sleep(10)
'''

X.go_home_position()
time.sleep(9)

active_snap_count=0

app = tk.Tk() 
app.iconbitmap("LH.ico")
app.title("Lunghwa_camera")
app.geometry('300x320')

label_file_name = tk.Label(app, text = "File name")
label_file_name.grid(column=0, row=0)
label_angle_X = tk.Label(app, text = "X-Angle")
label_angle_X.grid(column=0, row=1)
label_angle_Y = tk.Label(app, text = "Y-Angle")
label_angle_Y.grid(column=0, row=2)


file = tk.StringVar()
angle_test = tk.StringVar()
angle_test_Y = tk.StringVar()
entryfile = tk.Entry(app, width=20, textvariable=file)
entryangle = tk.Entry(app, width=20, textvariable=angle_test)
entryangle_Y = tk.Entry(app, width=20, textvariable=angle_test_Y)

entryfile.grid(column=1, row=0, padx=10)
entryangle.grid(column=1, row=1, padx=10)  
entryangle_Y.grid(column=1, row=2, padx=10)    
     
resultButton = tk.Button(app, text = 'Auto Screenshots',width=20,command=auto_thread)

resultButton.grid(column=1, padx=0,row=4)

up_Button = tk.Button(app, text = 'Up',width=20,command=up)

up_Button.grid(column=1, row=5)

left_Button = tk.Button(app, text = 'Left',width=20,command=left)

left_Button.grid(column=1, row=6)

right_Button = tk.Button(app, text = 'Right',width=20,command=right)

right_Button.grid(column=1, row=7)

down_Button = tk.Button(app, text = 'Down',width=20,command=down)

down_Button.grid(column=1, row=8)

home_Button = tk.Button(app, text = 'Home',width=20,command=home)

home_Button.grid(column=1, row=9)

snap_Button = tk.Button(app, text = 'Screenshots',width=20,command=snap)

snap_Button.grid(column=1, row=10)

stop_Button = tk.Button(app, text = 'Stop',width=20,command=stop)

stop_Button.grid(column=1, row=11)

abs_Button = tk.Button(app, text = 'Absolute',width=20,command=abs)

abs_Button.grid(column=1, row=12)


resultString=tk.StringVar()
resultLabel = tk.Label(app, textvariable=resultString)
resultLabel.grid(column=1, row=13)

app.mainloop()

'''
cam=cv2.VideoCapture("rtsp://admin:lunghwa123@10.0.0.172/doc/page/login.asp?_1659669219794")

while True:
    ret,img=cam.read()
    cv2.imshow("camera",img)
    if 0xFF & cv2.waitKey(5)==27:
        break
cv2.destroyAllWindows()
'''