from instabot import Bot

bot = Bot()
bot.login(username = '' , password = '') # Give the detsils about Users name and password.
bot.follow('')  # which account you want you follow add in it .
bot.unfollow('')  #  which account you want you unfollow add in it .
bot.send_message('',[''])  #1  add message in fist  gape   . #2 add account or ID which you want to send  messages .
bot.upload_photo('' , caption = '')  # Fill th blank using the path of your .jpg image  like :- D:/Milan/Hello/MyPython.jpg
                                        # add caption  which you want ex:- I Love Python.

followers = bot.get_user_followers('')  # add users name here  "  To get all followers list ."
for follower in followers:
    print(bot.get_user_info(follower))

followings = bot.get_user_following('')   # add users name here  "  To get all followings list ."
for following in followings:
    print(bot.get_user_info(following))
