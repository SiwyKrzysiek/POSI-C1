#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#SingleInstance Force
iteration := 100
max := 499
dataPath := "D:\Studia\PodstawySztucznejInteligencjii\Laby\C\1\Pomiary\Rosenbrock\50;95;0\data" 

#t::
	if (iteration > max) {
		iteration := max
	}
	Send %iteration%
	Send ^l
	Send %dataPath%{Enter}
	Sleep, 450
	Click, 1221, 1042
	iteration := iteration + 50

return