# UPLOAD AUDIO FORM YOUTUBE

CONTENTS OF THIS FILE
---------------------

 * Requirements
 * Recommended modules
 * Installation
 * Configuration
 * Troubleshooting
 * Maintainers
 * Version

REQUIREMENTS
------------

This module requires the following modules:

 * ffmpeg
 * install requirements

It is recommended to use a Python venv.

RECOMMENDED MODULES
-------------------

 * pytube
 * ffmpeg - Install in local machine
 * certifi

INSTALLATION
------------

Execute requirements file to install dependencies and next step to create a results folder if not exist.

CONFIGURATION
-------------

TROUBLESHOOTING
---------------

* If show an error as No such file or directory: 'ffmpeg' python

    - Have to install ffmpeg library in your local OS.
    
* Could not download Youtube audio and show Scraping: SSL: CERTIFICATE_VERIFY_FAILED error for http://en.wikipedia.org
    
    - It is mandatory to install certifi package inside venv with ssl to avoid validation.
    
MAINTAINERS
-----------


VERSION
-----------
upload_audio 0.1.0