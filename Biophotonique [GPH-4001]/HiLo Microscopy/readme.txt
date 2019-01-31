HiLo Image Processor v1.2
(updated Feb 25, 2011 by Daryl Lim)

Send all feedback/comments/problems to gnnbcjb+imagej@gmail.com

WHAT DO THESE PLUGINS DO?
=========================

HiLo imaging is a widefield imaging technique that produces optically sectioned images (comparable to confocal microscopy). To obtain an optically sectioned HiLo image, two raw images must first be supplied:

	1. 	Uniform image (taken with uniform illumination)
	2. 	Structured image (taken with structured illumination, eg. grid, speckle)

These plugins process these raw images into the final HiLo image. Depending on the type of structured illumination used, the appropriate plugin should be used for processing. Both plugins support image stacks.

For more information on the HiLo technique, go to: http://biomicroscopy.bu.edu/r_hilo.htm


HOW TO USE THE PLUGIN
=====================
Setup:

1.	Install/update ImageJ or Fiji (version 1.43 and newer).

2. 	Create a new folder called "HiLo" in the ImageJ plugin folder.

3. 	Copy the three files HiLo_Grid.jar, HiLo_Speckle.jar, and EtaPreviewer.jar into this HiLo folder.

4.	Restart ImageJ (if necessary).

5. 	Run HiLo Grid or HiLo speckle plugin from the Plugins drop down menu.


HiLo Grid Plugin inputs:
------------------------
1. Shot noise bias correction
	(i) Camera gain: This is needed to correct for shot noise bias correction and is defined here in units of ADU/electron, where ADU (analog-digital unit) refers to pixel value. This value should be found in the camera specs sheet or can be derived by dividing the bit-depth of the camera by the well-depth.
	(ii) Readout noise: This is also required for shot noise bias correction and should be given in units of ADU. Set to zero if value is unknown.

2.	HiLo weighting factor:
This scales the Lo image to ensure that the frequency content of the final image is balanced. This has been referred to as eta in our publications.

Currently, this is set manually by the user. If the "HiLo weighting factor preview" box is checked, the user will be able to preview the effect of choosing different values of the weighting factor on the final HiLo image and pick the appropriate one. In general, the weighting
factor should be set to a value of 1 or greater.

HiLo Speckle Plugin inputs:
---------------------------
1.	Depth of field multiplier
The depth of field can be modified with this input. The smaller this value, the smaller the depth of field of the final HiLo image. 

For more information regarding how this is achieved, please refer to:

D. Lim, T. N. Ford, K. K. Chu, and J. Mertz, "Optically sectioned in vivo imaging with speckle illumination HiLo microscopy," J. Biomed. Opt. 16, 016014 (2011)

2. Shot noise bias correction
Same as the HiLo grid plugin (see above).

3.	HiLo weighting factor
This can be set by 1 of 3 options:
	(i) Entering a value directly into "Set HiLo weighting factor"
	(ii) Picking a value based on a preview of the final HiLo image. For a stack, the preview is based on the first slice.
	(iii) Use a value automatically calculated based on the input of various optical parameters.

Option (iii) takes precedence over (ii), which takes precedence over (i).

Note: for the "Pixel size (at camera)" input, the value entered should be the real size of the pixel and should account for any binning.


SAMPLE IMAGES
=============
Two pairs of sample images are provided, one for grid illumination, and one for speckle illumination. Initial parameter settings are set for these images.

Grid HiLo sample: Fluorescein labeled tissue paper
Grid Period: 14.0, Camera Gain: 0.23, Readout noise: 1.4, HiLo weighting factor: 3.0

Speckle HiLo sample: GFP-labeled neurons in a mouse cortex slice
Camera gain: 0.15, Readout noise: 1.64, Magnification: 40, Pixel size: 22.2, Illumination wavelength: 488, Detection wavelength, 520, Illumination NA: 0.30, Detection NA: 0.40


CHANGELOG
=========
Version 1.2:
- fixed bug where Hi and Lo intermediate images show up for every frame when processing stacks
- added plugin for speckle illumination HiLo
- added in readout noise input for shot noise bias correction
- some GUI changes

Version 1.1:
- plugin is not kaput

Version 1.0:
- plugin is kaput