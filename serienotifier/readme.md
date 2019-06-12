A script that sends a mail, when the first episode from a serie is being aired. It connects to a MYSQL database, 
and retrieves the imdb ID and use the omdb api (Get a api key here; http://www.omdbapi.com/) to get latest season(new season must 
be confirmed and without dates on imdb). when date is known it wil put the date in the database. It will check the date in datebase
to the date at time of running the scripts if dates are equal it will send you a mail that the first episode is aired that day. 
Put te script in a cronjob to run everyday


It's not real practical script because of the requirement of a mysql database. But I made it to learn about classes & mysql.
