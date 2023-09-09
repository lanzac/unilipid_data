load(filePath="UNILIPID_data/inputs/SNARE/lewitt/model.pdb", readHetm=True, forceDSSP=False, showDefaultRep=True, center=False, modelsAsTraj=True, forceStructureType=-1)
showPrimitiveMembrane()
updatePrimitiveMembraneScale(180)
select("all", "all_model", True, False, False, True, False, False, True)
setIMDRepresentation()
deleteRepresentationInSelection("model_protein_or_nucleic", "c")
showSelection("all_model", "l")
setLineSize("all_model", 0.500)
clearSelections()

setStructurePositionRotation("model", Vector3(0.0000, 0.0000, 0.0000), Vector3(0.0000, 0.0000, 0.0000))
#Save parent position
setMolParentTransform( Vector3(0.4432, 0.0839, 3.2560), Vector3(0.0254, 0.0254, 0.0254), Vector3(285.2993, 180.0006, 71.0997), Vector3(0.4550, 0.0500, 3.2709) )
