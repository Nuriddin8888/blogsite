from .models import Person

def categories_processor(request):
    person = Person.objects.all()
    return {'persons': person}
