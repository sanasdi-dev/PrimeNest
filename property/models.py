from django.db import models


class PropertyType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Property(models.Model):

    STATUS_CHOICES = (
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    )

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    property_type = models.ForeignKey(
        PropertyType,
        on_delete=models.CASCADE
    )

    agent = models.ForeignKey(
        Agent,
        on_delete=models.CASCADE
    )

    amenities = models.ManyToManyField(
        Amenity,
        blank=True
    )

    city = models.CharField(max_length=100)

    address = models.CharField(max_length=300)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=12,
        decimal_places=0
    )

    area = models.PositiveIntegerField(
        help_text="Square meters"
    )

    bedrooms = models.PositiveIntegerField()

    bathrooms = models.PositiveIntegerField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    cover_image = models.ImageField(
        upload_to='properties/'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    @property
    def formatted_price(self):
        return "{:,.0f}".format(self.price)


    def __str__(self):
        return self.title

class PropertyImage(models.Model):

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='gallery'
    )

    image = models.ImageField(
        upload_to='property_gallery/'
    )

    def __str__(self):
        return f"{self.property.title} Image"

class VisitRequest(models.Model):

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="visit_requests"
    )

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=20
    )

    message = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.name} - {self.property.title}"