from django.contrib import admin

from session.models import (
    GuidedMeditation,
    RespiratoryGraph,
    SustainedAttention,
)

admin.site.register(GuidedMeditation)
admin.site.register(RespiratoryGraph)
admin.site.register(SustainedAttention)
