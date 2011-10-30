Prerequisites
=============

* ImageMagick (tested with version 6.7.1-1 2011-10-30)
* Python (tested with version 2.7.2)

To install ImageMagick: 

	$ sudo apt-get install imagemagick # on Ubuntu
	$ brew install imagemagick         # on Mac Os X

Usage
=====

	$ python cbz2pdf file.cbz
	$ # will output to file.pdf

Troubleshooting
===============

If you get `zipfile.BadZipfile: File is not a zip file`, make sure the `.cbz` file is indeed a zip archive:

	$ file FILENAME.cbz

If it's a RAR file, there is an additional `rar2zip` script to convert RAR to ZIP. Make sure you have `unrar` installed (`brew install unrar`).