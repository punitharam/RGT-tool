from RGT.XML.SVG.basicSvgNode import BasicSvgNode

class AltGlyphDefNode(BasicSvgNode):


    def __init__(self, ownerDoc):
        BasicSvgNode.__init__(self, ownerDoc, 'altGlyphDef')
        