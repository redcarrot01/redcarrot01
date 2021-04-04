import feedparser, datetime

velog_blog_rss_uri="https://v2.velog.io/rss/@redcarrot01"
feed = feedparser.parse(velog_blog_rss_uri)

markdown_text = """# Hello, there!
Your introduction goes here
## Recent blog posts
""" # list of blog posts will be appended here

lst = []


for i in feed['entries']:
    # dt = datetime.datetime.strptime(i['published'], "%a, %d %B %Y %H:%M:%S %z").strftime("%B %d, %Y")
    dt = i['published']
    markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'],i['published'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
