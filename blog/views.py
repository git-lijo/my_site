from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Lijo",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's Nothing like the views you get hiking in the mountains!",
        "content": '''
        lorem ipsum dolor sit amet, con

        lorem ipsum dolor sit amet, con
        
        lorem ipsum dolor sit amet, con
        
        lorem ipsum dolor sit amet, con'''
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.png",
        "author": "Lijo",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching for that error?",
        "content": '''
        lorem ipsum dolor sit amet, con

        lorem ipsum dolor sit amet, con
        
        lorem ipsum dolor sit amet, con
        
        lorem ipsum dolor sit amet, con'''
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpeg",
        "author": "Lijo",
        "date": date(2021, 10, 10),
        "title": "Nature At Its Best!",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking",
        "content": '''
        lorem ipsum dolor sit amet, con

        lorem ipsum dolor sit amet, con
        
        lorem ipsum dolor sit amet, con
        
        lorem ipsum dolor sit amet, con'''
    },

]
# Create your views here.


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts,
    })


def posts(request):
    return render(request, "blog/all-posts.html",{
      "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug']== slug)
    return render(request, "blog/post-detail.html",{
      "post":identified_post
    })
