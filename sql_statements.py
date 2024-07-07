staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"



staging_events_table_create= ("""
CREATE TABLE IF NOT EXISTS staging_events(
artist VARCHAR,
auth VARCHAR ,
firstName VARCHAR,
gender VARCHAR,
itemInSession VARCHAR,
lastName VARCHAR,
length VARCHAR,
level VARCHAR,
location VARCHAR,
method VARCHAR,
page VARCHAR,
registration VARCHAR,
sessionId INTEGER SORTKEY DISTKEY,
song VARCHAR,
status INTEGER,
ts BIGINT,
userAgent VARCHAR,
userId INTEGER);
""")

staging_songs_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_songs(
num_songs INTEGER,
artist_id VARCHAR SORTKEY DISTKEY,
artist_latitude VARCHAR,
artist_longtitude VARCHAR,
artist_location VARCHAR(500),
artist_name VARCHAR(500),
song_id VARCHAR ,
title VARCHAR(500) ,
duration DECIMAL(9),
year INTEGER);
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay(
songplay_id VARCHAR(50) SORTKEY,
start_time TIMESTAMP,
user_id VARCHAR(50) DISTKEY,
level VARCHAR(10),
song_id VARCHAR(50),
artist_id VARCHAR(50),
session_id VARCHAR(50),
location VARCHAR(100),
user_agent VARCHAR(300));
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
user_id INTEGER SORTKEY,
first_name VARCHAR(100),
last_name VARCHAR(100),
gender VARCHAR(10),
level VARCHAR(10)
) diststyle all;
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS song(
song_id VARCHAR(50) SORTKEY,
title VARCHAR(500) ,
artist_id VARCHAR(50),
year INTEGER,
duration DECIMAL(9)
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist(
artist_id VARCHAR(50) SORTKEY,
name VARCHAR(500) ,
location VARCHAR(500) ,
latitude DECIMAL(9) ,
longtitude DECIMAL(9) 
) diststyle all;
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
start_time TIMESTAMP SORTKEY,
hour SMALLINT ,
day SMALLINT ,
week SMALLINT ,
month SMALLINT ,
year SMALLINT ,
weekday SMALLINT 
) diststyle all;
""")












