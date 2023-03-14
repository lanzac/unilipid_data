# BioSpring Setup

The folder `biospring_binaires_Ubuntu_2004` contains 2 binairies:
    - `biospring` which is the program for the simulations
    - `pdb2spn` which is a tool to create a spring network from a pdb file (see inputs folder)


## Compilation plateform

Binaries have been compiled on a Ubuntu 20.04 and work for Ubuntu >= 20.04.

## Dependencies

### Ubuntu 20.04

Biospring binary required the following libraries installed:
    - gcc suite version 9.4.0 and above with OpenMP support.
    - netcdf C libraries (libnetcdf-dev) v4.7 and above (https://downloads.unidata.ucar.edu/netcdf/)
    - netcdf C++ libraries (libnetcdf-c++4-dev) v4.3 and above (https://downloads.unidata.ucar.edu/netcdf/)
    - hdf5 libraries (libhdf5-dev) v.1.10 (https://www.hdfgroup.org/downloads/hdf5/)

All should be availabe through apt: `apt install gcc libnetcdf-dev libnetcdf-c++4-dev`

### Dependencies included

Biospring includes also the MDDriver library and the freesasa library version 2.1.2 (https://freesasa.github.io/)


### Check the installation

If all dependencies are installed correctly, you should be able to launch the `biospring` program with `./biospring -h` and see the output:
```
biospring 1.0.1-ec2e330
Support:
  MDDriver: ON
  OpenMP: ON
  OpenCL: OFF
  FreeSASA: ON

biospring spring network engine

usage: biospring [options] --nc <topology.nc> --msp <config.msp>

Option             Type                Default      Description
----------------------------------------------------------------------
  -s, --nc         Input               None         input topology (nc format)
  -c, --msp        Input               None         input configuration (msp format)

MDDriver options:
Option                  Type             Default   Description
-------------------------------------------------------------------------
  --port <portnumber>   int            3000      Listening and outcoming port for MDDriver
  --[no-]wait           bool           true      Waiting for a connection before starting the simulation
  --debug <0,1,2>       int            0         Debug level of the MDDriver simulation
  --log <path>          Output, Opt    stdout    File name for MDDriver debug messages

FreeSASA options:
Option                  Type             Default   Description
-------------------------------------------------------------------------
  -d --dynamic          bool           false     Update SASA according to -f framerate parameter.
  -f --frsasa           int            1000      FreeSASA computation framerate (each n iterations).
  -a --alg {sr, lr}     Input          sr        Use Shrake-Rupley [sr] or Lee-Richards [lr] algorithm.
  --res                 int            100/20    Resolution: Shrake-Rupley n-points or Lee-Richards n-slices.
  --pr                  double          1.4       Probe radius (A).
  --radii               Input          default   FreeSASA classifier radius:
                                                 [protor,naccess,oons,default_classifier,biospring],
                                                 or Input file classifier.
  --nt                  int            2         Number of threads to use, if FreeSASA compiled with thread-support.

  -h, --help            bool           false     displays this help and exits
  --version             bool           false     displays biospring version and exits
```

### BioSpring command example

```
biospring --nc model.nc --msp model.msp --wait --radii biospring -a sr
```

- --msp : molecular simulation parameters file
- --radii biospring: use radii taken from amber_vdW.ff file


You can set the options in the MSP file:
-> To enable spring networks interactive simulation mode:
- enablespring = true # if springs are created with the option --cutoff from the pdb2spn tool
- enableimpalasampling = false
- enablerigidbody = false

-> To enable rigid body interactive simulation mode:
- enablespring = false
- enableimpalasampling = false
- enablerigidbody = true

-> To enable rigid body automatic sampling mode:
- enablespring = false
- enableimpalasampling = true
- enablerigidbody = true

We invite you to play with the other options of the MSP and we warn that some of
them may cause instabilities. We are continuously working to fix bugs and improve our programs.
