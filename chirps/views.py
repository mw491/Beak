from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Chirp
from .forms import EditChirpForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required


def view_chirp(request, username, id):
    if request.POST:
        Chirp.objects.filter(id=id).delete()
        messages.success(request, "Post successfully deleted")
        return redirect("ui-home")
    author = User.objects.get(username=username)
    chirp = Chirp.objects.get(id=id, author=author)

    return render(request, "chirps/view_chirp.html", {"chirp": chirp, "user": request.user, "title": f"{author.get_full_name()}'s Chirp"})


def edit_chirp(request, username, id):
    user = request.user  # logged in user
    author = User.objects.get(username=username)  # chirp author
    chirp = Chirp.objects.get(id=id)
    if user == author:
        if request.method == "POST":
            form = EditChirpForm(request.POST, instance=chirp)
            if form.is_valid:
                content = request.POST.get("content")
                chirp.content = content
                chirp.save()
                messages.success(
                    request, "Edited Successfully")
                return redirect("ui-home")
        else:
            form = EditChirpForm(instance=chirp)

        return render(request, "chirps/edit_chirp.html", {"form": form, "content": chirp.content, "title": "Edit Your Chirp"})
    raise PermissionDenied()


@login_required
def upvote(request, id, username):
    chirp = get_object_or_404(Chirp, id=id)
    if chirp.up_votes.filter(id=request.user.id).exists():
        chirp.up_votes.remove(request.user)
    else:
        chirp.up_votes.add(request.user)
    return redirect("ui-home")


@login_required
def downvote(request, id, username):
    chirp = get_object_or_404(Chirp, id=id)
    if chirp.down_votes.filter(id=request.user.id).exists():
        chirp.down_votes.remove(request.user)
    else:
        chirp.down_votes.add(request.user)
    return redirect("ui-home")
