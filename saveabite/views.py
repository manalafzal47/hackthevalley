import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from .forms import userSignupForm
from .models import food_data


# doauth = OAuth()

OAuth_instance = OAuth()
OAuth_instance.register(
    name="auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
    client_metadata_discovery=True,
)

def login(request):
    redirect_uri = request.build_absolute_uri(reverse("callback"))
    return OAuth_instance.auth0.authorize_redirect(request, redirect_uri=redirect_uri)

def callback(request):
    token = OAuth_instance.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("registration_page")))

def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def index(request):
    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )

def registration_page(request):
    form = userSignupForm()
    if request.method == 'POST':
        form = userSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('market')
   
            
    return render(request, 'registration_page.html', {'form': form})


def market(request):
    market_items = food_data.objects.all()  # Fetch all items from the MarketItem model
    return render(request, 'marketplace.html', {'market': market_items})
