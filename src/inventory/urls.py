from django.urls import path

from .views import ProductView, SupplierProductsView, SupplierView


urlpatterns = [
    path(
        'product',
        ProductView.as_view(),
        name='product',
    ),
    path(
        'suppliers',
        SupplierView.as_view(),
        name='suppliers',
    ),
    path(
        'supplier-products',
        SupplierProductsView.as_view(),
        name='supplier-products',
    ),
]
