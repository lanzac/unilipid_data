# UNILIPID DEPOSIT

This public repository provides the *UnityMol* and *BioSpring* software as well as interactive simulation systems and the transfer energy parameter adjustment algorithm used in the article:

Lanrezac A, Baaden M. "UNILIPID, a Methodology for Energetically Accurate Prediction of Protein Insertion into Implicit Membranes of Arbitrary Shape" Membranes (2023) DOI: [10.3390/membranes13030362](https://doi.org/10.3390/membranes13030362)


## File organization

### Inputs folder
```

├── README.md
├── inputs
│   ├── OmpA
│   │   └── all_atom
│   │       ├── model.msp
│   │       ├── model.nc
│   │       └── model.pdb
│   ├── SNARE
│   │   ├── lewitt
│   │   │   ├── model.msp
│   │   │   ├── model.nc
│   │   │   └── model.pdb
│   │   ├── martini3
│   │   │   ├── model.msp
│   │   │   ├── model.nc
│   │   │   └── model.pdb
│   │   ├── pos4ar1.dat
│   │   └── test_dynPlot.py
│   └── transfer_energies_adjustment
````

#### What's in inputs folder ?
- There are OmpA and SNARE systems that are part of the paper experiments.
- In each system folder there is a subfolder for the representation used, such as __All-atom__, or coarse grain such as __lewitt__ or __martini3__
- For each experiment (sub-defined here by the representation used), there is a simulation parameter file (__msp__ file) and two structure files, one of which is in binary format (__nc__ file) and the other in standard format (__PDB__ file).
- The __msp__ file and the __nc__ file are the inputs of *BioSpring* simulation engine.
- The __PDB__ file is the input of *UnityMol* visualization software.
- The __nc__ and __PDB__ file descibres exactly the same 3D structure.
- The __nc__ file also contains additional data to describes biophysical properties of the studied system using the NetCDF binary format:
    - __Parameters of the spring network built from from inter-particle distances__: identification numbers of pairs of linked particles, stiffness constant, equilibrium distance
    - __Particle parameters__: fixed or dynamic state, radii, mass, Steric Lennard-Jones potential energy parameter (epsilon), charge, accessible surface area, hydrophobicity, transfert energy for IMPALA model
- In the SNARE system folder, the python script __test_dynPlot.py__, which connects to *UnityMol* during the interactive SNARE simulation, retrieves the insertion depth data of the transmembrane region and displays it dynamically on a plot for comparison with the reference data available in the __pos4ar1.dat__ file.

### Software folder
```

└── software
    ├── Biospring
    │   ├── LICENSE.txt
    │   ├── biospring_binaries_MacOS
    │   │   └── install_bs_macos.zip
    │   └── biospring_binaries_Ubuntu_2004
    │       ├── biospring
    │       └── pdb2spn
    └── UnityMol
        ├── LICENSE.md
        ├── UnityMol_BioSpring_Linux.tar.gz
        ├── UnityMol_BioSpring_MacOS.zip
        └── UnityMol_BioSpring_Windows.zip

```
#### What's in software folder ?
- __BioSpring__ simulation engine which simulates the dynamics of spring networks as well as rigid bodies in our latest version. Rigid body simulation is used in particular for the OmpA system, and spring network simulation for SNARE.
- __UnityMol__ visualization software for visualization and interaction with the simulation in progress.
- __BioSpring__ is supplied for macos and Unix and __UnityMol__ for macOS, Unix and Windows.

## Get's started

OmpA video tutorial: https://youtu.be/5u2n3CKaPuY \
SNARE video tutorial: https://youtu.be/cvBHfDa5VlM

### OmpA system

#### Run UnityMol

- Extract the UnityMol archive
``` 
cd unilipid_deposit/software/UnityMol

tar -xzf UnityMol_BioSpring_[your_platform].tar.gz
# or
unzip UnityMol_BioSpring_[your_platform].zip
```
- Run UnityMol

#### Load the scene in UnityMol

- (1) Load the scene from script (fastest way)
    - __In UnityMol on the left panel__ go to `Utils/LoadScript` and open `unilipid_deposit/inputs/OmpA/all_atom/UMolState.py`

> **_NOTE (User interface):_** To see the scene more clearly, you can close the right panel (IronPython command line terminal) by clicking on the corresponding black arrow in the blue circle.

> **_NOTE (Navigation):_** Hold down the left mouse button to rotate around the scene, the middle button to translate and the right button to zoom. 

> **_NOTE (The scene script):_** You can open the script `UMolState.py` to see all the commands recorded. Note that a copy of the structure PDB files has been made in UnityMol's `ApplicationData` folder to simplify file access  with relative path.


- or (2) load the scene mannualy (as shown in `tutorial_OmpA.mov`) \
    __In UnityMol on the left panel__:
    - Load PDB file: Go to `Input/Load` and open `unilipid_deposit/inputs/OmpA/all_atom/model.pdb`
    - Go to `BioSpring/IMD Tools/Visualization` and switch on `ShowMembrane`, set the `MembraneScale` slider to approx. 55, and click on `Set IMD representation` button.

> **_NOTE (IMD Representation):_** This representation uses the *HyperBalls* representation developed in the laboratory to display particles here as large balls that are easier to catch with the mouse during interaction.

#### Run BioSpring simulation

- Switch to the terminal and run:
```
cd unilipid_deposit/software/Biospring/biospring_binaries_[your_platform]/

bs_path=$PWD

cd unilipid_deposit/inputs/OmpA/all_atom/

$bs_path/biospring --nc model.nc --msp model.nc --wait
```
- __BioSpring__ now wait for the client connection. Check the oppened port shown on the line:
```
MDDriver > Interactive MD bind to /[your machine]/[port]
```

#### Connect __UnityMol__ to __BioSpring__

- __In UnityMol on the left panel__ go to `IMD/` : 
    - Keep blank the IP input field for a default connection on the local machine (localhost)
    - Click on the input field `Port: 8888` and enter the port you saw on the BioSpring standby output.
    - Click on `Connect`

#### During the interactive simulation

> **_NOTE (User interface):_** To see the scene more clearly, you can close the bottom panel (dynamic graphs) which has just opened by clicking on the corresponding black arrow in the blue circle and open it again later to monitor the evolution of protein insertion parameters.

- __In UnityMol on the left panel__ go to `BioSpring/IMD Tools/IMD Parameters` : 
    - Set the `viscosity` to 0.001 and `IMPALAScaling` to approx. 12 and click on `SendParameters`

> **_NOTE (IMD Parameters):_** These two parameters can also be set in the msp parameter input file. Modifying these parameters in the UI and sending them will override those previously defined in the MSP file. The values are not precisely defined, but chosen empirically to observe a smooth insertion of the protein into the membrane. You can, of course, change these values as you wish.

- You can try to grab


## License

Data published under open access CC-BY license.