from django.shortcuts import render, get_object_or_404

from .models import Group


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group.html', {'groups': groups})

def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'group_detail.html', {'group': group})
