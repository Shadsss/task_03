from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list":[
    {"restaurant_name":"Restaurant-1","food_type":"Italian"},
    {"restaurant_name":"Restaurant-2","food_type":"Indian"},
    {"restaurant_name":"Restaurant-3","food_type":"American"},
    ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":{"restaurant_name":"Restaurant-1","food_type":"Italian"},
    }
    return render(request, 'detail.html', context)
