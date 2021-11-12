from django.shortcuts import render
import requests
import json
import pandas as pd
# Create your views here.


def news_home(request):
    if request.method == "POST":
        topic = request.POST.get('search')
        url = "https://newsapi.org/v2/everything?q={}&from=2021-11-12&sortBy=popularity&apiKey=f5c9b9c08087455395aa2f21e9652469".format(topic)
        data = requests.get(url)
        data = data.json()
        status = data['status']
        total_results = data['totalResults']
        articles = data['articles']
        print(articles)
    else:
        home_url = "https://newsapi.org/v2/everything?q=world&from=2021-11-12&sortBy=popularity&apiKey" \
                   "=f5c9b9c08087455395aa2f21e9652469 "
        home_data = requests.get(home_url)

        home_data = home_data.json()

        status = home_data['status']
        total_results = home_data['totalResults']
        articles = home_data['articles']
        print("Status", status)
        print("Total-results", total_results)
        print("article's - source", home_data['articles'][-1]['content'])
    context = {
        "status": status,
        "total_results": total_results,
        "articles": articles
    }
    return render(request, 'home.html', context)
