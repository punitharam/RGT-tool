from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from RGT.authentication.forms.ForgotPasswordForm import ForgotPasswordForm
from RGT import settings
from RGT.authentication.models import PassRecoverCode
from RGT.authentication.EmailService import EmailService
from RGT.gridMng import utility #for randomStringGenerator.....
from RGT.authentication.views.CaptchaSecuredFormViewMixin import CaptchaSecuredFormViewMixin


class ForgotPasswordView(FormView, CaptchaSecuredFormViewMixin):
    template_name = 'authentication/forgotPass.html'
    form_class = ForgotPasswordForm

    def get_form(self, form_class):
        if self.request.method in ('POST', 'PUT'):
            return ForgotPasswordForm(self.request.POST, request = self.request)

        return ForgotPasswordForm()

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.get(email=email)
        generatedCode = utility.randomStringGenerator(14)

        code = PassRecoverCode()
        code.email = email
        code.linkCode = generatedCode

        emailService = EmailService()

        if emailService.sendForgotPasswordEmail(user, code):
            code.save()
            return self.render_to_response(self.get_context_data(form=form, checkEmail = True))
        else:
            # error in sending mail
            pass

        return super(ForgotPasswordView, self).form_valid(form)