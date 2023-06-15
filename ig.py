import instaloader
import datetime

L =  instaloader.Instaloader()

# ig.login(username, password)
# page_name = input('eso: ')

# -- DOWNLOAD ALL FROM USERNAME --
def downloadAll(username):
    profile = instaloader.Profile.from_username(L.context, username)
    for post in profile.get_posts():
        L.download_post(post, target=profile.username)

downloadAll("ndalfonsin")



