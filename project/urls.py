from rest_framework import routers
from .api import Client_viewset
from .api import Product_viewset
from .api import Invoice_viewset
from .api import Detail_viewset
from .api import Payments_viewset

router = routers.DefaultRouter()

router.register('api/client', Client_viewset, 'client')
router.register('api/product', Product_viewset, 'product')
router.register('api/invoice', Invoice_viewset, 'invoice')
router.register('api/detail', Detail_viewset, 'detail')
router.register('api/payments', Payments_viewset, 'payments')

urlpatterns = router.urls