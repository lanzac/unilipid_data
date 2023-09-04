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
-
## License

Data published under open access CC-BY license.