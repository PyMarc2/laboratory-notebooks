# -*- coding: utf-8 -*-
"""
This script will implement the edge-response function's curve fitting
algorithm given a csv file, plot the fitted curve, and calculate the
resulting point spread function and modulation transfer function
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from scipy.special import erf
from scipy.optimize import curve_fit, fsolve
import glob
import re
import os


def varerf(x, a, b, c, d):
    """This function returns an ERF. It is used by analyze_edge in the ERF
    fitting.
    """
    return a*erf(x*b - c) + d


def analyze_edge(file, imagevoxelsize=0.25, linelength=None, skipPlots=False):
    """This function imports the data of an edge profile from a .csv file
    created by the DeskCat software. It fits an ideal ERF on the raw data and
    then, computes the PSF and MTF. It plots all those 3 functions and saves
    them in png files whose names are derived from the original data file.

    Inputs:
        file =              file name
        imagevoxelsize =    voxelsize as set up in the parameters of the
                            reconstruction
        linelength =        the length of the line in the projection viewer if
                            the profile is taken on a 2D image

    Outputs:
        All the outputs are comprised of the x and y axis data

        orig =      Original profile data
        erf_fit =   ERF fitted on the original profile data
        psf =       PSF based on the ERF fit
        mtf =       MTF based on the PSF
    """
    #importing data and making sure that the decimal separators are "." instead of ","
    # the next 6 lines is the equivalent of ImprtData
    with open(file) as f:
        text = f.read()
    text = text.replace(",", ".")
    with open(file, "w") as f:
        f.write(text)
    data = np.genfromtxt(file, delimiter=". ", skip_header=1)
    pos = data[:,0]
    erf = data[:,1]
    # transforming the pixel number in a spatial position based on the
    # imagevoxelsize or the linelength if a linelength is provided
    if linelength:
        pos *= linelength/pos[-1]
        voxelsize = pos[1] - pos[0]
    else:
        pos *= imagevoxelsize
        voxelsize = pos[1] - pos[0]
    # normalizing the data
    erf /= np.max(erf)
    # reverting the erf vector so it goes up along the position
    if erf[int(len(erf)/4)] > erf[int(3*len(erf)/4)]:
        erf = np.flipud(erf)
    # eliminates the artefact that is present when the profile is drawn
    # outside of the phantom
    if erf[0] > 0.5:
        erf = erf[np.where(erf < 0.5)[0][0]:-1]
        pos = pos[np.where(erf < 0.5)[0]:-1]
    if max(pos) > 50:
        cutIdx = np.where(pos > 50)[0]
        if len(cutIdx) > 1:
            cutIdx = cutIdx[0]
            pos = pos[:cutIdx]
            erf = erf[:cutIdx]
    # arbitraty clipping of the profile at the beginning and at the end so
    # the ERF is centered on the x axis
    newend = int(np.where(erf > 0.6)[0][0] + 2*len(erf)/5)
    newstart = int(np.where(erf < 0.4)[0][-1] - 2*len(erf)/5)
    newerf = erf[newstart:newend]
    newpos = pos[newstart:newend]
    # Fitting the ideal ERF on the raw data
    popt, pcov = curve_fit(varerf, newpos, newerf,
                           [0.5,1,newpos[int(len(newpos)/2)],0.5])
    erf_fit = varerf(newpos, popt[0], popt[1], popt[2], popt[3])
    # Creating a spline on the ERF fit in order to get a numerical derivative
    # on the same x axis as the ERF
    erf_us = UnivariateSpline(newpos, erf_fit, k=4, s=0)
    psf = erf_us.derivative(1)(newpos)
    # Normalizing the PSF
    psf /= np.max(psf)
    # Computing the MTF from the PSF
    mtf = np.abs(np.fft.fftshift(np.fft.fft(psf)))
    mtf /= np.max(mtf)
    freq = np.fft.fftshift(np.fft.fftfreq(len(psf), d=voxelsize))

    # Outputting the plots
    if not skipPlots:
        fname = os.path.basename(file)
        # ERF plot
        plt.figure(file + " erf")
        plt.plot(pos, erf, label="mesurée", lw=1.5, color="blue")
        plt.plot(newpos, erf_fit, label="ajustée", lw=2, color="red", ls="--")
        plt.legend(loc="best", fontsize=20)
        plt.xlabel("Position $x$ [mm]", fontsize=24)
        plt.ylabel("ERF", fontsize=24)
        plt.tick_params(labelsize=20)
        plt.margins(0.05)
        plt.tight_layout()
        plt.savefig("p5outs/" + "erf_" + fname[:-4] + ".png", dpi=200)

        # PSF plot
        plt.figure(file + " psf")
        plt.plot(newpos, psf)
        plt.xlabel("Position $x$ [mm]", fontsize=24)
        plt.ylabel("PSF", fontsize=24)
        plt.tick_params(labelsize=20)
        plt.margins(0.05)
        plt.tight_layout()
        plt.savefig("p5outs/" + fname[:-4] + "_psf.png", dpi=200)

        # MTF plot
        plt.figure(file + " mtf")
        plt.plot(freq, mtf)
        plt.xlim(0, 1.2)
        plt.xlabel("Fréquence spatiale [mm$^{-1}$]", fontsize=24)
        plt.ylabel("MTF", fontsize=24)
        plt.tick_params(labelsize=20)
        plt.tight_layout()
        plt.savefig("p5outs/" + fname[:-4] + "_mtf.png", dpi=200)

    # returning the orig, erf_fit, psf, mtf
    return (newpos, newerf), (newpos, erf_fit), (newpos-np.mean(newpos)-1.8, psf), (freq, mtf)


###############################################################################
# Main
###############################################################################
# This is an example of a main script using the analyze_edge function

if __name__ == '__main__':
    # getting all the profile data files at once
    files = glob.glob("jppp/step*.csv")
    # creating lists to keep track of the data while looping through the files
    origs = list()
    erffits = list()
    psfs = list()
    mtfs = list()
    mtfs_01 = list()
    mtfs_us = list()
    # looping through the files
    for file in files:
        print(file)
        # retrieving  and setting the voxelsize in the name of the file
        # this should be adapted to your filename scheme
        voxelsize = float(re.findall("\d\.?\d*",file)[-1])
        linelength = None
        if "2d" in file:
            linelength = 39.5
            if "haut" in file:
                linelength = 36.0
            elif "bas" in file:
                linelength = 36.9
        elif "160" in file:
            voxelsize = 0.25
        elif "40" in file:
            voxelsize = 0.25
        # analyzing the data with analyze_edge
        orig, erffit, psf, mtf = analyze_edge(file, voxelsize, linelength)
        # computing the values of the spatial frequency for a MTF of 0.1
        mtf_us = UnivariateSpline(mtf[0],mtf[1]-0.1,k=3,s=0)
        mtf_01 = mtf_us.roots()[-1]
        # appending the results in the previously created
        mtfs_01.append((file,mtf_01))
        mtfs_us.append(mtf_us)
        origs.append(orig)
        erffits.append(erffit)
        psfs.append(psf)
        mtfs.append(mtf)
    # Creating plots for the lab report
    plt.figure("mtf haut bas 2d")
    plt.plot(mtfs[0][0], mtfs[0][1], label="bas", ls="-", lw=2, color="blue")
    plt.plot(mtfs[1][0], mtfs[1][1], label="haut", ls="-.", lw=2, color="red")
    plt.plot(mtfs[2][0], mtfs[2][1], label="centre", ls="--", lw=2, color="g")
    plt.legend(loc="best", fontsize=20)
    plt.tick_params(labelsize=20)
    plt.xlabel("Fréquence spatiale [mm$^{-1}$]", fontsize=24)
    plt.ylabel("MTF($f$)", fontsize=24)
    plt.xlim(0, 1.2)
    plt.tight_layout()
    plt.savefig("mtf_haut_bas_2d.png", dpi=200)

    plt.figure("erf haut bas 2d")
    plt.plot(erffits[0][0], erffits[0][1], label="bas", ls="-", lw=2, color="blue")
    plt.plot(erffits[1][0], erffits[1][1], label="haut", ls="-.", lw=2, color="red")
    plt.plot(erffits[2][0], erffits[2][1], label="centre", ls="--", lw=2, color="g")
    plt.legend(loc="best", fontsize=20)
    plt.tick_params(labelsize=20)
    plt.xlabel("Position [mm]", fontsize=24)
    plt.ylabel("ERF($x$)", fontsize=24)
    plt.margins(0.05)
    plt.tight_layout()
    plt.savefig("erf_haut_bas_2d.png", dpi=200)

    # plt.figure("mtf haut bas 3d")
    # plt.plot(mtfs[3][0], mtfs[3][1], label="bas", ls="-", lw=2, color="blue")
    # plt.plot(mtfs[4][0], mtfs[4][1], label="haut", ls="-.", lw=2, color="red")
    # plt.plot(mtfs[5][0], mtfs[5][1], label="centre", ls="--", lw=2, color="g")
    # plt.legend(loc="best", fontsize=20)
    # plt.tick_params(labelsize=20)
    # plt.xlabel("Fréquence spatiale [mm$^{-1}$]", fontsize=24)
    # plt.ylabel("MTF($f$)", fontsize=24)
    # plt.xlim(0, 1.2)
    # plt.tight_layout()
    # plt.savefig("mtf_haut_bas_3d.png", dpi=200)
    #
    # plt.figure("erf haut bas 3d")
    # plt.plot(erffits[3][0], erffits[3][1], label="bas", ls="-", lw=2, color="blue")
    # plt.plot(erffits[4][0], erffits[4][1], label="haut", ls="-.", lw=2, color="red")
    # plt.plot(erffits[5][0], erffits[5][1], label="centre", ls="--", lw=2, color="g")
    # plt.legend(loc="best", fontsize=20)
    # plt.tick_params(labelsize=20)
    # plt.xlabel("Position [mm]", fontsize=24)
    # plt.ylabel("ERF($x$)", fontsize=24)
    # plt.margins(0.05)
    # plt.tight_layout()
    # plt.savefig("erf_haut_bas_3d.png", dpi=200)

    # plt.figure("mtf 0.25 vs 0.5 vs 2")
    # plt.plot(mtfs[8][0], mtfs[8][1], label="voxels de 2mm", ls="-", lw=2, color="blue")
    # plt.plot(mtfs[6][0], mtfs[6][1], label="voxels de 0.5mm", ls="-.", lw=2, color="red")
    # plt.plot(mtfs[5][0], mtfs[5][1], label="voxels de 0.25mm", ls="--", lw=2, color="g")
    # plt.legend(loc="best", fontsize=20)
    # plt.tick_params(labelsize=20)
    # plt.xlabel("Fréquence spatiale [mm$^{-1}$]", fontsize=24)
    # plt.ylabel("MTF($f$)", fontsize=24)
    # plt.xlim(0, 1.2)
    # plt.tight_layout()
    # plt.savefig("mtf_taille_voxels_3d_edge", dpi=200)

    # plt.figure("mtf num proj edge")
    # plt.plot(mtfs[9][0], mtfs[9][1], label="40 proj.", ls="-", lw=2, color="blue")
    # plt.plot(mtfs[7][0], mtfs[7][1], label="160 proj.", ls="-.", lw=2, color="red")
    # plt.plot(mtfs[5][0], mtfs[5][1], label="320 proj.", ls="--", lw=2, color="g")
    # plt.legend(loc="best", fontsize=20)
    # plt.tick_params(labelsize=20)
    # plt.xlabel("Fréquence spatiale [mm$^{-1}$]", fontsize=24)
    # plt.ylabel("MTF($f$)", fontsize=24)
    # plt.xlim(0, 1.2)
    # plt.tight_layout()
    # plt.savefig("mtf_num_proj_edge", dpi=200)

    # plt.figure("erf num proj edge")
    # plt.plot(erffits[9][0], erffits[9][1], label="40 proj.", ls="-", lw=2, color="blue")
    # plt.plot(erffits[7][0], erffits[7][1], label="160 proj.", ls="-.", lw=2, color="red")
    # plt.plot(erffits[5][0], erffits[5][1], label="320 proj.", ls="--", lw=2, color="g")
    # plt.legend(loc="best", fontsize=20)
    # plt.tick_params(labelsize=20)
    # plt.xlabel("Position [mm]", fontsize=24)
    # plt.ylabel("ERF($x$)", fontsize=24)
    # plt.margins(0.05)
    # plt.tight_layout()
    # plt.savefig("erf_num_proj_edge", dpi=200)
