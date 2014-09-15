# -*- coding:utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from django.core.mail.backends import smtp #import EmailBackend
from django.conf import settings

RECIPIENTS = getattr(settings, "DEV_EMAIL_BACKEND_RECIPIENTS", [])
if not RECIPIENTS:
    RECIPIENTS = [mail for name, mail in settings.ADMINS]
    
# permet de faire des exceptions aux redirections
EXCEPTIONS = getattr(settings, "DEV_EMAIL_BACKEND_EXCEPTIONS", [])

# pour forcer le fail_silently
FAIL_SILENTLY = getattr(settings, "DEV_EMAIL_BACKEND_FAIL_SILENTLY", False)

class DevEmailBackend(smtp.EmailBackend):
    """ An EmailBackend that redirect ALL emails to admins and
    do not fail silently by default - very useful for testing and debugging
    """
    
    def __init__(self, *args, **kw):
        super(DevEmailBackend, self).__init__(*args, **kw)
        logger.warn("DevEmailBackend activated - email redirected to %s" % ", ".join(RECIPIENTS)) 
        if self.fail_silently and not FAIL_SILENTLY:
            self.fail_silently = False
            logger.warn("DevEmailBackend : fail_silently overridden by settings.DEV_EMAIL_BACKEND_FAIL_SILENTLY") 
        
    def _send(self, email_message):
        """A helper method that does the actual sending."""

        original_recipients = email_message.recipients()
        if not original_recipients:
            if self.fail_silently:
                logger.warn("email message has no recipients")
            else:
                raise ValueError("email message has no recipients")

        recipients = RECIPIENTS
        for mail_address in original_recipients:
            if mail_address in EXCEPTIONS and mails_address not in recipients:
                recipients.append(mail_address)
        
        try:
            self.connection.sendmail(
                email_message.from_email,
                recipients,
                email_message.message().as_string()
                )
        except:
            if not self.fail_silently:
                raise
            return False
        return True
