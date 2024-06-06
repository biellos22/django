from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm
from django.utils import timezone


def event_list(request):
    events = Event.objects.filter(start_datetime__gte=timezone.now()).order_by('start_datetime')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user == event.creator:
        if request.method == 'POST':
            form = EventForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                return redirect('event_detail', pk=event.pk)
        else:
            form = EventForm(instance=event)
        return render(request, 'events/event_form.html', {'form': form})
    else:
        return redirect('event_list')

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user == event.creator:
        event.delete()
    return redirect('event_list')

