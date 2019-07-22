from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	'my_list': [
    		{"restaurant_name": "Al-Baik", "food_type": "Checken Spicy"},
    		{"restaurant_name": "Maestro Pizza", "food_type": "Vegtibales pizza"},
    		{"restaurant_name": "Al-Romansiyah", "food_type": "Kabsah ;)"},
    	],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	'my_object': {"restaurant_name": "Al-Baik", "food_type": "Checken Spicy"}
    }
    return render(request, 'detail.html', context)
