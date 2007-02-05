# webinstaller.nsi
# installer for debunk2 -- ripped off the ffmpeg installer
# havard@dahle.no (C) 2007 -- GPLv2
# 
# much gore extracted from the pluginImportersExporters.nsi script of the AbiWord project. 
# 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; set version defaults
!ifndef VERSION_MAJOR
!define VERSION_MAJOR "0"
!endif

!ifndef VERSION_MINOR
!define VERSION_MINOR "5"
!endif

;!ifndef VERSION_MICRO
;!define VERSION_MICRO "3"
;!endif

; set download urls
!ifndef RUNTIME_URL
;!define RUNTIME_URL "http://debunk2.google.com/files/debunk2-runtime"
!define RUNTIME_URL "http://www.orakel.ntnu.no/~havardda/dok_temp/debunk2-runtime.zip"
!endif

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; Do a Cyclic Redundancy Check to make sure the installer
; was not corrupted by the download.
CRCCheck on

; set the compression algorithm used, zlib | bzip2 | lzma
SetCompressor /SOLID lzma

; The name of the installer
Name "debuNK2"

; XPStyle makes the installer controls use the new XP style when running on Windows XP.
XPStyle On

; output file name
OutFile ".\dist\debunk2_${VERSION_MAJOR}.${VERSION_MINOR}_webinstall.exe"

; License Information
LicenseText "This program is Licensed under the GNU General Public License (GPL).\r\nYou must agree to this license before you are permitted to use it." "$(^NextBtn)"
LicenseData "LICENSE.txt"

; the default installation directory
InstallDir "$PROGRAMFILES\debunk2"

; Registry key to check for directory (so if you install again, it will overwrite the old one automatically)
InstallDirRegKey HKLM SOFTWARE\debuNK2\v${VERSION_MAJOR} "Install_Dir"

; Introducing the installer
ComponentText "This will install debuNK2 on your computer."

;The text to prompt the user to enter a directory
;DirText "Please select the folder where you want to install debuNK2. If you're upgrading, choose the folder of the previous installation."

;;;;;;;;;;;;;;;;;;;;;;;;MACROS;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
!macro dlFileMacro remoteFname localFname errMsg
        ; from pluginImportersExporters.nsi
        !define retryDLlbl retryDL_${__FILE__}${__LINE__}
        !define dlDonelbl dlDoneDL_${__FILE__}${__LINE__}

        ;Call ConnectInternet   ; try to establish connection if not connected
        ;StrCmp $0 "online" 0 ${dlDonelbl}

        ${retryDLlbl}:
        NSISdl::download "${remoteFname}" "${localFname}"
        Pop $0 ;Get the return value
        StrCmp $0 "success" ${dlDonelbl}
                ; Couldn't download the file
                DetailPrint "${errMsg}"
                DetailPrint "Remote URL: ${remoteFname}"
                DetailPrint "Local File: ${localFname}"
                DetailPrint "NSISdl::download returned $0"
                MessageBox MB_RETRYCANCEL|MB_ICONEXCLAMATION|MB_DEFBUTTON1 "${errMsg}" IDRETRY ${retryDLlbl}
        ${dlDonelbl}:
        !undef retryDLlbl
        !undef dlDonelbl
!macroend
!define dlFile "!insertmacro dlFileMacro"

; USAGE: 
; ${dlFile} "http://www.abisource.com/downloads/dependencies/libxml2/libxml2-2.6.19-runtime.zip" "$TEMP\libxml2-2.6.19-runtime.zip" "ERROR: Dependency download failed.  Please make sure you are connected to the Internet, then click Retry.  File: http://www.abisource.com/downloads/dependencies/libxml2/libxml2-2.6.19-runtime.zip"
;        StrCmp $0 "success" 0 doCleanup

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Macro for unzipping a file from an archive with error reporting
!macro unzipFileMacro archiveFname destinationPath errMsg
        ; from pluginImportersExporters.nsi
        !define uzDonelbl uzDone_${__FILE__}${__LINE__}

        ZipDLL::extractall "${archiveFname}" "${destinationPath}"
        Pop $0 ; Get return value
        StrCmp $0 "success" ${uzDonelbl}
                ; Couldn't unzip the file
                DetailPrint "${errMsg}"
                MessageBox MB_OK|MB_ICONEXCLAMATION|MB_DEFBUTTON1 "${errMsg}" IDOK
        ${uzDonelbl}:
        !undef uzDonelbl
!macroend
!define unzipFile "!insertmacro unzipFileMacro"

; USAGE:
;${unzipFile} "$TEMP\libxml2-2.6.19-runtime.zip" "$INSTDIR\AbiWord" "bin\libxml2.dll" "ERROR: failed to extract libxml2.dll from libxml2-2.6.19-runtime.zip"
;        StrCmp $0 "success" 0 doCleanup
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;LET'S START THE PARTY;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


#Page custom customPage
Page components
Page license
Page directory 
Page instfiles

Section "Required libraries"
        ; Testing clause to see if important dlls exist
        IfFileExists "$INSTDIR\debuNK2\python25.dll" DontInstall 0
        
        ; slurp the dlls
        ${dlFile} "${RUNTIME_URL}" "$TEMP\debuNK2-runtime.zip" "ERROR: Dependency download failed.  Please make sure you are connected to the Internet, then click Retry.  File: ${RUNTIME_URL}"
        StrCmp $0 "success" 0 doCleanup
        
        ; explode the dlls
        ${unzipFile} "$TEMP\debuNK2-runtime.zip" "$INSTDIR\debuNK2" "" "ERROR: failed to extract debuNK2-runtime.zip"
        StrCmp $0 "success" 0 doCleanup
        
        
        doCleanup:
            ; delete temp files
            Delete "$TEMP\debuNK2-runtime.zip"
        DontInstall:
            ; naught
SectionEnd


Section "Install"
  ;Install Files
  SetOutPath $INSTDIR
  SetCompress Auto
  SetOverwrite IfNewer
  File ".\win\debunk2.exe"
  File ".\debunk2.pyw"
  File ".\debunk2_gui.py"
  File ".\debunk2_ui.py"
  File ".\nk2parser.py"
  File ".\LICENSE.txt"

/*
  ; documentation
  #SetOutPath $INSTDIR\doc
  #File ".\doc\faq.html"
  #File ".\doc\ffmpeg-doc.html"
  #File ".\doc\ffplay-doc.html"

  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\debuNK2" "DisplayName" "debuNK2 (remove only)"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\debuNK2" "UninstallString" "$INSTDIR\debuNK2-uninst.exe"
WriteUninstaller "debuNK2-uninst.exe"
*/
SectionEnd

Section "Shortcuts"
  ;Add Shortcuts
SectionEnd

UninstallText "This will uninstall debuNK2 from your system"

/*
Section Uninstall
  ; delete files
  Delete "$INSTDIR\ffmpeg.exe"
  Delete "$INSTDIR\SDL.dll"
  Delete "$INSTDIR\ffplay.exe"
  Delete "$INSTDIR\COPYING"
  Delete "$INSTDIR\CREDITS"

  ; delete documentation
  Delete "$INSTDIR\doc\faq.html"
  Delete "$INSTDIR\ffmpeg-doc.html"
  Delete "$INSTDIR\doc\ffplay-doc.html"

  RMDir /r $INSTDIR\doc

  ; delete uninstaller and unistall registry entries
  Delete "$INSTDIR\Uninst.exe"
  DeleteRegKey HKEY_LOCAL_MACHINE "SOFTWARE\FFmpeg"
  DeleteRegKey HKEY_LOCAL_MACHINE "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\FFmpeg"
  RMDir "$INSTDIR"
SectionEnd
*/

/*
Section "LaTeX"
        SectionIn 2

        ; Testing clause to Overwrite Existing Version - if exists
        IfFileExists "$INSTDIR\AbiWord\plugins\AbiLaTeX.dll" 0 DoInstall

        MessageBox MB_YESNO "Overwrite Existing AbiLaTeX Plugin?" IDYES DoInstall

        DetailPrint "Skipping AbiLaTeX Plugin (already exists)!"
        Goto End

        DoInstall:
        File "AbiLaTeX.dll"

        End:
SectionEnd
*/