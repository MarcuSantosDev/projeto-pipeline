from django.shortcuts import render
import subprocess

def index(request):
    try:
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()
    except Exception:
        branch = "desconhecida"
    return render(request, "home/index.html", {"branch": branch})
