kayakfind
=========

A command line tool to find flights on kayak.com using their RSS

ChangeLog
========

h3. 0.0.1
* Find flights on kayak.com using their rss
* Specify departure and destination using arguments
* Accepts destionation comma separated list of aeroports
* Saves a temporary file using system function mktemp and delete the file at the end of execution
* Saves a file with your query and the best price 

 Roadmap
 =======
* Rewrite the bash script in python for cross operating system compatibility
* Uses log file to genrate a graph
* Set the currency using --curency=NZD
* A web app frontend to serach flights 