import numpy as np
import matplotlib.pyplot as plt









#1 Consider the following input continuous-time signal

# x(t) = cos(100*pi*t) + 2*cos(400*pi*t)

#a)Sample x(t) at rate fs = 800 samples/s. Determine the discrete-time signal x[n] after sampling. Does aliasing occur and if so why?

#define x(t)


#f_s is the sample rate in samples/second 
#interval is the duration of the sampling
def generate_time_axis(f_s, interval = None):
        if interval is None:
                interval = 1
        # must be an integer
        f_s = int(f_s)
        return np.linspace(0,interval,f_s,endpoint= False)

#f_x must be a numpy function
def discrete_function_time_domain(f_x,f_s, interval = None):
        t = generate_time_axis(f_s,interval)
        return f_x(t)


#default sinusoid
sinusoid = lambda t, A, f, phi: A * np.cos(2 * np.pi * f * t + phi)


# A = Amplitude
#f = frequency (of wave)
#Ph
def generate_aliases_sinusoidal(A,f,phi,f_s,interval = None):
        #time between samples T_s
        T_s = float(1/f_s)
        #angular frequency given frequency
        w = 2*np.pi*f
        #normalized radian frequency
        w_hat = float(w*T_s)

        f_n = sinusoid()
        