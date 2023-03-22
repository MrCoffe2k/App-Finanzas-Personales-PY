; Includes
!include "MUI2.nsh"
!include "LogicLib.nsh"
!include "WinVer.nsh"
!include "x64.nsh"

; The name of the installer
Name "Sin Un Cinco"

; The file to write
OutFile "SinUnCincoInstaller.exe"

; The default installation directory
InstallDir "$PROGRAMFILES\J&M Solutions\Sin Un Cinco"

; Request application privileges for Windows Vista/7/8/10
RequestExecutionLevel admin

; Pages
!insertmacro MUI_PAGE_WELCOME
;!insertmacro MUI_PAGE_LICENSE ".\output\SinUnCinco\license.txt"
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

; Languages
!insertmacro MUI_LANGUAGE "English"

; Installer sections
Section "Sin Un Cinco" SecSinUnCinco
    ; Set output path to the installation directory.
    SetOutPath $INSTDIR

    ; Put the files into the installation directory.
    File /r ".\output\SinUnCinco\*"

    ; Write the installation path into the registry.
    WriteRegStr HKLM "Software\J&M Solutions\Sin Un Cinco" "" $INSTDIR

    ; Create a shortcut on the Start Menu
    CreateDirectory "$SMPROGRAMS\J&M Solutions"
    CreateShortCut "$SMPROGRAMS\J&M Solutions\Sin Un Cinco.lnk" "$INSTDIR\SinUnCinco.exe"

    ; Create a shortcut on the desktop
    CreateDirectory "$DESKTOP"
    CreateShortCut "$DESKTOP\Sin Un Cinco.lnk" "$INSTDIR\SinUnCinco.exe"

SectionEnd

; Uninstaller section
Section "Uninstall"
    ; Remove registry keys
    DeleteRegKey HKLM "Software\J&M Solutions\Sin Un Cinco"

    ; Remove files and uninstaller
    Delete "$INSTDIR\SinUnCinco.exe"
    RMDir "$INSTDIR"
    Delete "$INSTDIR\uninstall.exe"

    ; Remove shortcuts
    Delete "$SMPROGRAMS\J&M Solutions\Sin Un Cinco.lnk"
    RMDir "$SMPROGRAMS\J&M Solutions"

SectionEnd
