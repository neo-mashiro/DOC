# Getting Started

- https://www.sidefx.com/docs/houdini/solaris/usd.html
- https://graphics.pixar.com/usd/release/glossary.html
- https://github.com/NVIDIA-Omniverse/USD-Tutorials-And-Examples
- https://developer.nvidia.com/usd/tutorials
- https://courses.nvidia.com/courses/course-v1:DLI+S-FX-02+V1/
- https://docs.omniverse.nvidia.com/prod_usd/prod_usd/python-snippets.html
- https://remedy-entertainment.github.io/USDBook/index.html
- https://github.com/ColinKennedy/USD-Cookbook

# The Basics

- Stage
```python3
stage = Usd.Stage.CreateInMemory('temporary_layer.usda')
stage = Usd.Stage.CreateNew('new_layer.usda')
stage = Usd.Stage.Open('some_layer.usda')

stage.ExportToString()       # flatten the UsdStage and export to string
stage.Export('a_file.usdc')  # flatten the UsdStage and export to file, possibly in another file format
stage.Save()                 # won't save session layers or anonymous layers

UsdGeom.SetStageMetersPerUnit(stage, UsdGeom.LinearUnits.meters)  # set stage linear units to meters
UsdGeom.UsdGeomSetStageUpAxis(stage, UsdGeom.Tokens.z)            # set stage up axis to +Z

stage.GetRootLayer()
stage.GetRootLayer().Export('root_layer.usda')  # there is no flattening when exporting an individual layer
stage.GetSessionLayer()
stage.GetSessionLayer().ExportToString()
```

- Prim
```python3
prim = stage.DefinePrim('/foo', 'Xform')   # define a generic usd prim of type Xform
prim = stage.DefinePrim('/bar', 'Sphere')  # define a generic usd prim of type Sphere
prim = stage.DefinePrim('/foo/bar')        # typeless def
prim = stage.OverridePrim('/root/cube')    # author an override
prim = stage.CreateClassPrim("/_class_v")  # define an abstract prim to be inherited from
prim = stage.GetPrimAtPath('/root/cube')   # get generic prim from a sdf path

stage.SetDefaultPrim(prim)
stage.RemovePrim('/root/cube')
if prim.IsValid():  # check if a prim exists, return false
if prim:            # check if a prim exists, return false

sprim = UsdGeom.Xform.Define(stage, '/root')          # define a prim (schema object)
sprim = UsdGeom.Sphere.Define(stage, '/root/sphere')  # define a prim (schema object)

prim = sprim.GetPrim()           # get the underlying generic usd prim from a schema prim
prim.GetName()                   # cube
prim.GetTypeName()               # Cube
prim.GetPrimPath()               # Sdf.Path('/root/cube'), generic method of UsdObject
prim.GetPath()                   # Sdf.Path('/root/cube'), generic method of UsdObject
prim.GetPropertyNames()          # ['extent', 'proxyPrim', 'purpose', 'size', 'primvars:displayColor'...]
prim.GetAttribute('size').Get()  # 2.0

# apply API schemas on x in order to use the API functions, x can be either prim or sprim
UsdGeom.XformCommonAPI(x).SetTranslate((4, 5, 6))
UsdGeom.PrimvarsAPI(x).CreatePrimvar("foo", Sdf.ValueTypeNames.Float)
Usd.ModelAPI(x).SetKind(Kind.Tokens.component)
```

- Traversal
```python3
UsdPrimDefaultPredicate  # target all active, loaded, defined, non-abstract (LAND) prims

prim.GetChild('root')  # get direct child prim by name
prim.GetChildren()     # get all "LAND" child prims as an iterable range
prim.GetAllChildren()  # get all child prims as an iterable range

prim.GetFilteredChildren(UsdPrimDefaultPredicate)               # equivalent to `prim.GetChildren()`
prim.GetFilteredChildren(UsdPrimIsModel & ~Usd.PrimIsAbstract)  # get all non-abstract model child prims

[p for p in stage.Traverse()]     # traverse the stage in depth-first order, include LAND prims
[p for p in stage.TraverseAll()]  # also include non-LAND prims (except children of deactivated prims)

[p for p in stage.Traverse() if p.GetName() == 'foo']  # find a prim by name
[p for p in stage.Traverse() if p.IsA(UsdGeom.Mesh)]   # find all prims of type Mesh
[p for p in stage.Traverse() if UsdGeom.Sphere(p)]     # find all prims of type Sphere

it = iter(Usd.PrimRange.PreAndPostVisit(stage.GetPseudoRoot()))  # pre and post order traversal
```

- Attribute
```python3
attr = prim.CreateAttribute('weight', Sdf.ValueTypeNames.Float)
attr = prim.GetAttribute('purpose')                # get attribute from a generic prim
attr = prim.GetAttribute("primvars:displayColor")  # get attribute from a generic prim
attr = sprim.GetPurposeAttr()                      # get attribute from a schema object prim
attr = sprim.GetDisplayColorAttr()                 # get attribute from a schema object prim

if attr.IsValid():  # check if an attribute exists
if attr:            # check if an attribute exists

attr.Get()         # get attribute value, initially None, regardless of the type
attr.Get(96)       # get the value authored or interpolated at a particular time, e.g. the 96th frame
attr.Set(12.3)     # set attribute value
attr.Set(0.1, 96)  # set a time sample at a particular time, e.g. the 96th frame
```

- Layer Path
```python3
rootLayer = stage.GetRootLayer()
subLayer = Sdf.Layer.CreateNew("/path/to/sublayer.usd")
rootLayer.subLayerPaths.append(subLayer.identifier)     # append sublayers to the root layer
rootLayer.subLayerPaths.insert(3, subLayer.identifier)  # insert into the root layer's layer stack

primPath = Sdf.Path("/root/setpieces")
primPath.GetParentPath()  # Sdf.Path('/root')

primPath = Sdf.Path("/root/props")
primPath.AppendPath("table/lamp")  # Sdf.Path("/root/props/table/lamp")

primPath = Sdf.Path("/root/mesh")
primPath.AppendProperty(UsdGeom.Tokens.points)  # Sdf.Path("/root/mesh.points")
```

- Composition Arc
```python3
prim.GetReferences().AddReference('./ref_layer.usda')  # reference the default prim
prim.GetReferences().AddReference(assetPath="./model.usda", primPath="/model/sphere")

prim.GetPayloads().AddPayload('./ref_layer.usda')  # add the default prim
prim.GetPayloads().AddPayload(assetPath="./model.usda", primPath="/model/sphere")

base = stage.CreateClassPrim("/_class_foo")
prim.GetInherits().AddInherit(base.GetPath())

base = stage.GetPrimAtPath("/root/base")
prim.GetSpecializes().AddSpecialize(base.GetPath())

prim.CreateRelationship("rel").SetTargets(["/root/t1", "/root/t2"])
prim.GetRelationship("rel").AddTarget(["/root/t3"])

##########################################################

vset = prim.GetVariantSets().AddVariantSet('colorVariant')
vset = prim.GetVariantSets().GetVariantSet('colorVariant')
variants = ['c1', 'c2', 'c3']

for v in variants:
    vset.AddVariant(v)

for v in variants:
    vset.SetVariantSelection(v)
    with vset.GetVariantEditContext():
        ...  # author specs for this variant

vset.SetVariantSelection(variants[0])
vset.GetVariantSelection()
```

- Camera
```python3
camera = UsdGeom.Camera.Define(stage, Sdf.Path("/root/camera"))
camera.CreateProjectionAttr().Set(UsdGeom.Tokens.perspective)
camera.CreateFocalLengthAttr().Set(35)
camera.CreateHorizontalApertureAttr().Set(20.955)
camera.CreateVerticalApertureAttr().Set(15.2908)
camera.CreateClippingRangeAttr().Set((0.1,100000))
```

# Command Line Tools

```python3
usdcat -o scene.usdc scene.usda                         # usda -> usdc
usdcat -o scene.usda scene.usdc                         # usdc -> usda
usdcat -o scene_bin.usd --usdFormat usdc scene_txt.usd  # usd (usda) -> usd (usdc)
usdcat -o scene_txt.usd --usdFormat usda scene_bin.usd  # usd (usdc) -> usd (usda)
usddiff scene.usda scene.usdc  # diff usd files

usdcat -o output.usda --flatten asset.usd            # compose the stage
usdcat -o output.usda --layerMetadata asset.usd      # output metadata
usdcat -o output.usda --flattenLayerStack asset.usd  # flatten the root layer stack
...
```