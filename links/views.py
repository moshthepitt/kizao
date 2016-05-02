from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.contrib import messages

from .models import Link
from .forms import LinkForm


class LinkUpdate(UpdateView):
    model = Link
    form_class = LinkForm
    template_name = "links/link_edit.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, _('Successfully updated.  Should be live shortly.'))
        return super(LinkAdd, self).form_valid(form)


class LinkAdd(CreateView):
    model = Link
    form_class = LinkForm
    success_url = reverse_lazy('home')
    template_name = "links/link_add.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, _('Successfully added, it should be live shortly'))
        return super(LinkAdd, self).form_valid(form)
