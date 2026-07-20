from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Property, VisitRequest
from django.shortcuts import redirect
from .models import Property



def home(request):

    properties = Property.objects.all().order_by("-created_at")[:6]

    context = {
        "properties": properties,
    }

    return render(request, "home.html", context)




def property_list(request):

    properties = Property.objects.all().order_by("-created_at")


    # Filter by property type
    property_type = request.GET.get("property_type")

    if property_type:
        properties = properties.filter(
            property_type__name=property_type
        )


    # Filter by sale / rent
    status = request.GET.get("status")

    if status:
        properties = properties.filter(
            status=status
        )


    # Minimum price
    min_price = request.GET.get("min_price")

    if min_price:
        properties = properties.filter(
            price__gte=min_price
        )


    # Maximum price
    max_price = request.GET.get("max_price")

    if max_price:
        properties = properties.filter(
            price__lte=max_price
        )


    # Pagination
    paginator = Paginator(properties, 9)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)


    context = {
        "properties": page_obj,
    }


    return render(
        request,
        "property/list.html",
        context
    )







def property_detail(request, slug):

    property = get_object_or_404(
        Property,
        slug=slug
    )


    if request.method == "POST":

        VisitRequest.objects.create(

            property=property,

            name=request.POST.get("name"),

            email=request.POST.get("email"),

            phone=request.POST.get("phone"),

            message=request.POST.get("message"),

        )


    context = {

        "property": property

    }


    return render(
        request,
        "property/detail.html",
        context
    )
def contact(request):

    return render(
        request,
        "contact.html"
    )
def favorites(request):

    favorite_ids = request.session.get("favorites", [])

    properties = Property.objects.filter(
        id__in=favorite_ids
    )

    context = {

        "properties": properties

    }

    return render(
        request,
        "property/favorites.html",
        context
    )
def add_to_favorites(request, id):

    favorites = request.session.get("favorites", [])

    if id not in favorites:
        favorites.append(id)

    request.session["favorites"] = favorites

    return redirect(request.META.get("HTTP_REFERER", "property:list"))