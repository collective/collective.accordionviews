# -*- coding: utf-8 -*-

# from collective.accordionviews import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class AccordionFoldersView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('accordion_folders_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
