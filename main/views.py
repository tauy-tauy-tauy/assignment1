from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    
    context = {
        'name': 'Earl Rusty cagadas',        
        'student_id': '2023-06759'       
    }
    return render(request, 'main/about.html', context)
