#
# Database access functions for the web forum.
# 


import psycopg2
## Database connection

## Get posts from database.
def GetAllPosts():
    DB = psycopg2.connect("dbname = forum")
    cur = DB.cursor()
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    cur.execute("select time, content from posts order by time desc;")
    posts = ({'content': str(row[1]), 'time': str(row[0])} for row in cur.fetchall())
    DB.close()    
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    DB = psycopg2.connect("dbname = forum")
    cur = DB.cursor()
    #t = time.strftime('%c', time.localtime())
    cur.execute("insert into posts(content) values(%s)", (content,))
    cur.execute("update posts set content = 'cheese' where content like '%Spam%';")
    DB.commit()
    DB.close()
