# DataGeneratorAndDatabaseUploader
Generates random data uploads it to a local set SQL Server.

## Background
I've worked with Python, Sql, and Power BI for a couple years professionally and I wanted to show the ease of connection between a Python script and Power BI.

## Approach to the problem
I started with needing a data set. So instead of doing the easy thing and finding one to use. I created a simple script that just creates some random data to use. Now that I had my data to use. I used a combination of Pandas and Pyodbc to read in my new data set and input in into a local SQL Server I had created. From there I just had to pull the data from the SQL Server into Power BI and that completed the data sets journey from Python to a report.

## Final solution
My final solution took two tries for this project. I changed the way I created the data set to allow some different ideas for the end result in Power BI. Using Pyodbc for the first time was very simple to allow the transfer of data from Python to SQL Server. Over all this project was simple but showed me some future potential for automation.
