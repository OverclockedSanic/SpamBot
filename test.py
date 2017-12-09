import imp

home = os.getcwd()

class test(object):
    def __init__(self):
        self.doc = {}
        self.stats = {}
        self.setup()

    def setup(self):
        self.variables = {}

        filenames = []

        for fn in os.listdir(os.path.join(home, 'modules')):
            if fn.endswith('.py') and not fn.startswith('_'):
                filenames.append(os.path.join(home, 'modules', fn))


        modules = []

        for filename in filenames:
             name = os.path.basename(filename)[:-3]

        try:
            module = imp.load_source(name, filename)
        except Exception, e:
            print("Error loading %s: %s" % (name, e))
        else:
            self.register(vars(module))
            modules.append(name)

        if modules:
            print('Registered modules:', ', '.join(modules))

        def register(self, variables):
         for name, obj in variables.iteritems():
             if hasattr(obj, 'commands') or hasattr(obj, 'rule'):
                 self.variables[name] = obj

        def bind_commands(self):
            self.commands = {'high': {}, 'medium': {}, 'low': {}}

            def bind(self, regexp, func):
                if not hasattr(func, 'name'):
                    func.name = func.__name__
                if func.__doc__:
                    if hasattr(func, 'example'):
                        example = func.example
                    else: example = None
