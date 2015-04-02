# Design Retional Database: Tournament-Planner

### 1. Project Description: Tournament Planner
In this project, you’ll be writing a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.

### 2. Creating Your Database

1) direct to fullstack/vagrant
###### cd /fullstack/vagrant 

2) start up ubuntu
###### vagrant up

3) log in
###### vagrant ssh

4) direct to tournament folder
###### vagrant@vagrant-ubuntu-trusty-32:~$ cd /vagrant/tournament

5) run psql
###### vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ psql

6) create database
###### vagrant=> create database tournament;

7) connect database to user
###### vagrant=> \c tournament;

8) create table for tournament database
###### tournament=> \i tournament.sql;

9) if you want to delete table
###### tournament=> drop table_name;

10) if you want to delete database
###### vagrant=> drop database_name;

### 3. Functions in tournament.py

1) registerPlayer(name)
###### Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. Different players may have the same names but will receive different ID numbers.

2) countPlayers()
###### Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.

3) deletePlayers()
###### Clear out all the player records from the database.

4) reportMatch(winner, loser)
###### Stores the outcome of a single match between two players in the database.

5) deleteMatches()
###### Clear out all the match records from the database.

6) playerStandings()
###### Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

7) swissPairings()
###### Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. For instance, if there are eight registered players, this function should return four pairings. This function should use playerStandings to find the ranking of players.

### 4. Resources
[Intro to Relational Databases](https://www.udacity.com/course/viewer#!/c-ud197)

[Postgresql](http://www.postgresql.org/docs/9.4/static/sql-createdatabase.html)

[Psycopg2](http://initd.org/psycopg/docs/)

[SQL Tutorial](http://www.w3schools.com/sql/)
