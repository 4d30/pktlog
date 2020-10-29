#!/usr/pkg/bin/Rscript

#Connect to db
library("RPostgreSQL")

drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = "bge0db", host = "127.0.0.1", user = "pgsql")

#Check for connection
message("Checking for table 'iptraffic'")
tryCatch(
	dbExistsTable(con, "iptraffic"),
	warning = function(w) 
	    message(w),
	error = function(e) 
	    message(e) )


df <- dbReadTable(con, "iptraffic")
data <- as.data.frame(table(df$srcaddr))
barplot(height=table(data))
	
