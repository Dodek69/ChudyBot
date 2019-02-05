@echo off
MODE 140,30
title ChudyBot 0.9.9_69 Updater
color 02 
update.py
SET /P y=Run the bot?: 
IF "%y%"=="y" GOTO y
IF "%y%"=="yes" GOTO y
exit
:y
START "" setup.exe /HIGH
exit
