# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "diverseforest/blog@gh-pages"
}

# 站点设置
site_name = "参差森林 DiverseForest"
site_logo = "${static_prefix}logo.png"
site_build_date = "2022-01-25T10:00+08:00"
author = "jizenghui"
email = "diverseforest@outlook.com"
author_homepage = "https://www.diverseforest.press"
description = "试图以真诚的文字为途径，呼朋唤友地长出一片参差多态的小森林"
key_words = ['参差森林', 'diverseforest', 'blog', 'newsletter']
language = 'zh-CN'
external_links = [
    #{
    #    "name": "Maverick",
    #    "url": "https://github.com/AlanDecode/Maverick",
    #    "brief": "🏄‍ Go My Own Way."
    #},
    {
        "name": "Newsletter",
        "url": "https://diversity.zhubai.love",
        "brief": "参差森林"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twiter",
        "url": "https://twitter.com/diverseforest",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/diverseforest",
        "icon": "gi gi-github"
    },
    #{
    #    "name": "Weibo",
    #    "url": "https://weibo.com/5245109677/",
    #    "icon": "gi gi-weibo"
    #}
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
