# pktlog

pktlog is a collection of scripts to automate the collection of network packets for storage in a SQL database.

# tcpdump.py

Opens a tcpdump(8) process, parses the output, and INSERTs the data into an SQL database.

# rpart.R

This is a script I've been using to analyze the data in the database created by tcpdump.py
