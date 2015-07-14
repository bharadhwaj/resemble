StartupBox Task
===============

#Problem
Write a program which when given links to two images on the Internet, finds out how similar they are.Bonus points if it ranks images on a similarity scale from 0 - very different to 100 - exactly the same.

#Solution 1
First solution uses opencv and python. Comparison is based on histograms.

###Usage:
``` python compare.py <url1> <url2>```

###Dependencies:
- opencv
- python-opencv

Python packages:

- matplotlib
- requests

#Solution 2

Uses [resemble.js]
Implemented as a python-flask web app.
###Usage:

``` python app.py ``` starts the server at port 8000 in localhost.
Head over to http://localhost:8080 to see it in action.

###Dependencies:

Python packages:

- Flask
- requests

Authors
=======
- Ashwin Jayakumar ```<ashwinjkm94@gmail.com>```
- Bharadhwaj CN ```<bharadhwaj10@gmail.com>```
- Hanzal Salim ```<hanzalsalim94@gmail.com>```
- Shafeeq K ```<shafeeq94@gmail.com>```
- Sreya K ```<sreyakannan@gmail.com>```

[resemble.js]: https://github.com/Huddle/Resemble.js