class RampReactivity():
    '''A representation of a reactivity which is initially static, then changes linearly, then remains static again'''
    def __init__(self, start_time, stop_time, start_reactivity, stop_reactivity):
        '''Constructs a constant reactivity profile
        self -- The instance of the constant reactivity being constructed (ConstantReactivity)
        start_time -- The time the reactivity starts changing (s)(float)
        stop_time -- The time the reactivity starts changing (s)(float)
        start_reactivity -- The initial reactivity ($)(float)
        stop_reactivity -- The final reactivity ($)(float)'''
        
        # If the start time is after the stop time raise an exception
        if start_time > stop_time:
            raise ValueError("The start time ({}) was greater than the stop time ({}).".format(start_time, stop_time))

        self._start_time = start_time
        self._stop_time = stop_time
        self._start_reactivity = start_reactivity
        self._stop_reactivity = stop_reactivity
        self._gradient = (stop_reactivity - start_reactivity) / (stop_time - start_time)

    def __call__(self, time):
        ''' Returns the reactivity at a given time 
        self -- The reactivity profile the value is being returned from (ConstantReactivity)
        time -- 
        [return] -- The reactivity at the specified time'''
        if time < self._start_time:
            return self._start_reactivity
        elif time > self._stop_time:
            return self._stop_reactivity
        else:
            return self._start_reactivity + self._gradient * (time - self._start_time)