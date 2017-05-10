
class TFImport:
    def __init__(self):
        self.real_imp = __import__
        self.injected = False

    def __call__(self, name, *args, **kwargs):
        obj = self.real_imp(name, *args, **kwargs)
        
        if name == "tensorflow" and not self.injected:
            tf = obj
            # for Session
            tf.Session.old_init = tf.Session.__init__
            def new_init(session_object, target='', graph=None, config=None):
                # print("Session.__init__")
                if not config:
                    config = tf.ConfigProto()
                    config.gpu_options.allow_growth = True
                    print("NOTE gpu_options.allow_growth enabled!")
                tf.Session.old_init(session_object, target, graph, config)
            tf.Session.__init__ = new_init
            
            # for InteractiveSession
            # NOTE REDUNDANT original InteractiveSession.__init__() generates ConfigProto if config is None
            tf.InteractiveSession.old_init = tf.InteractiveSession.__init__
            def new_init(session_object, target='', graph=None, config=None):
                # print("InteractiveSession.__init__")
                if not config:
                    config = tf.ConfigProto()
                    config.gpu_options.allow_growth = True
                    print("NOTE gpu_options.allow_growth enabled!")
                tf.InteractiveSession.old_init(session_object, target, graph, config)
            tf.InteractiveSession.__init__ = new_init

            # inject into ConfigProto
            tf.ConfigProto.old_init = tf.ConfigProto.__init__
            def new_init_CP(self, *args, **kwargs):
                # print("ConfigProto.__init__")
                tf.ConfigProto.old_init(self, *args, **kwargs)
                self.gpu_options.allow_growth = True
                print("NOTE gpu_options.allow_growth <= True")
            tf.ConfigProto.__init__ = new_init_CP

            self.injected = True
            print("NOTE __init__() wrappers for Session, InteractiveSession, ConfigProto were placed")
            
        return obj

def inject_hook():
    import builtins
    builtins.__import__ = TFImport()
    print("NOTE import hook for TensorFlow allow_growth was installed!")

