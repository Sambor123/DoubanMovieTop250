# -*- coding: UTF-8 -*-
"""
 获取时光影评电影评分排行榜
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


# 获得指定开始排行的电影url
def get_url(root_url,start):
    return root_url+"?start="+str(start)+"&filter="

def get_review(page_url):
    movies_list=[]
    response=requests.get(page_url)
    soup=BeautifulSoup(response.text,"lxml")
    soup=soup.find('ol','grid_view')
    for tag_li in soup.find_all('li'):
        dict={}
        dict['rank']=tag_li.find('em').string
        dict['name']=tag_li.find_all('span','title')[0].string
        dict['score']=tag_li.find('span','rating_num').string
        if(tag_li.find('span','inq')):
            dict['desc']=tag_li.find('span','inq').string
        movies_list.append(dict)
    return movies_list

if __name__ == "__main__":
    root_url="https://movie.douban.com/top250"
    start=0
    while(start<250):
        movies_list=get_review(get_url(root_url,start))
        for movie_dict in movies_list:
            print('电影排名：'+movie_dict['rank'])
            print('电影名称：'+movie_dict.get('name'))
            print('电影评分：'+movie_dict.get('score'))
            print('电影评词：'+movie_dict.get('desc','无评词'))
            print('------------------------------------------------------')
        start+=25


    

    