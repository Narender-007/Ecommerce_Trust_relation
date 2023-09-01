from django.contrib import admin

# Register your models here.
from etrust.models import RegistrationModel, ProductModel, CommentModel, SearchHistoryModel, RatingModel, \
    TransactionModel

admin.site.register(RegistrationModel)
admin.site.register(ProductModel)
admin.site.register(CommentModel)
admin.site.register(SearchHistoryModel)
admin.site.register(RatingModel)
admin.site.register(TransactionModel)