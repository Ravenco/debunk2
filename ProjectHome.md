Microsoft Outlook stores its **autocomplete email info** in an undocumented file format. This project tries to unlock the information therein.

### Current status ###

2007-02-02: Version 0.5 has been released, with an installer for MS Windows. Instructions:

  1. Download the `debunk2-0.5-win.exe` installer (from the list on the right)
  1. Run the installer and choose target folder (does not require admin rights)
  1. Run `debunk2.exe`  (Currently, no program shortcuts are created.)

New in this version:

  * Automatically locates your default NK2 file(s).
  * If the record doesn't have something that looks like a name, it is reconstructed by looking at the e-mail field (like Gmail)
  * Code is rearranged, so that future updates won't require a full download

Please post problems and praise to [the list](http://groups.google.com/group/debunk2)


### Export formats ###


  * CSV/TSV - comma-, tab-, and semicolon-separated lists
  * vCard - virtual business cards (vcf)

  * SyncML - an xml dialect of vcard (_planned_)

