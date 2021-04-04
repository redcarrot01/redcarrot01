import feedparser, datetime

velog_blog_rss_uri="https://v2.velog.io/rss/@redcarrot01"
feed = feedparser.parse(velog_blog_rss_uri)

markdown_text = """### Hi there 👋

### 🥕 About myself

I'm Yu Jin Hong and I'm interested in Backend development & Cloud.   
I'm full with eager to learn new technique and skill.   
I want to be a developer who grows day by day as much as github commits.   



### Skill Set

✔ Familiar with  
Python, c++, c, AWS, MySQL, mongondb, Crawling, Django, git

🙌 Currently learning   
Spring, Kubernetes

✨ From now on & Want to do well   
Java, Spring, Spring boot, Spring cloud ..

👌 So so & Had tried it  
Html, css, Java, javascript, linux, Docker, Tensorflow, Android



### :mailbox_with_mail: More about me & Contacts
[![Gmail Badge](https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=mailto:redccc9010@gmail.com)](mailto:redccc9010@gmail.com)   [![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://https://www.linkedin.com/in/yujin-hong-b93454193)](https://www.linkedin.com/in/yujin-hong-b93454193)   [![TechBlog Badge](https://img.shields.io/badge/Tech%20Blog-11B48A?style=flat-square&logo=Vimeo&logoColor=white&link=https://velog.io/@redcarrot01)](https://velog.io/@redcarrot01)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fredcarrot01%2Fhit-counter&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)


<!--
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=redcarrot01&layout=compact&theme=radical)](https://github.com/anuraghazra/github-readme-stats)
-->
<!--
**redcarrot01/redcarrot01** is a ✨ _special_ ✨ repository because its `README.md` (this file) ap&theme=radicalpears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

[![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=redcarrot01&theme=radical&show_icons=true)](https://github.com/anuraghazra/github-readme-stats)
### Recent blog posts
""" # list of blog posts will be appended here

lst = []


for i in feed['entries']:
    # dt = datetime.datetime.strptime(i['published'], "%a, %d %B %Y %H:%M:%S %z").strftime("%B %d, %Y")
    dt = i['published']
    markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
