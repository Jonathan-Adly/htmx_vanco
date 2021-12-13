from django.shortcuts import render
from .forms import VancoForm, CrCLForm


def home(request):
    return render(
        request, "pages/home.html", {"form": VancoForm(), "crcl_form": CrCLForm()}
    )
