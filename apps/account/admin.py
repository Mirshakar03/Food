from django.contrib import admin

from apps.account.models import Users, Card, Contact, Payment


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name')

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_filter = ('user', 'card_number', 'card_number', 'expiry_date')
    list_display = ('user', 'card_number', 'card_number', 'expiry_date')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass