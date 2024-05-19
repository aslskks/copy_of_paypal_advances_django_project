# transactions/views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from transactions.forms import TransferForm
from transactions.models import Transaction
from accounts.models import UserProfile
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages

@login_required
def transfer_view(request):
    if request.method == 'POST':
        form = TransferForm(user=request.user.userprofile, data=request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.sender = request.user.userprofile
            
            # Update balances
            if transaction.sender.balance >= transaction.amount:
                transaction.sender.balance -= transaction.amount
                transaction.receiver.balance += transaction.amount
                
                transaction.sender.save()
                transaction.receiver.save()
                transaction.save()

                # Send email notifications
                send_transfer_email(transaction)

                messages.success(request, "Transfer completed successfully.")
                return redirect('success_url')  # Replace with your success URL
            else:
                messages.error(request, "Insufficient funds for the transfer.")
    else:
        form = TransferForm(user=request.user.userprofile)
    
    return render(request, 'transfer.html', {'form': form})

def send_transfer_email(transaction):
    sender_subject = "Transfer Confirmation"
    receiver_subject = "You Have Received a Transfer"
    
    sender_html_message = render_to_string('email_sender.html', {'transaction': transaction})
    sender_plain_message = strip_tags(sender_html_message)
    
    receiver_html_message = render_to_string('email_receiver.html', {'transaction': transaction})
    receiver_plain_message = strip_tags(receiver_html_message)
    
    send_mail(
        sender_subject,
        sender_plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [transaction.sender.user.email],
        html_message=sender_html_message,
    )
    
    send_mail(
        receiver_subject,
        receiver_plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [transaction.receiver.user.email],
        html_message=receiver_html_message,
    )
