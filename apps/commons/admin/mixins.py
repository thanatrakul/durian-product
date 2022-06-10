from django.db.models import ForeignKey
from django.db.models import OneToOneField


class RawIdFieldAdminMixin(object):
    raw_id_fields = ()

    def __init__(self, model, admin_site, *args, **kwargs):
        self.raw_id_fields = self.setup_raw_id_fields(model)
        super().__init__(model, admin_site, *args, **kwargs)

    def setup_raw_id_fields(self, model):
        return tuple(
            f.name
            for f in model._meta.get_fields()
            if isinstance(f, ForeignKey) or isinstance(f, OneToOneField)
        )


class ControlAdmin(object):
    actions_on_top = True
    save_on_top = True

    # Display
    # list_display = ('__str__',)
    # list_display_links = ()
    # list_filter = ()
    # list_select_related = False
    # list_per_page = 100
    # list_max_show_all = 200
    # list_editable = ()
    # search_fields = ()
    # date_hierarchy = None
    # save_as = False
    # save_as_continue = True
    # save_on_top = False
    # paginator = Paginator
    # preserve_filters = True
    # inlines = []

    # Fields
    # autocomplete_fields = ()
    # raw_id_fields = ()
    # fields = None
    # exclude = None
    # fieldsets = None
    # form = forms.ModelForm
    # filter_vertical = ()
    # filter_horizontal = ()
    # radio_fields = {}
    # prepopulated_fields = {}
    # formfield_overrides = {}
    # readonly_fields = ()
    # ordering = None
    # sortable_by = None
    # view_on_site = True
    # show_full_result_count = True

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.created_user = request.user
        obj.updated_user = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            # Do something with `instance`

            if instance.pk is None:
                instance.created_user = request.user
            instance.updated_user = request.user
            instance.save()
        formset.save_m2m()
        formset.save()
