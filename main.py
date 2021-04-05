import feedparser, datetime

velog_blog_rss_uri="https://v2.velog.io/rss/@redcarrot01"
feed = feedparser.parse(velog_blog_rss_uri)

markdown_text = """

## Hi there! 👋


### About myself 🥕

I'm Yu Jin Hong and I'm interested in Backend development & Cloud.   
I'm full with eager to learn new technique and skill.   
I want to be a developer who grows day by day as much as github commits.   


### Skill Set 

✔ Familiar with  
Python, c++, c, AWS, MySQL, mongondb, Crawling, Django, git

🙌 Currently learning   
Spring, Kubernetes

✨ from now on & want to do well   
Java, Spring, Spring boot, Spring cloud ..

👌 So so & Had tried it  
Html, css, Java, javascript, linux, Docker, Tensorflow, Android


### About me & Contact me 

  <a href="https://velog.io/@redcarrot01"><img src="https://img.shields.io/badge/Tech%20Blog-11B48A?style=flat-square&logo=Vimeo&logoColor=white&link=https://velog.io/@redcarrot01"/></a>  <a href="https://www.linkedin.com/in/yujin-hong-b93454193"><image src="https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/yujin-hong-b93454193"/></a>  <a href="mailto:redccc9010@gmail.com"><img src="https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=viliketh1s98@naver.com"/></a> 


[![redcarrot01's GitHub stats](https://github-readme-stats.vercel.app/api?username=redcarrot01&count_private=true&show_icons=true&theme=omni)](https://github.com/anuraghazra/github-readme-stats)

<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fredcarrot01&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a>

### Recent blog posts
""" # list of blog posts will be appended here

lst = []

j=0
for i in feed['entries']:
    j+= 1
    if j >5:
        break
    else:
        # dt = datetime.datetime.strptime(i['published'], "%a, %d %B %Y %H:%M:%S %z").strftime("%B %d, %Y")
        dt = i['published']
        markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
        print(i['link'], i['title'],i['published'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
