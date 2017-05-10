from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Task to send e-mail notification when am order is succefully added
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order_id)
    message = 'Hy, Dear {}, \n\nYou have succefully placed an order. \
                Your order id is {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message, 'assncess@gmail.com',
                        [order.email])

    return mail_sent
