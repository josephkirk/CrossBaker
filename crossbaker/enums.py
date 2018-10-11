from enum import Enum
import re
#Enum
Import = Enum("Import", ["UseMeshName", "UseFileName"])
ImportTypes = {
    Import.UseMeshName: re.compile(r"(\w*)_(low|high)_?\w*.(obj|fbx)"),
    Import.UseFileName: re.compile(r"(\w*).(obj|fbx)\Z")
}
Padding = Enum("Padding",[
    "None", "Moderate", "Extreme"])
BakeMap = Enum("BakeMap",[
    "Normals",
    "ObjectNormals",
    "Height",
    "Position",
    "Curvature",
    "Convexity",
    "Concavity",
    "Thickness",
    "BentNormals",
    "ObjectBentNormals",
    "AO",
    "Albedo",
    "Gloss",
    "Specular",
    "Diffuse",
    "Roughness",
    "Metalness",
    "Emissive",
    "Transparency",
    "VertexColor",
    "DiffuseLighting",
    "SpecularLighting",
    "Lighting",
    "MaterialID",
    "ObjectID",
    "GroupID",
    "UVIsland",
    "Wireframe",
    "AlphaMask"])