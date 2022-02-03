import numpy as np
from scipy.io import savemat

if __name__== "__main__":
    a = np.zeros((11,3))
    a[0,:] = [-0.4, -0.3, 0]
    a[1,:] = [0.4, -0.3, 0]
    a[2,:] = [0.4, 0.3, 0]
    a[3,:] = [-0.4, 0.3, 0] # bottom 4 points
    a[4,:] = [-0.4, -0.4, 0]
    a[5,:] = [0.4, -0.4, 0]
    a[6,:] = [0.4, 0.4, 0]
    a[7,:] = [-0.4, 0.4, 0] # cover 4 points
    a[8,:] = [0.5, -0.5, 0.2]
    a[9,:] = [0.5, 0.5, 0.2]
    a[10,:] = [-0.5, 0.5, 0.2] # antenna tips
    mdic = {"tango3Dpoints": a}
    savemat("src/utils/tangoPoints.mat", mdic)
