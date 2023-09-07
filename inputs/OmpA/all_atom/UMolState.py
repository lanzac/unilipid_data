load(filePath="UNILIPID_data/inputs/OmpA/all_atom/model.pdb", readHetm=True, forceDSSP=False, showDefaultRep=True, center=False, modelsAsTraj=True, forceStructureType=-1)
showPrimitiveMembrane()
updatePrimitiveMembraneScale(55)
select("all", "all_model", True, False, False, True, False, False, True)
setRepSize("all_model", "hb", 3.00)
setHyperballShrink("all_model", 1.000)
setIMDRepresentation()
deleteRepresentationInSelection("model_protein_or_nucleic", "c")
clearSelections()

setStructurePositionRotation("model", Vector3(0.0000, 0.0000, 0.0000), Vector3(0.0000, 0.0000, 0.0000))
#Save parent position
setMolParentTransform( Vector3(0.4355, -0.2465, 0.2936), Vector3(0.0254, 0.0254, 0.0254), Vector3(284.2994, 180.0004, 165.3995), Vector3(0.4400, -0.2850, 0.2909) )
