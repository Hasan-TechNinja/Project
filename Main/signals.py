# main_app/signals.py
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import SpecialOffer, Product
from decimal import Decimal
from django.utils import timezone

@receiver(post_save, sender=SpecialOffer)
@receiver(m2m_changed, sender=SpecialOffer.products.through)
def update_special_offer_price(sender, instance, **kwargs):
    """
    Update the `SpecialOffer_price` field in each associated product when a SpecialOffer is saved or modified.
    """
    if instance.is_active():
        for product in instance.products.all():
            # Calculate discounted price
            discount_factor = Decimal(instance.discount_percentage) / Decimal(100)
            special_offer_price = product.selling_price * (1 - discount_factor)
            # Update product's SpecialOffer_price
            product.SpecialOffer_price = special_offer_price
            product.save()
    else:
        # If the offer is inactive, reset the `SpecialOffer_price` to zero or another default
        for product in instance.products.all():
            product.SpecialOffer_price = 0
            product.save()
