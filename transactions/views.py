from PIL import Image, ImageDraw, ImageFont
from django.core.files.base import ContentFile
import io
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm
from .models import Transaction
from accounts.models import BankAccount
from accounts.utils import send_transaction_email

def generate_transaction_image(sender_name, receiver_name, amount):
    # Crear una imagen en blanco
    img = Image.new('RGB', (400, 200), color='white')

    # Crear un objeto de dibujo
    draw = ImageDraw.Draw(img)

    # Especificar la fuente y el tamaño del texto
    font = ImageFont.truetype('arial.ttf', size=20)

    # Escribir el texto en la imagen
    draw.text((20, 20), f'¡Has enviado {amount} a {receiver_name}!', fill='black', font=font)
    draw.text((20, 50), f'Receptor: {receiver_name}', fill='black', font=font)
    draw.text((20, 80), f'Cantidad: ${amount}', fill='black', font=font)
    draw.text((20, 110), f'Transferido por: {sender_name}', fill='black', font=font)

    return img

@login_required
def transfer_money(request):
    if request.user.groups.filter(name='Special Users').exists():
        if request.method == 'POST':
            form = TransactionForm(request.POST, request.FILES)
            if form.is_valid():
                transaction = form.save(commit=False)
                sender_account = request.user.bankaccount
                
                if sender_account.balance >= transaction.amount:
                    receiver_account = transaction.receiver
                    
                    if sender_account == receiver_account:
                        return render(request, 'error.html', {'message': 'No puedes transferir dinero a la misma cuenta.'})
                    
                    sender_account.balance -= transaction.amount
                    receiver_account.balance += transaction.amount
                    sender_account.save()
                    receiver_account.save()
                    transaction.sender = sender_account
                    transaction.save()

                    # Enviar notificaciones por correo electrónico
                    send_transaction_email(sender_account.user.email, 'Transferencia Exitosa', f'Has transferido {transaction.amount} a la cuenta {receiver_account.account_number}.')
                    send_transaction_email(receiver_account.user.email, 'Has Recibido una Transferencia', f'Has recibido {transaction.amount} de la cuenta {sender_account.account_number}.')

                    # Generar la imagen de la transacción
                    transaction_image = generate_transaction_image(sender_account.user.username, receiver_account.user.username, transaction.amount)

                    # Convertir la imagen a formato PNG y guardarla en un campo de imagen del modelo de transacción
                    buffer = io.BytesIO()
                    transaction_image.save(buffer, format='PNG')
                    image_file = ContentFile(buffer.getvalue())
                    transaction.photo.save(f'transaction_{transaction.id}.png', image_file)

                    return redirect('success')
        else:
            form = TransactionForm()
        return render(request, 'transfer.html', {'form': form})
    else:
        return render(request, 'error.html', {'message': 'No tienes permiso para realizar esta acción.'})
