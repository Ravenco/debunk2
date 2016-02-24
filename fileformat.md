#summary The NK2 file format explained.
#labels Featured,Phase-Implementation

# Introduction #

_Microsoft Outlook_ stores its autocomplete data in a specially-crafted, binary file (NK2). Its format is **not documented**, presumably because it is regarded as an internal data structure to the program. Still, the contents of that file are often valuable, and are definately worth keeping.

The python library of this project, [\_nk2parser.py\_](http://debunk2.googlecode.com/svn/trunk/nk2parser.py) successfully pulls out **names** and **email addresses** from the file. Here's how.

# Details #

## Contents ##

At the time of writing, the author is aware of the following resources withing the file:

  * Display name: name, or e-mail address if no name was supplied
  * Delivery Method: SMTP or Exchange
  * Address: SMTP address or MS addressing

According to [internet sources(1)](http://www.ingressor.com/about_nk2_files.htm), there's more:

  * Record type: SMTP, Exchange, Fax, or MAPIPDL (Distribution List)
  * Alias (and smtp email address or GAL reference)
  * Exchange x500 address
  * x509 PKI (Public Key Infrastructure)
  * Various other data which may be populated from the Active Directory

There is no reason to expect this to be untrue, but this program doesn't care about any of that.

# Unraveling the stuff #

1. Luckily, the most important data is also most easy to pull out. The email addresses are stored as ascii strings, so by just running _strings_ on the file, you'll get all the addresses.

2. To get the names assosciated with the addresses, you have to dig deeper.

The following is an attempt of describing what works for debunk2.

## Record separators ##

Looking at the NK2 file in an _hex viewer_ or something that can _print unprintable bytes_ so that a human can interpret it
is time-consuming, exhausting and not something that someone should have to do when there is plenty of green left in the
world. It is also the only way of examining the blasted thing.

Since there is so much green yet to be experienced, your author took some sharp turns and elbow-greased some dirty code into chopping the NK2 file into records.

Thus, debunk2 splits at the following byte strings to make sense out of the NK2 files:

```

sep1 = '\x04H\xfe\x13' # record separator
sep2 = '\x00\xdd\x01\x0fT\x02\x00\x00\x01'  # record separator

```

After the file is split at both these byte sequences, the program runs through all records. A lot of the records are
duplicates (they aren't really, but since we're only after the name and email addresses, they're redundant).

This isn't perfect, but it gets the job done.

## NUL-byte separated strings ##

**Most** record fields are separated by triple NUL-bytes (ASCII 0). Some fields are separated by single NUL bytes.

```

  split1 = [x.replace(NUL, '') for x in y.split(NUL*3)] # SPLIT1: split record into something useful by separating at triple NULs
  if split1[1] != 'SMTP': # SPLIT1 failed
    split2 = [x.replace(NUL, '') for x in y.split(NUL*1)] # SPLIT2: split again, this time using single NULs as delimiter

```


**Most** field strings are sprinkled with NUL-bytes (every second byte, actually). This is how nk2parser.py does it:

```

  def strp(self, s):
	  "Return string stripped of NUL bytes and unprintable characters"
	  return s.replace(NUL, '')#.replace('\x00', '')

```

## SMTP addresses ##

prefixed with "SMTP:"

# File location #

Little help, please?

# References #

  * (1): http://www.ingressor.com/about_nk2_files.htm
  * http://www.iwriteiam.nl/Ha_HTCABFF.html
  * http://filext.com/detaillist.php?extdetail=NK2
  * http://www.nk2.info/