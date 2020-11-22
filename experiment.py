
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Import the PsychoPy libraries that you want to use
from psychopy import core, visual, gui, web


class WebWindow:
    def __init__(self, Response, Stimulus):
        self.response = Response
        self.stimulus = Stimulus

    def show_response(self):
        self.response = web.haveInternetAccess()
        return self.response

