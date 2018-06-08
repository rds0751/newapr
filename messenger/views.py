import os

from Approapp import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

from decorators import ajax_required
from messenger.models import Message

# "{% url 'send_message' %}"
@login_required
def inbox(request):
        conversations = Message.get_conversations(user=request.user)
        users_list = User.objects.filter(
            is_active=True).exclude(username=request.user).order_by('username')
        active_conversation = None
        messages = None
        if conversations:
            conversation = conversations[0]
            active_conversation = conversation['user'].username
            messages = Message.objects.filter(user=request.user,
                                              conversation=conversation['user'])
            messages.update(is_read=True)
            for conversation in conversations:
                if conversation['user'].username == active_conversation:
                    conversation['unread'] = 0

        return render(request, 'messenger/inbox.html', {
            'messages': messages,
            'conversations': conversations,
            'users_list': users_list,
            'active': active_conversation
        })



@login_required
def messages(request, username):
    if request.method=='GET':
        conversations = Message.get_conversations(user=request.user)
        users_list = User.objects.filter(
            is_active=True).exclude(username=request.user).order_by('username')
        active_conversation = username
        messages = Message.objects.filter(user=request.user,
                                          conversation__username=username)
        messages.update(is_read=True)
        for conversation in conversations:
            if conversation['user'].username == username:
                conversation['unread'] = 0

        return render(request, 'messenger/inbox.html', {
            'messages': messages,
            'conversations': conversations,
            'users_list': users_list,
            'active': active_conversation
        })
    else:
            from_user = request.user
            to_user = User.objects.get(username=username)
            message = request.POST.get('message')
            if request.POST.get("document") is None:
                save_path = os.path.join('sent_docs/', request.FILES['document'].name)
                doc = default_storage.save(save_path, request.FILES['document'])
                msg = Message.send_message(from_user, to_user, message, doc)
                conversations = Message.get_conversations(user=request.user)
                users_list = User.objects.filter(
                    is_active=True).exclude(username=request.user).order_by('username')
                active_conversation = username
                messages = Message.objects.filter(user=request.user,
                                                  conversation__username=username)
                messages.update(is_read=True)
                for conversation in conversations:
                    if conversation['user'].username == username:
                        conversation['unread'] = 0

                return render(request, 'messenger/inbox.html', {
                    'messages': messages,
                    'conversations': conversations,
                    'users_list': users_list,
                    'active': active_conversation,
                })
            else:
                doc = None
                msg = Message.send_message(from_user, to_user, message, doc)
                conversations = Message.get_conversations(user=request.user)
                users_list = User.objects.filter(
                    is_active=True).exclude(username=request.user).order_by('username')
                active_conversation = username
                messages = Message.objects.filter(user=request.user,
                                                  conversation__username=username)
                messages.update(is_read=True)
                for conversation in conversations:
                    if conversation['user'].username == username:
                        conversation['unread'] = 0

                return render(request, 'messenger/inbox.html', {
                    'messages': messages,
                    'conversations': conversations,
                    'users_list': users_list,
                    'active': active_conversation,
                })





@login_required
@ajax_required
def delete(request):
    return HttpResponse()


@login_required
@ajax_required
def send(request):
    if request.method == 'POST':
        from_user = request.user
        to_user_username = request.POST.get('to')
        to_user = User.objects.get(username=to_user_username)
        message = request.POST.get('message')
        if len(message.strip()) == 0:
            return HttpResponse()
        if from_user != to_user:
            msg = Message.send_message(from_user, to_user, message)
            return render(request, 'messenger/includes/partial_message.html',
                          {'message': msg})

        return HttpResponse()

    else:
        return HttpResponse("ho")


@login_required
@ajax_required
def receive(request):
    if request.method == 'GET':
        message_id = request.GET.get('message_id')
        message = Message.objects.get(pk=message_id)
        return render(
            request,
            'messenger/includes/partial_message.html', {'message': message})

    else:
        return HttpResponseBadRequest()


# TO DO
# Deprecated
@login_required
@ajax_required
def check(request):
    count = Message.objects.filter(user=request.user, is_read=False).count()
    return HttpResponse(count)
