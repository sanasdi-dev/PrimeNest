from django.shortcuts import render
from property.models import Property, Agent
from django.core.paginator import Paginator


def home(request):

    properties = Property.objects.all()

    city = request.GET.get('city')
    property_type = request.GET.get('property_type')
    status = request.GET.get('status')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if city:
        properties = properties.filter(city__icontains=city)

    if property_type:
        properties = properties.filter(
            property_type__name__iexact=property_type
        )

    if status:
        properties = properties.filter(status=status)

    if min_price:
        properties = properties.filter(price__gte=min_price)

    if max_price:
        properties = properties.filter(price__lte=max_price)
        paginator = Paginator(properties, 6)

        page_number = request.GET.get('page')

        properties = paginator.get_page(page_number)

    context = {
        'properties': properties,
    }

    return render(request, 'home.html', context)
    id="a71kq"
def about(request):

    return render(
        request,
        "about.html"
    )



def contact(request):

    return render(
        request,
        "contact.html"
    )
    from property.models import Agent


def agents(request):

    agents = Agent.objects.all()

    context = {
        "agents": agents
    }

    return render(
        request,
        "agents.html",
        context
    )