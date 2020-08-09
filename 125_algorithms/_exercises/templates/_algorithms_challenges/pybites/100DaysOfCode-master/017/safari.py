from datetime ______ datetime, timedelta
______ os
______ socket
______ ssl
______ sys
from urllib.request ______ urlopen
from xml.etree.ElementTree ______ parse

cwd = os.getcwd()
project_root = os.path.dirname(cwd)
sys.path.append(project_root)

from common.twitter_config ______ tweet_status

GO_BACK = timedelta(days=1)
NOW = datetime.now()
RSS = 'https://www.safaribooksonline.com/feeds/recently-added.rss'
LOCAL = 'MacBook' in socket.gethostname()
TWEET = 'New on @safari: {} - {}'


___ get_tweets(greps=['Python']

    doc = get_rss_feed()

    # Python cookbook 3rd ed
    for item in doc.iterfind('channel/item'
        title = item.findtext('title')
        date = item.findtext('pubDate')[:-6]
        dt = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S')
        link = item.findtext('link')
        category = item.findtext('category')

        __ (NOW - dt) > GO_BACK:
            continue

        __ not any(g.lower() in title.lower()
                   or g.lower() in category.lower()
                   for g in greps
            continue

        title = ' '.join(gen_hashtags(title, greps))
        yield TWEET.format(title, link)


___ get_rss_feed(
    __ LOCAL:
        with open('recently-added.rss') as f:
            r_ parse(f)
    ____
        # work around SSL: CERTIFICATE_VERIFY_FAILED
        context = ssl._create_unverified_context()
        u = urlopen(RSS, context=context)
        r_ parse(u)


___ gen_hashtags(title, greps
    for word in title.split(
        __ any(g.lower() __ word.lower() for g in greps
            yield '#' + word
        ____
            yield word


__ __name__ __ '__main__':

    for tweet in get_tweets(
        __ LOCAL:
            print(tweet)
        ____
            tweet_status(tweet)
