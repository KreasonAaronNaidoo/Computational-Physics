import numpy as np
from matplotlib import pyplot as plt

class data:

    def __init__(self, x, sigma, x0, amp):

        # x is an array in this case
        self.x = x.copy()
        self.y = amp*np.exp(-0.5*(x - x0)**2 / sigma**2)

    def add_noise(self, noiseamp = 1.0):

        self.noise = np.random.randn(self.y.size)*noiseamp
        self.noise = np.reshape(self.noise, self.y.shape)
        self.noiseamp = noiseamp
        self.y += self.noise


    def chisq(self, params):
        x0 = params[0]
        sigma = params[1]
        amp = params[2]

        pred = amp*np.exp(-0.5*(self.x - x0)**2 / sigma**2) #the model in a perfect world

        delta = self.y - pred

        chisq = (delta**2 / self.noiseamp**2)

        return np.sum(chisq)

def MCMC_driver(p_start, data, p_sig,  nstep = 10000,):

    p_cur = p_start.copy()
    chi_cur = data.chisq(p_cur)
    npar = len(p_start)
    samps = np.zeros([nstep,npar])
    samps[0,:] = p_start

    big_chisq = np.zeros(nstep)
    big_chisq[0] = chi_cur

    for i in range (1, nstep):

        p_trial = p_cur + p_sig*np.random.randn(npar)

        chi_trial = data.chisq(p_trial) #new random position

        delta_chi = chi_trial - chi_cur

        accept_probability = np.exp(-0.5*delta_chi)

        accept = np.random.rand < accept_probability # like using an if statment

        if(delta_chi < 0):
            accept = True


        if accept:
            p_cur = p_trial
            chi_cur = chi_trial

        samps[i,:] = p_cur
        big_chisq[i] = chi_cur

    return samps, big_chisq





if __name__ == '__main__':

    x = np.linspace(-5,5,1000)
    sigma = 2.0
    x0 = 0.0
    amp = 1.0

    mydat = data(x,sigma,x0,amp)

    mydat.add_noise()

    p_start = np.asarray([x0,sigma,amp+5])
    p_sig = np.asarray([0.01,0.1,0.1])
    samps, chisq = MCMC_driver(p_start,mydat,p_sig)

    plt. plot(chisq)

    plt.show()





