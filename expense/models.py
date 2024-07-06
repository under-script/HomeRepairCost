from django.db import models
from django.utils import timezone


class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Possessor(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Currency(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class DollarExchangeRate(TimeStampModel):
    price = models.IntegerField(default=12600)

    def __str__(self):
        return str(self.price)


class Category(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Expense(TimeStampModel):
    possessor = models.ForeignKey(Possessor, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=1, null=True, blank=True)
    price_in_sum = models.IntegerField(null=True, blank=True)
    price_in_dollar = models.IntegerField(null=True, blank=True)
    total_in_sum = models.IntegerField(null=True, blank=True)
    total_in_dollar = models.IntegerField(null=True, blank=True)
    dollar_exchange_rate = models.ForeignKey(DollarExchangeRate, on_delete=models.SET_NULL, null=True)
    given_currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    given_time = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.possessor.name

    def set_total_other_fields(self):
        if self.amount:
            if self.price_in_sum:
                self.total_in_sum = self.price_in_sum * self.amount
            if self.price_in_dollar:
                self.total_in_dollar = self.price_in_dollar * self.amount
        if self.total_in_sum and self.amount:
            self.price_in_sum = self.total_in_sum // self.amount
        if self.total_in_dollar and self.amount:
            self.price_in_dollar = self.total_in_dollar // self.amount
        if self.total_in_sum is None and self.total_in_dollar:
            self.total_in_sum = self.total_in_dollar * self.dollar_exchange_rate.price
        if self.total_in_dollar is None and self.total_in_sum:
            self.total_in_dollar = self.total_in_sum // self.dollar_exchange_rate.price

    def save(self, *args, **kwargs):
        self.set_total_other_fields()
        super().save(*args, **kwargs)
