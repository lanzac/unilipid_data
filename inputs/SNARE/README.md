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