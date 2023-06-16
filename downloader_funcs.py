import instaloader
import datetime
import os
from dateutil.relativedelta import relativedelta
from itertools import dropwhile, takewhile

# -- DOWNLOAD ALL FROM USERNAME --
def download_all(username):
    L =  instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    for post in profile.get_posts():
        L.download_post(post, target=profile.username)

# -- DOWNLOAD LAST N POSTS FROM USERNAME --
def download_last_n(username_target, n, user="foo", contra="foo"):
    os.system('color')
    path = os.getcwd() + '/downloads/@{target}/'
    L =  instaloader.Instaloader(dirname_pattern=path)
    
    if not (user == "foo" and contra == "foo"):
        try:
            L.login(user, contra)
        except instaloader.InstaloaderException as ie:
            print(ie)
            
    profile = instaloader.Profile.from_username(L.context, username_target)
    posts = profile.get_posts()
    
    SINCE = datetime.datetime.today()
    UNTIL = SINCE - relativedelta(months=6)
    
    last_posts = []
    try:
        for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
            last_posts.append(post)
        
        amount_posts = len(last_posts)
        i = 0
        for post in last_posts:
            if(i <= n and i <= amount_posts):
                L.download_post(post, username_target)
            else:
                break
            i += 1
    except Exception:
        print('\x1b[1;37;41m' + "||||||  ERROR! ("+ Exception +")" + " [" + username_target + "] ||||||" + '\x1b[0m')
    else:
        print('\x1b[6;30;42m' + '||||||  DESCARGADO: [' + username_target + ': '+ str((n,len(last_posts))[len(last_posts) < n]) +' posts]  ||||||' + '\x1b[0m')

# -- DOWNLOAD FROM URL --
def download_from_url(url):
    path = os.getcwd() + '/downloads/@{target}/'
    L = instaloader.Instaloader(dirname_pattern=path)
    post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
    L.download_post(post, post.owner_username)