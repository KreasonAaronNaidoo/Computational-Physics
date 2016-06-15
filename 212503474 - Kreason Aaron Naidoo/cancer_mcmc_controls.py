import numpy
from matplotlib import pyplot as plt

def logchoose(n,m):
    #calculate some terms in the Poisson likelihood so that
    #you don't hit numerical overflow
    v1=numpy.arange(1,m+1)
    v2=numpy.arange(n-m+1,n+1)
    logprob=numpy.log(v2).sum()-numpy.log(v1).sum()
    return logprob

def poisson(k,n,r):
    #calculate the log of the probability of observing k events in
    #n trials, given an expected even probability of r.
    p1=numpy.log(r)*k
    p2=numpy.log(1.0-r)*(n-k)
    pp=p1+p2+logchoose(n,k)
    return pp

def cancer_prob(pp,nsamp=[90,90,90,90,90,90,90],ncancer=[0,3,3,2,0,0,3],dose=[0,1,2,4,1,2,4]):
    #given cancer incidence data and a model, calculate the log of the probability
    #of observing the given incidence data.
    tot_prob=0;
    for ii in range(len(nsamp)):
        tot_prob=tot_prob+poisson(ncancer[ii],nsamp[ii],pp[0]+pp[1]*dose[ii])
    return tot_prob

def run_chain(pp,chain_length,sigs,nsamp,ncancer,dose):
    #run a markov chain for cancer rates, given input study data
    nparam=pp.size
    chain=numpy.zeros([chain_length,nparam])

    chain[0,:]=pp
    cur_loglike=cancer_prob(pp,nsamp,ncancer,dose)

    for i in numpy.arange(1,chain_length):
        pp_trial=pp+sigs*numpy.random.randn(nparam)
        trial_loglike=cancer_prob(pp_trial,nsamp,ncancer,dose)
        prob_ratio=numpy.exp(trial_loglike-cur_loglike)
        if (prob_ratio>numpy.random.rand(1)):
            pp=pp_trial
            cur_loglike=trial_loglike
        chain[i,:]=pp
    return chain



if __name__=='__main__':
    #print 'hello'
    #delt=0.00025
    #p1=numpy.arange(delt,0.05,delt)
    #p2=numpy.arange(-0.00,0.05,delt)


    if (True):
        #glioma without old controls
        nsamp=[90,90,90,90,90,90,90]
        ncancer=[0,3,3,2,0,0,3]
        dose=[0,1,2,4,1,2,4]

    if (True):
        #glioma with old controls
        nsamp=[90,90,90,90,90,90,90,550]
        ncancer=[0,3,3,2,0,0,3,11]
        dose=[0,1,2,4,1,2,4,0]

    if (False):
        #all schwannomas in males
        nsamp=[90,90,90,90,90,90,90,699]
        ncancer=[0,2,1,5,2,3,6,9]
        dose=[0,1,2,4,1,2,4,0]

    if (False):
        #all schwannomas in males, no control
        nsamp=[90,90,90,90,90,90,90]
        ncancer=[3,3,5,7,4,4,7]
        dose=[0,1,2,4,1,2,4]


    param_guess=numpy.asarray([0.03,0.03])
    step_size=numpy.asarray([0.01,0.01])
    mychain=run_chain(param_guess,20000,step_size,nsamp,ncancer,dose)





    plt.clf()

    plt.plot(mychain[:, 0], mychain[:, 1], ".")

    ax = plt.gca()

    #ax.set_yscale("log")
   # ax.set_xscale("log")

    plt._show()

