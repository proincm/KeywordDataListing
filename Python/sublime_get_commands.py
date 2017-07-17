import sublime_plugin
import sublime
import re, os, sys, inspect

RE  = re.compile('[A-Z]')
rpl = lambda m: '_'+m.group(0).lower()

def get_cache_dir(module):
    try:
        cache_dir = os.path.join(sublime.cache_path(), 'Command Help')
    except:
        cache_dir = os.path.join(sublime.packages_path(), '..', 'Cache', 'Command Help')

    cache_dir = os.path.join(cache_dir, module)

    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    return cache_dir


class CommandHelpCommand(sublime_plugin.WindowCommand):
    '''\
    Show Quick Panel listing all commands and some info about it.

    On select, there is opened a view with more info (from ``__doc__`` 
    strings).
    '''

    def command_doc(self, cmd, type):
        cn = cmd.__name__
        cmd_name = RE.sub(rpl, cn)
        if cmd_name.startswith('_'):
            cmd_name = cmd_name[1:]

        if cmd_name.endswith('_command'):
            cmd_name = cmd_name[:-8]

        if hasattr(cmd.run, 'func_code'):
            code = cmd.run.func_code
        else:
            code = cmd.run.__code__

        if hasattr(cmd.run, 'func_defaults'):
            defaults = cmd.run.func_defaults
        else:
            defaults = cmd.run.__defaults__

 #       import spdb ; spdb.start()

        varnames = code.co_varnames[:code.co_argcount]
        varnames = varnames[1:] # do not consider self

        if not defaults:
            defaults = []

        _defaults = [x for x in reversed(defaults)]
        _varnames = [x for x in reversed(varnames)]

        _no_defaults = _varnames[len(defaults):]

        params = [ "%s" % x for x in reversed(_no_defaults) ]

        if _varnames:
            params = [ "%s = %s" % (x, repr(y)) 
                 for x,y in reversed([y for y in zip(_varnames, _defaults)]) ]

        has_doc = False

        fn = os.path.join(get_cache_dir(cmd.__module__), "%s.rst" % cn)
        with open(fn, 'w') as fh:
            fh.write(cn+"\n")
            fh.write(len(cn)*"="+"\n\n")
            fh.write("Module:\n    %s\n\n" % cmd.__module__)
            fh.write("Type:\n    %s\n\n" % type)
            fh.write("Command:\n    %s\n" % cmd_name)
            fh.write("\n")
            fh.write("Parameter::\n\n")
            if params:
                fh.write("    "+"\n    ".join(params)+"\n\n")
            else:
                fh.write("    None\n\n")

            #try:
            doc = inspect.getdoc(cmd)
            #except:
            #    doc = Noen

            if doc:
                has_doc = True
                fh.write(
                    "Documentation\n"
                    "-------------\n"
                    "\n" + 
                    doc
                    )

            doc = inspect.getdoc(cmd.run)
            #try:
            #    doc = inspect.getdoc(cmd).splitlines()
            #except:
            #    doc = Noen
            if doc:
                if not cmd.__doc__:
                    fh.write(
                        "Documentation\n"
                        "-------------\n"
                        "\n")

                fh.write(doc)
                has_doc = True

        return [ 
            cn, 
            "Module: %s" % cmd.__module__, 
            '%s: %s' % (type, cmd_name), 
            ", ".join(params), 
            (has_doc and "more ..." or "no more doc :(") 
            ]


    def run(self):

        commands = []

        #import spdb ; spdb.start()

        for c in sublime_plugin.application_command_classes:
            commands.append(self.command_doc(c, 'Application Command'))

        for c in sublime_plugin.window_command_classes:
            commands.append(self.command_doc(c, 'Window Command'))

        for c in sublime_plugin.text_command_classes:
            commands.append(self.command_doc(c, 'Text Command'))

        def _done(index):
            if index < 0: return
            cmd = commands[index]
            cmd_name = cmd[0]
            cmd_module = cmd[1][8:]

            self.window.open_file(os.path.join(get_cache_dir(cmd_module), cmd_name+".rst"), sublime.TRANSIENT)

        show_panel(self.window, commands, _done)

def show_panel(window, options, callback=None):
    sublime.set_timeout(lambda: window.show_quick_panel(options, callback, 0), 10)
