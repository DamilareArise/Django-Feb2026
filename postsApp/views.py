from django.shortcuts import render

# Create your views here.

def homeView(request):
    
    account = {
        'name': "John Mark",
        'gender': 'Male',
        'course': 'Data science',
        'bio': "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eos, autem fugiat. Accusamus quis officiis sit ea? Quae pariatur, doloribus velit nam quas sapiente assumenda labore perferendis saepe tempora quis enim?"
    }
    
    students = ['David', 'Samuel', 'Blessing', 'Rejoice']
    
    
    return render(
        request,
        template_name="index.html",
        context={"account":account, "students": students}
    )
    

def aboutView(request):
    
    return render(
        request,
        template_name="about.html",
        context={}
    )