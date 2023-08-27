Consider this Django code.

class RegistrarView(LoginRequiredMixin, PrometaView):
    template_name = "registrar.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_registrar:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

Write a function that requires that the logged in user has "is_registrar" 
permissions.  Otherwise redirect to "/not_allowed".

