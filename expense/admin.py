from django.contrib import admin
from django_admin_listfilter_dropdown.filters import ChoiceDropdownFilter

from expense.models import Expense, Possessor, Currency, DollarExchangeRate, Category

# Register your models here.
class BaseAdmin(admin.ModelAdmin):
    list_per_page = 10

    class Meta:
        abstract = True


class PossessorAdmin(BaseAdmin):
    list_display = ("name",)
    list_display_links = ("name",)


class CurrencyAdmin(BaseAdmin):
    list_display = ("name",)
    list_display_links = ("name",)


class DollarExchangeRateAdmin(BaseAdmin):
    list_display = ("price",)
    list_display_links = ("price",)


class CategoryAdmin(BaseAdmin):
    list_display = ("name",)
    list_display_links = ("name",)


class ExpenseAdmin(BaseAdmin):
    list_display = ("possessor", "description", "category", "amount", "price_in_sum", "price_in_dollar", "total_in_sum", "total_in_dollar", "dollar_exchange_rate", "given_currency", "created", "updated", "given_time")
    list_display_links = ("possessor", "description", "category", "amount", "price_in_sum", "price_in_dollar", "total_in_sum", "total_in_dollar", "dollar_exchange_rate", "given_currency", "created", "updated", "given_time")


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Possessor, PossessorAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(DollarExchangeRate, DollarExchangeRateAdmin)
admin.site.register(Category, CategoryAdmin)
