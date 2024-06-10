from django.contrib import admin

from .models import *

for m in (WeddingRing, CircletRing, SealRing, Chainlet, Pendant, Necklace, Earrings, Kaf, Bracelet):
    admin.site.register(m)

for m in (Order, Feedback, Advice):
    admin.site.register(m)
