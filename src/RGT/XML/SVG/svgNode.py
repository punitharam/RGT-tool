from RGT.XML.SVG.structuralNode import StructuralNode
from RGT.XML.SVG.Attribs.conditionalProcessingAttributes import ConditionalProcessingAttributes
from RGT.XML.SVG.Attribs.documentEventAttributes import DocumentEventAttributes
from types import StringType


class SvgNode(StructuralNode, ConditionalProcessingAttributes, DocumentEventAttributes):

    ATTRIBUTE_X= 'x'
    ATTRIBUTE_Y= 'y'
    ATTRIBUTE_WIDTH= 'width'
    ATTRIBUTE_HEIGH= 'height'
    ATTRIBUTE_VIEWBOX= 'viewBox'
    ATTRIBUTE_PRESERVEASPECTRATIO= 'preserveAspectRatio'
    ATTRIBUTE_ZOOMANDPAN= 'zoomAndPan'
    ATTRIBUTE_VERSION= 'version'
    ATTRIBUTE_BASEPROFILE= 'baseProfile'
    ATTRIBUTE_CONTENTSCRIPTTYPE= 'contentScriptType'
    ATTRIBUTE_CONTENTSTYLETYPE= 'contentStyleType'


    def __init__(self, ownerDoc):
        StructuralNode.__init__(self, ownerDoc)
        ConditionalProcessingAttributes.__init__(self)
        DocumentEventAttributes.__init__(self)
    
    
    def setX(self, data):
        if data != None:
            if type(data) is not StringType:
                data= str(data)
            self._setNodeAttribute(self.ATTRIBUTE_X, data)
    
    def setY(self, data):
        if data != None:
            if type(data) is not StringType:
                data= str(data)
            self._setNodeAttribute(self.ATTRIBUTE_Y, data)
            
    def setWidth(self, data):
        if data != None:
            if type(data) is not StringType:
                data= str(data)
            self._setNodeAttribute(self.ATTRIBUTE_WIDTH, data)
            
    def setHeight(self, data):
        if data != None:
            if type(data) is not StringType:
                data= str(data)
            self._setNodeAttribute(self.ATTRIBUTE_HEIGH, data)
            
    def setViewBox(self, data):
        if data != None:
            if type(data) is not StringType:
                data= str(data)
            self._setNodeAttribute(self.ATTRIBUTE_VIEWBOX, data)
            
    
    def setPreserveAspectRatio(self, data):
        if data != None:
            if type(data) is not StringType:
                data= str(data)
            self._setNodeAttribute(self.ATTRIBUTE_PRESERVEASPECTRATIO, data)
    
    def setZoomAndPan(self, data):
        if data != None:
            if type(data) is not StringType:
                data= str(data)
            self._setNodeAttribute(self.ATTRIBUTE_ZOOMANDPAN, data)
    
    def setVersion(self, data):
        if data != None:
            if type(data) is not StringType:
                data= str(data)
            self._setNodeAttribute(self.ATTRIBUTE_VERSION, data)
            
    def setBaseProfile(self, data):
        if data != None:
            if type(data) is not StringType:
                data= str(data)
            self._setNodeAttribute(self.ATTRIBUTE_BASEPROFILE, data)
    
    def setContentScriptType(self, data):
        if data != None:
            if type(data) is not StringType:
                data= str(data)
            self._setNodeAttribute(self.ATTRIBUTE_CONTENTSCRIPTTYPE, data)
            
    def setContentStyleType(self, data):
        if data != None:
            if type(data) is not StringType:
                data= str(data)
            self._setNodeAttribute(self.ATTRIBUTE_CONTENTSTYLETYPE, data)
    
    
    def getX(self):
        node= self._getNodeAttribute(self.ATTRIBUTE_X)
        if node != None:
            return node.nodeValue
        return None
        
    def getY(self):
        node= self._getNodeAttribute(self.ATTRIBUTE_Y)
        if node != None:
            return node.nodeValue
        return None
    
    def getWidth(self):
        node= self._getNodeAttribute(self.ATTRIBUTE_WIDTH)
        if node != None:
            return node.nodeValue
        return None
    
    def getHeight(self):
        node= self._getNodeAttribute(self.ATTRIBUTE_HEIGH)
        if node != None:
            return node.nodeValue
        return None
    
    def getViewBox(self):
        node= self._getNodeAttribute(self.ATTRIBUTE_VIEWBOX)
        if node != None:
            return node.nodeValue
        return None
    
    def getPreserveAspectRatio(self):
        node= self._getNodeAttribute(self.ATTRIBUTE_PRESERVEASPECTRATIO)
        if node != None:
            return node.nodeValue
        return None
    
    def getZoomAndPan(self):
        node= self._getNodeAttribute(self.ATTRIBUTE_ZOOMANDPAN)
        if node != None:
            return node.nodeValue
        return None
    
    def getVersion(self):
        node= self._getNodeAttribute(self.ATTRIBUTE_VERSION)
        if node != None:
            return node.nodeValue
        return None
    
    def getBaseProfile(self):
        node= self._getNodeAttribute(self.ATTRIBUTE_BASEPROFILE)
        if node != None:
            return node.nodeValue
        return None
    
    def getContentScriptType(self):
        node= self._getNodeAttribute(self.ATTRIBUTE_CONTENTSCRIPTTYPE)
        if node != None:
            return node.nodeValue
        return None
    
    def getContentStyleType(self):
        node= self._getNodeAttribute(self.ATTRIBUTE_CONTENTSTYLETYPE)
        if node != None:
            return node.nodeValue
        return None