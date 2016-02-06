
![Logo](http://i.imgur.com/PTOqoh1.png)

# BedpresBro
[![Build Status](https://travis-ci.org/michaelmcmillan/BedpresBro.svg?branch=master)](https://travis-ci.org/michaelmcmillan/BedpresBro)

BedpresBro is the bro you have always wanted. It is a bot that that will notify you on Facebook when the enrollment date for for a bedpres is about to start.

### Dependencies
To get started the only requirement is that you have <code>python3</code> and <code>pip3</code> in your path. Go ahead and type both of those names in your terminal to confirm that this is the case. 

### Install
To install the libraries the project requires, type this command in the root directory. 

````bash
make install
````

### Test
If you want to confirm that the system works, type this command in the root directory.

````bash
make test
````

### Configuration
All configurations reside in the <code>config</code> file in the root directory. You must move <code>test/test_config</code> to <code>config</code>
before starting the system. Modify the settings to your needs.

````bash
mv test/test_config config
````

### Start
To start BedpresBro simply type this in the command line.

````bash
make run
````
