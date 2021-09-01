class ConstantReactivity():
    '''A representation of a constant reactivity'''
    def __init__(self, reactivity):
        '''Constructs a constant reactivity profile
        self -- The instance of the constant reactivity being constructed (ConstantReactivity)
        reactivity -- The constant reactivity to be returned ($)(float)'''
        self._reactivity

    def __call__(self, time):
        ''' Returns the reactivity at a given time 
        self -- The reactivity profile the value is being returned from (ConstantReactivity)
        time -- 
        [return] -- The reactivity at the specified time'''
        return(self._reactivity)