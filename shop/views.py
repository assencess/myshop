from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .forms import EmailContactForm
from django.core.mail import send_mail
from django.views import View
from django.views.generic import DetailView, ListView

class ProductListView(ListView):
    model = Category
    template_name = 'shop/product/list.html'

    def get_context_data(self, **kwargs):
        # get context
        context = super(ProductListView, self).get_context_data(**kwargs)
        if not 'category_slug' in self.kwargs:
            self.kwargs['category_slug'] = None

        category = None
        categories = Category.objects.all()
        products = Product.objects.all().filter(available=True)
        if self.kwargs['category_slug']:
            category = get_object_or_404(Category,
                slug=self.kwargs['category_slug'])
            products = products.filter(category=category)

        context['category'] = category
        context['categories'] = categories
        context['products'] = products

        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product/detail.html'

    def get_context_data(self, **kwargs):
        # get context
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product = get_object_or_404(Product, id=self.kwargs['id'],
                    slug=self.kwargs['slug'],
                    available=True)
        context['product'] = product
        return context

class ContactView(View):
    form_class = EmailContactForm
    initial = {'form': form_class()}
    template_name = 'shop/contact.htmlss'
    sent = False

    def get(self, request, *args, **kwargs):
        return render(request, 'shop/contact.html',
            {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send message to client
            client_email = cd['email']
            subject = 'Support from www.localhost'
            message = '{} your messages was sent to support of {}' \
                    .format(cd['name'], 'www.localhost')
            send_mail(subject, message, 'www.localhost', [client_email])
            # send message to support of localhost
            subject = 'From client {}'.format(client_email)
            send_mail(subject, cd['comments'], client_email,
                    ['borodaa@gmail.com'])
            sent = True

        return render(request, 'shop/contact.html', {'form': form})

