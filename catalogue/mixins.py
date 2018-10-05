
class MultiRedirectMixin(object):
    """
    A mixin that supports submit-specific success redirection.
     Either specify one success_url, or provide dict with names of 
     submit actions given in template as keys
     Example: 
       In template:
         <input type="submit" name="create_new" value="Create"/>
         <input type="submit" name="delete" value="Delete"/>
       View:
         MyMultiSubmitView(MultiRedirectMixin, forms.FormView):
             success_urls = {"create_new": reverse_lazy('create'),
                               "delete": reverse_lazy('delete')}
    """
    success_urls = {}  

    def form_valid(self, form):
        """ Form is valid: Pick the url and redirect.
        """

        for name in self.success_urls:
            if name in form.data:
                self.success_url = self.success_urls[name]
                break

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        """
        Returns the supplied success URL.
        """
        if self.success_url:
            # Forcing possible reverse_lazy evaluation
            url = force_text(self.success_url)
        else:
            raise ImproperlyConfigured(
                _("No URL to redirect to. Provide a success_url."))
        return url