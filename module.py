import functools

def commands(*command_list):
    def add_attribute(function):
        if not hasattr(function, "commands"):
            function.commands = []
        function.commands.extend(command_list)
        return function
    return add_attribute

def thread(value):
    def add_attribute(function):
        function.thread = value
        return function

def priority(value):
    def add_attribute(function):
        function.priority = value
        return function
    return add_attribute

def event(*event_list):
    def add_attribute(function):
        if not hasattr(function, "event"):
            function.event = []
        function.event.extend(event_list)
        return function
    return add_attribute

def rate(user=0, channel=0, server=0):
    def add_attribute(function):
        function.rate = user
        function.channel_rate = channel
        function.global_rate = server
        return function
    return add_attribute
