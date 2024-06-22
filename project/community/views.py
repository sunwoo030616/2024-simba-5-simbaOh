from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Free, Move, Freecomment, Movecomment, Freetag, Movetag
# Create your views here.

def board(request):
    return render(request, 'community/board.html')

def free_board(request):
    frees = Free.objects.all()
    return render(request, 'community/free_board.html', {'frees': frees})

def move_board(request):
    moves = Move.objects.all()
    return render(request, 'community/move_board.html', {'moves': moves})

def new_free(request):
    return render(request, 'community/new_free.html')

def new_move(request):
    return render(request, 'community/new_move.html')

@login_required
def free_create(request):
    if request.method == 'POST':
        new_free = Free()
        new_free.title = request.POST.get('title', '')
        new_free.writer = request.user
        new_free.content = request.POST['content']
        new_free.pub_date = timezone.now()
        new_free.image = request.FILES.get('image')
        new_free.save()

        freewords = new_free.content.split(' ')
        freetag_list = []

        for f in freewords:
            if len(f)>0:
                if f[0] == '#':
                    freetag_list.append(f[1:])

        for t in freetag_list:
            freetag, boolean = Freetag.objects.get_or_create(freename=t)
            new_free.freetags.add(freetag.id)


        return redirect('community:free-detail', new_free.id)
    return render(request, 'community/new_free.html')

@login_required
def move_create(request):
    if request.method == 'POST':
        new_move = Move()
        new_move.title = request.POST.get('title', '')
        new_move.writer = request.user
        new_move.content = request.POST['content']
        new_move.pub_date = timezone.now()
        new_move.image = request.FILES.get('image')
        new_move.save()
        movewords = new_move.content.split(' ')
        movetag_list = []
        
        for m in movewords:
            if len(m)>0:
                if m[0] == '#':
                    movetag_list.append(m[1:])

        for a in movetag_list:
            movetag, boolean = Movetag.objects.get_or_create(movename=a)
            new_move.movetags.add(movetag.id)
        
        return redirect('community:move-detail', new_move.id)
    return render(request, 'community/new_move.html')

def free_detail(request, id):
    free = get_object_or_404(Free, pk=id)
    if request.method == 'GET':
        freecomments = Freecomment.objects.filter(free=free)
        return render(request, 'community/free_detail.html', {'free':free, 'freecomments':freecomments})

    elif request.method == 'POST':
        if 'delete_freecomment_id' in request.POST:
            freecomment_id = request.POST['delete_freecomment_id']
            freecomment = get_object_or_404(Freecomment, id=freecomment_id)
            if request.user.is_authenticated and freecomment.writer == request.user:
                freecomment.delete()
                return redirect('community:free-detail', id=id)  # 리다이렉트를 redirect 함수로 처리

        elif request.user.is_authenticated:
            new_freecomment = Freecomment()
            new_freecomment.free = free
            new_freecomment.writer = request.user
            new_freecomment.content = request.POST['content']
            new_freecomment.pub_date = timezone.now()
            new_freecomment.save()
            return redirect('community:free-detail', id=id)  # 리다이렉트를 redirect 함수로 처리

        else:
            return redirect('community:free-board')

    return render(request, 'community/free_detail.html', {'free': free, 'freecomments': freecomments})

def move_detail(request, id):
    move = get_object_or_404(Move, pk=id)
    if request.method == 'GET':
        movecomments = Movecomment.objects.filter(move=move)
        return render(request, 'community/move_detail.html', {'move':move, 'movecomments':movecomments})

    elif request.method == 'POST':
        if 'delete_movecomment_id' in request.POST:
            movecomment_id = request.POST['delete_movecomment_id']
            movecomment = get_object_or_404(Movecomment, id=movecomment_id)
            if request.user.is_authenticated and movecomment.writer == request.user:
                movecomment.delete()
                return redirect('community:move-detail', id=id)  # 리다이렉트를 redirect 함수로 처리

        elif request.user.is_authenticated:
            new_movecomment = Movecomment()
            new_movecomment.move = move
            new_movecomment.writer = request.user
            new_movecomment.content = request.POST['content']
            new_movecomment.pub_date = timezone.now()
            new_movecomment.save()
            return redirect('community:move-detail', id=id)  # 리다이렉트를 redirect 함수로 처리

        else:
            return redirect('community:move-board')

    return render(request, 'community/move_detail.html', {'move': move, 'movecomments': movecomments})

def free_edit(request, id):
    edit_free = Free.objects.get(pk=id)
    return render(request, 'community/free_edit.html', {'free' : edit_free})
def move_edit(request, id):
    edit_move = Move.objects.get(pk=id)
    return render(request, 'community/move_edit.html', {'move' : edit_move})



def free_update(request, id):
    update_free = Free.objects.get(pk=id)
    if request.user.is_authenticated and request.user == update_free.writer:

        update_free.title = request.POST['title']
        update_free.content = request.POST['content']
        update_free.pub_date = timezone.now()
        if request.FILES.get('image'):
            update_free.image = request.FILES['image']

        update_free.save()
        return redirect('community:free-detail', update_free.id)
    return render(request, 'community/free_board.html')

    

def move_update(request, id):
    update_move = Move.objects.get(pk=id)
    if request.user.is_authenticated and request.user == update_move.writer:

        update_move.title = request.POST['title']
        update_move.content = request.POST['content']
        update_move.pub_date = timezone.now()
        if request.FILES.get('image'):
            update_move.image = request.FILES['image']


        update_move.save()

        return redirect('community:move-detail', update_move.id)
    return render(request, 'community/move_board.html')

def free_delete(request, id):
    delete_free = Free.objects.get(pk=id)
    delete_free.delete()
    return redirect('community:free-board')

def move_delete(request, id):
    delete_move = Move.objects.get(pk=id)
    delete_move.delete()
    return redirect('community:move-board')

def freetag_list(request):
    freetags = Freetag.objects.all()
    return render(request, 'community/freetag-list.html', {'freetags':freetags})

def freetag_frees(request, freetag_id):
    freetag = get_object_or_404(Freetag, id=freetag_id)
    frees = freetag.frees.all()
    return render(request, 'community/freetag-free.html', {
        'freetag' : freetag,
        'frees' : frees
    })

def movetag_list(request):
    movetags = Movetag.objects.all()
    return render(request, 'community/movetag-list.html', {'movetags':movetags})

def movetag_moves(request, movetag_id):
    movetag = get_object_or_404(Movetag, id=movetag_id)
    moves = movetag.frees.all()
    return render(request, 'community/movetag-move.html', {
        'movetag' : movetag,
        'moves' : moves
    })



