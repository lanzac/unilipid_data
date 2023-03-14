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


# How to perform simulations (OmpA example)

Make sure both UnityMol and BioSpring are working correctly first (see README in the sub-folders).

The inputs files are available in the `inputs` folder and correspond to the system studied in the paper.

## With UnityMol and BioSpring on Linux

### BioSpring

Start the interactive simulation with the input topology (`-s` option), the config file (`-c` option), the IMD option to wait for a client (`--wait`),
the algorithm, the radii and the resolution for the freesasa part (`-a`, `--radii`, `--res`).

Freesasa options were taken from this paper (https://doi.org/10.1002/jcc.540141103).

```
[unix]$ cd inputs/OmpA
[unix]$ ../software/Biospring/biospring_binaries/biospring -s model.nc -c model.msp --wait --radii biospring -a sr --res 377
```

Biospring should parse the files and wait for a client connection for the IMD:
```
-- #_selfHydrophilicParticles: 774
-- #_interactionHydrophilicParticles: 0
-- Check center of mass, need to be equal to (0,0,0) and has value of (1.858356, -0.214325, 1.645172)
-- bary: x: -5.142622 y: 0.655240 z: -4.386541
-- mass: 18854.689453
_IMDforcescale 0.0004184 Da.A.fs-2
-- BioSpring radii values
MDDriver >      Bad filename, using stderr
MDDriver >      Interactive MD bind to /Serenity/3000
MDDriver >      Awaiting connection
```

### UnityMol

Launch UnityMol with the PDB file of the model.

```
[unix]$ ../software/UnityMol/UnityMol_BioSpring_Linux/UnityMol_BioSpring_Linux/UnityMol_BioSpring_1.1.4.x86_64 -i model.pdb
```

Once launched, in the *IMD* menu, enter "127.0.0.1" for the IP and the port given by Biospring (here from the above example 3000).
Setting only the port may works as well and connect to localhost.

#### BioSpring visual effects

Several visual effects have been added to UnityMol regarding the BioSpring/IMPALA interactive simulation.
There are available in the *BioSpring/IMD Tools/Visualization* submenu (see README of UnityMol).  

> **_NOTE:_** You will probably need to minimize the graph display panel by clicking on the small arrow on the right.

You can for example show the membrane (`ShowMembrane` tick) and adapt its scaling (`MembraneScale` slider)  

To tug atoms more easily and manipulate the protein you can click on `Set IMD representation` button above.

> **_NOTE:_** This representation is a Hyperball representation that you can then delete or hide in the `Loaded Molecules` submenu at the bottom of the panel.

You can show the atoms transfer energies by clicking on the button `ShowTransferEnergy` once (to retrieve the data from BioSpring) and then a second time to apply the corresponding colors to these energies. 
 
Display the color scale by clicking on `ShowColorBar`.

To display the insertion vector, click on `ShowInsertionVector` and adjust the length of the vector displayed on the slider just below.

Click on `Disconect` to disconnect from BioSpring and stop the process on the terminal

> **_NOTE:_** You may need to recalibrate some settings as UnityMol will prioritize and send new parameters to BioSpring. To do so, you have to go to the *IMD Parameters* tab and change in particular the IMPALA scaling, and for example the viscosity for rigid body simulation like OmpA (low viscosity at 0.0001 for example). Then click on `SendParameters`.

## With UnityMol on Windows and BioSpring on WSL

It's also possible to perform interactive simulations on Windows through the WSL feature.

### Biospring

Copy/paste the biospring binaries and the input files into WSL (take the 20.04 version) and install the dependencies (see README.md in Biospring folder)
Launch the biospring binary:
```
[WSL]$ biospring -s model.nc -c model.msp --wait --radii biospring -a sr --res 377
```

### UnityMol

Double-click on the executable, load the `model.pdb` file through the `Load` button.

To connect to the simulation, we need first to retrieve the ip adress of the wWSL:
   - launch a Windows Powershell and enter : `wsl hostname -I`
   - It will output the correct ip adress.

Enter the IP and the port (given by biospring) in the *IMD* menu.

# How to perform simulations (SNARE example)

## With UnityMol and BioSpring on Linux

### BioSpring

```
[unix]$ cd inputs/SNARE/lewitt
[unix]$ ../software/Biospring/biospring_binaries/biospring -s model.nc -c model.msp --wait --radii biospring -a sr --res 377
```

### UnityMol

Load the model as explain above or just run UnityMol and click on `Load` button.

Enter the given port and connect to BioSpring.

In *BioSpring/IMD Tools/Visualization* : 


- `Set IMD Representation`
- `ShowTransferEnegy`
- `ShowColorBar`
- `ShowMembrane`
- Use `DoubleMembraneOffset` slider and vary the offset.


#### Connect to the dynamic plotting
→ Show the interactive representation of the insertion depth. 
Still under development / improvement: 
- run `test_dynPlot.py` in *inputs/SNARE*. 

> **_NOTE:_** You will probably need to install the lxml, matplotlib and pandas libraries.

- In UnityMol go to *BioSpring/IMD Tools/Analyze* click on `TCPConnectTest`. If the procedure worked you should see the dynamic plot. (tested on UnityMol_BioSpring_MacOS)

