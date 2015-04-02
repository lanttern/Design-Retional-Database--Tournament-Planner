import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def get_connect():
    """get connection and cursor object"""
    con = connect()
    return con, con.cursor() 
    
def dis_connect(con, cur):
    """ disconnect cursor and connection"""
    cur.close()
    con.close()
    
def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """    
    con, cur = get_connect()
    query = "INSERT INTO GameOutcomes (player_name) VALUES(%s);"
    cur.execute(query, (name,))
    con.commit()
    dis_connect(con, cur)
    
def countPlayers():
    """Returns the number of players currently registered."""
    con, cur = get_connect()
    query = "SELECT count(player_id) as num FROM GameOutcomes;"
    cur.execute(query)
    output = int(cur.fetchone()[0])
    dis_connect(con, cur)
    return output

def deletePlayers():
   """Clear out all the player records from the database."""
   con, cur = get_connect()
   query = "DELETE FROM GameOutcomes;"
   cur.execute(query)
   con.commit()
   dis_connect(con, cur)

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """    
    con, cur = get_connect()
    query_w = "UPDATE GameOutcomes SET game_matches = game_matches + 1, game_wins = game_wins + 1 WHERE player_id = {0}".format(winner)
    cur.execute(query_w)
    query_l = "UPDATE GameOutcomes SET game_matches = game_matches + 1 WHERE player_id = {0}".format(loser)
    cur.execute(query_l)
    con.commit()
    dis_connect(con, cur)
    
def deleteMatches():
    """Remove all the match records from the database."""
    con, cur = get_connect()
    query = "UPDATE GameOutcomes SET game_matches = 0, game_wins = 0;"
    cur.execute(query)
    con.commit()
    dis_connect(con, cur)

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    con, cur = get_connect()
    query = "SELECT * FROM GameOutcomes ORDER BY game_wins DESC;"
    cur.execute(query)
    output = cur.fetchall()
    dis_connect(con, cur)
    return output

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    output = []
    results = playerStandings()
    for i in range(0, len(results), 2):
        output.append((results[i][0], results[i][1], results[i+1][0], results[i+1][1]))
    return output
