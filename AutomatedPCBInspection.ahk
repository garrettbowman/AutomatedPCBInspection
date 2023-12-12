; o::Run "C:\Program Files\Leica Microsystems CMS GmbH\LAS X\BIN\LMSApplicationDVM.exe"

#Include WaitPixelColor.ahk
CoordMode, Mouse, Screen

\::

WinActivate, Chrome Remote Desktop - Google Chrome
Click, 1758 373
Send, 1
send, {enter}
Sleep, 25000 ; placing PCB 

WinActivate, LAS X

MouseMove, 1205, 650
Loop, 100 {
 Send {WheelUp}
 Sleep, 100
}

Click, 1592 412

Click, 1470 743 ; fullscan

Sleep, 1000 ; save 

Click, 800 565 

Sleep, 1000 

Click, 1190 673 ; Potential overwrite msg

sleep, 25000

Click, 1494 691 ; Potential rotation error msg

WaitPixelColor(0xFFFFFF,1480,533)
Sleep, 1000
;Sleep, 85000 ; whole scan time

Click, 1472 412

Click, 1592 412


MouseMove, 1205, 650
Loop, 120 {
 Send {WheelDown}
 Sleep, 100
}

Sleep, 1000 ; 

WinActivate, Chrome Remote Desktop - Google Chrome
Click, 1758 373
Send, 2
send, {enter}
Sleep, 25000 ; placing PCB 

;SECOND PCB

WinActivate, Chrome Remote Desktop - Google Chrome
Click, 1758 373
Send, 3
send, {enter}
Sleep, 25000 ; placing PCB 

WinActivate, LAS X

MouseMove, 1205, 650
Loop, 100 {
 Send {WheelUp}
 Sleep, 100
}

Click, 1592 412

Click, 1470 743 ; fullscan

Sleep, 1000 ; save 

Click, 800 565 

Sleep, 1000 

Click, 1190 673 ; Potential overwrite msg

sleep, 25000

Click, 1494 691 ; Potential rotation error msg

;sleep, 85000 ; whole scan time
WaitPixelColor(0xFFFFFF,1480,533)
Sleep, 1000

Click, 1472 412

Click, 1592 412


MouseMove, 1205, 650
Loop, 120 {
 Send {WheelDown}
 Sleep, 100
}

WinActivate, Chrome Remote Desktop - Google Chrome
Click, 1758 373
Sleep, 1000 
Send, 4
send, {enter}
Sleep, 25000 ; placing PCB 
