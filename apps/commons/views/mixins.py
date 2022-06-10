from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView


class ControlModelViewMinix(object):

    def form_valid(self, form):

        if form.non_field_errors():
            return super().form_invalid()

        if not self.object:
            form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user

        return super().form_valid(form)


class FormControlModelViewMixin(ControlModelViewMinix):
    pass


class CreateControlModelViewMixin(ControlModelViewMinix, CreateView):
    pass


class UpdateControlModelViewMixin(ControlModelViewMinix, UpdateView):
    pass


class DeleteControlModelViewMixin(ControlModelViewMinix, DeleteView):
    pass
