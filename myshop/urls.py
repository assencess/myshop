from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    url('^admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^coupons/', include('coupons.urls', namespace='coupons')),
    url(r'^rosetta/', include('rosetta.urls')),
    url('^', include('shop.urls', namespace='shop')),
)

# urlpatterns += [
#     # url(r'^admin/', admin.site.urls),
#     url(r'^cart/', include('cart.urls', namespace='cart')),
#     url(r'^orders/', include('orders.urls', namespace='orders')),
#     url(r'^coupons/', include('coupons.urls', namespace='coupons')),
#     # url(r'^', include('shop.urls', namespace='shop')),
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
