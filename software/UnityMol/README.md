# UnityMol Setup

Binaries were created with Unity 2019.4.26f1 on a Windows 10 plateform.
It contains MDDriver library for communication through IMD protocol.


To use it:

- Unzip the desired archive for your architecture (Windows or Linux)
- For Windows, double-click on the executable `UnityMol_BioSpring_1.1.4.exe`
- For Linux, use the commandline:
```
tar xzvf UnityMol_BioSpring_Linux.tar.gz
cd UnityMol_BioSpring_Linux
./UnityMol_BioSpring_1.1.4
```

## Tutorial

A tutorial on how to use UnityMol is available here : https://nezix.github.io/


## BioSpring extension for UnityMol

All the features dedicated to the management of BioSPring in UnityMol are in the sub-menu *BioSpring*

- BioSpring
    - Molecular Simulation Parameters: Read and generate new MSP file for BioSpring
    - IMD Tools
        - General
            - Set working directory
            - Set screenshot directory
            - Selection k neighbors (experimental): grab n neighbors of the grabbed particle. Only when using spring networks (not with rigid body).

        - SaveToPDB : Save one of loaded structure to PDB file.
        - PDB2SPN: UI to run pdb2spn (need to be updated)
        - Run BioSpring (experimental): Run BioSpring from UnityMol using C# Process class
        - Visualization
            - Steric Grid: Show steric grid if steric interaction is enabled
            - Electrostatic Grid: Show electrostatic grid if electrostatic interaction is enabled
            - ShowGrid: deprecated
            - Add IMD representation: HyperBalls representation for IMD, select the structure before. This representation is mandatory for the following tools.
            - ShowTransferEnergy: Show IMPALA transfer energy during interactive simulation
            - ShowSASA: Show the solvent surface accessible areas. Set the framerate in the inputfield and click on the toggle.
            - Show membrane : show 3D representation of IMPALA membrane
            - ShowInsertionVector: During interactive session, just ckick on the toggle to set the vector.
            - InsertionVectorLengthScale: set size of the insertion vector
            - Membrane Scale: set size of the membrane
        - IMD forces scaling
            - HADDOCK (experimental): scaling for HADDOCK ambiguous restraint (useless for now)
            - SMD (experimental): scaling for Steered Molecular Dynamics -like, use experimental anchors tool.
            - InputForces: force scaling for direct interactive manipulation.
            - IMPALA Scaling: IMPALA force scaling factor. (may not work for now)
            - RandomShakeScaling: Used with T key is pressed during simulation
            - InsertionDepth: force insertion depth targed when user click on 2D graph
            - InsertionAngle: force insertion angle targed when user click on 2D graph
        - Analyze
            - ImmersionDepths (experimental): export individual particle depth at specific time
            - GraphSteeings: range graph scaling of some our structure studies
