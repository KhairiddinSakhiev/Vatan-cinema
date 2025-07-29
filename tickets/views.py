from django.shortcuts import render, redirect, HttpResponse
from .models import *
from cinema.models import *


def create_order_view(request):
    users = CustomUser.objects.all()
    tickets = Ticket.objects.all()
    if request.method == "GET":
        return render(request, "create_order.html", {"users": users, "tickets": tickets})
    elif request.method == "POST":
        user_id = request.POST.get("user", False)
        payment_status = request.POST.get("payment_status", False)
        ticket_id = request.POST.get("ticket", False)
        if not user_id or not payment_status or not ticket_id:
            return HttpResponse("Error please fill all datas")
        user = CustomUser.objects.filter(id=user_id).first()
        ticket = Ticket.objects.filter(id=ticket_id).first()
        Order.objects.create(
            user=user,
            payment_status=payment_status,
            ticket=ticket
        )
        return redirect('home')




def show_list_view(request):
    if request.method == "GET":
        shows = Show.objects.all().order_by("-id")
        return render(request, "show_list.html", {"shows":shows})
    



def order_list_view(request):
    if request.method == "GET":
        orders = Order.objects.all().order_by("-id")
        return render(request, "order_list.html", {"orders":orders})
    




def ticket_list_view(request):
    if request.method == "GET":
        tickets = Ticket.objects.all().order_by("-id")
        return render(request, "ticket_list.html", {"tickets":tickets})
    