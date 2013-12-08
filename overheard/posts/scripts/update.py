from posts.models import Post

import facebook
import json
import urllib2
import datetime
import time

OVERHEARD_ID = '2709015299'
APP_ID = '182720515262516'
APP_SECRET = 'fe035c20b816d3e6f90c020bbbc3e1ef'
LIMIT = 1000

def process_query(data):
    for post in data:
        post_id = post['post_id']
        obj, created = Post.objects.get_or_create(facebook_id=post_id)
        obj.poster_id = post['actor_id']
        obj.comment_count = int(post['comment_info']['comment_count'])
        obj.date = datetime.datetime.fromtimestamp(post['created_time'])
        obj.num_likes = post['like_info']['like_count']
        obj.permalink = post['permalink']
        obj.body = post['message']
        try:
            picture_url = post['attachment']['media'][0]['src']
        except KeyError:
            obj.has_picture = False
        except IndexError:
            obj.has_picture = False
        else:
            obj.has_picture = True
            obj.picture_url = picture_url[:-5] + 'n.jpg' # change size

        obj.save()

def init_graph():
    access_token = facebook.get_app_access_token(APP_ID, APP_SECRET)
    graph = facebook.GraphAPI(access_token)
    return graph

def update_all(latest_time=None):
    ''' Updates all posts. FQL paging sucks, so I have to do it manually via 
    checking the created_time field 
    '''
    graph = init_graph()
    finished = False
    if not latest_time:
        created_time = int(time.time()) # current UNIX time
    else:
        created_time = latest_time
    while not finished:
        print "Processing query"
        query = '''SELECT post_id, permalink, message, like_info, type, actor_id, 
        comment_info, created_time,  attachment FROM stream WHERE source_id=''' + OVERHEARD_ID + ' AND created_time < ' + str(created_time) + ' LIMIT ' + str(LIMIT)
        
        data = graph.fql(query)
        if len(data) == 0:
            finished = True
        else:
            process_query(data)
            created_time = data[-1]['created_time']

def update_latest(count=100):
    ''' Updates the latest 100 posts, and also the top 100 posts'''
    graph = init_graph()
    query = '''SELECT post_id, permalink, message, like_info, type, actor_id, 
        comment_info, created_time,  attachment FROM stream WHERE source_id=''' + OVERHEARD_ID + ' LIMIT ' + str(count)

    data = graph.fql(query)
    process_query(data)

def update_top():
    graph = init_graph()
    # I have to do a big list of OR's to get this to work. 
    post_ids = Post.objects.order_by('-num_likes').exclude(body__isnull=True)[:100].values_list('facebook_id', flat=True)
    base_query = '''SELECT post_id, permalink, message, like_info, type, actor_id, comment_info, created_time,  attachment FROM stream WHERE source_id=''' + OVERHEARD_ID + ' AND '
    ids = " OR ".join(['post_id="%s"' % (pid) for pid in post_ids])
    query =  base_query + "(" + ids + ")"

    data = graph.fql(query)
    process_query(data)


def run(*script_args):
    if len(script_args) == 0:
        update_latest(100)
        update_top()
    else:
        if script_args[0] == 'all':
            update_all()
        elif script_args[0] == 'latest':
            try:
                count = int(script_args[1])
            except:
                count = 100
            update_latest(count)




