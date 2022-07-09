### What to do:


 _Make a Flask based web server, which:_
1) “repeats” the functionality of the Linux command line for processing files.
2) consists of one POST method only. The method must meet the following requirements:

- Available on the path /perform_query
- It takes 5 parameters: where 1, 2, 3, 4 - request, 5th - file name.

_Link to request examples_
- The method should look for files inside the data directory. The data folder must be in the same folder as the web server.
- Process the file following the written request and return the response to the client

Request consists following commands:
- **filter** - get lines which contains given string
- **map** - get data from the column only
- **unique** - get only unique data 
- **sort** - sort data ascending or descending
- **limit** - limit lines by given number

Requests can be realized as a json POST-request or as request parameters

_Example 1_: { "file_name": "apache_logs.txt", "cmd1": "filter", "value1": "get", "cmd2": "limit", "value2": 5 }

_Example 2_: http://127.0.0.1:5000/perform_query/?cmd1=filter&value1=GET&cmd2=limit&value2=2

