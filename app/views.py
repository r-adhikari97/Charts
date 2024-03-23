from django.shortcuts import render
from .models import Profile


def view_chart(request):
    labels = []
    data = []
    queryset = Profile.objects.order_by("-age")  # Order by name ascending

    for person in queryset:
        labels.append(person.name)
        data.append(person.age)

    context = {
        "labels": labels,
        "data": data
    }

    print("labels:", labels)
    print("data:", data)

    return render(request, "app/index.html", context)
