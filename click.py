# -*- coding: utf-8 -*-
import win32api 
import win32gui 
import win32con 
import time 
import ctypes
import pyHook
import threading
import pythoncom 

flag=0   #标记 0：未开始点击，1：开始    2：停止

def click(): 
		pos=win32api.GetCursorPos()
		x=pos[0]
		y=pos[1]
		win32api.SetCursorPos((x,y))
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def onKeyboardEvent(event):
	# 监听键盘事件
	'''
	print "MessageName:", event.MessageName
	print "Message:", event.Message
	print "Time:", event.Time
	print "Window:", event.Window
	print "WindowName:", event.WindowName
	print "Ascii:", event.Ascii, chr(event.Ascii)
	print "Key:", event.Key
	print "KeyID:", event.KeyID
	print "ScanCode:", event.ScanCode
	print "Extended:", event.Extended
	print "Injected:", event.Injected
	print "Alt", event.Alt
	print "Transition", event.Transition
	print "---"
	'''
	global flag
	if event.Key=='S':     #按下S开始
		flag=1
	elif event.Key=='E':   #E结束
		flag=2
	return True

def createKeyboardListen():
	# 创建一个“钩子”管理对象
	hm = pyHook.HookManager()
	# 监听所有键盘事件
	hm.KeyDown = onKeyboardEvent
	# 设置键盘“钩子”
	hm.HookKeyboard()
	# 开始监听
	pythoncom.PumpMessages() 

def main():
	print '将鼠标移动到需要点击的位置，按下键盘s'
	#单独开一个线程用于监听键盘按键
	t=threading.Thread(target=createKeyboardListen,args=())
	#开启线程
	t.start()
	#鼠标点击
	while(1):
		time.sleep(1)    #每隔1秒鼠标点1次
		if flag==1:
			click()
		elif flag==2:
			break
		#print flag

main()

