# Software provided

In this repository, you will find binaries of the software needed to reproduce the results of the paper.


We used:
    - UnityMol for the visualisation part.
    - BioSpring, a Spring network simulation engine, for the simulation part.
    - MDDriver, a library designed for data communication between UnityMol and BioSpring, allowing us to perform Interactive Molecular Simulations.


## UnityMol

UnityMol is a molecular viewer and prototyping platform, coded in C# with the Unity game engine.
Source code of earlier versions are available on [GitHub](https://github.com/LBT-CNRS/UnityMol-Releases) and binaries of most recent one are available on [SourceForge](https://sourceforge.net/projects/unitymol/).
More information is available at http://unitymol.sourceforge.net/

In the UnityMol folder, you will find binaries for Linux and Windows dedicated to our IMPALA implementation.
Biospring sub-menus and various visual feedbacks (see section 2.4.3 of the paper) have been added to easily follow the simulation.

The IMD protocol is implemented natively in UnityMol and communicates directly with the MDDriver socket for simulation data exchange.

Additional information about how to use this software is available in the  `README.md` file in the UnityMol folder.


## BioSpring

BioSpring is our interactive simulation engine and uses additive energy and force terms to represent the various contributions to a given model representation.


Additional information about the dependencies, the compilation details are available in the  `README.md` file in the BioSpring folder.
