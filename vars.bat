@echo off
rem
rem This file is generated
rem

rem python setup.py py2exe --includes sip

echo Setting up a MinGW/Qt only environment...
echo -- QTDIR set to C:\Qt
echo -- PATH set to C:\Qt\bin
echo -- Adding C:\qt\MinGW\bin to PATH
echo -- Adding %SystemRoot%\System32 to PATH
echo -- QMAKESPEC set to win32-g++

set QTDIR=C:\Qt
set PATH=C:\Qt\bin
set PATH=%PATH%;C:\qt\MinGW\bin
set PATH=%PATH%;%USERPROFILE%\prog\python25
set PATH=%PATH%;%SystemRoot%\System32
set QMAKESPEC=win32-g++


