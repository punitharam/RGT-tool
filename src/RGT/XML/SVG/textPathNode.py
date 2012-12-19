from RGT.XML.SVG.baseTextNode import BaseTextNode
from RGT.XML.SVG.Attribs.xlinkAttributes import XlinkAttributes
from types import StringType

class TextPathNode(BaseTextNode, XlinkAttributes):

    ATTRIBUTE_START_OFFSET= 'startOffset'
    ATTRIBUTE_METHOD= 'method'
    ATTRIBUTE_SPACING= 'spacing'

    def __init__(self, ownerDoc):
        BaseTextNode.__init__(self, ownerDoc, 'textPath')
        XlinkAttributes.__init__(self)
    
    def setStartOffset(self, data):
        if data != None:
            if type(data) is not StringType:
                data= str(data)
            self._setNodeAttribute(self.ATTRIBUTE_START_OFFSET, data)
    
    def setMethod(self, data):
        allowedValues= ['align', 'stretch']
        
        if data != None:
            if data not in allowedValues:
                values= ''
                for value in allowedValues:
                    values+= value + ', '
                values= values[0: len(values)-2]
                raise ValueError('Value not allowed, only ' + values + 'are allowed')
            else:
                self._setNodeAttribute(self.ATTRIBUTE_METHOD, data)
    
    def setSpacing(self, data):
        allowedValues= ['auto', 'exact']
        
        if data != None:
            if data not in allowedValues:
                values= ''
                for value in allowedValues:
                    values+= value + ', '
                values= values[0: len(values)-2]
                raise ValueError('Value not allowed, only ' + values + 'are allowed')
            else:
                self._setNodeAttribute(self.ATTRIBUTE_SPACING, data)
    
    def getStartOffset(self):
        node= self._getNodeAttribute(self.ATTRIBUTE_START_OFFSET)
        if node != None:
            return node.nodeValue
        return None
        
    def getMethod(self):
        node= self._getNodeAttribute(self.ATTRIBUTE_METHOD)
        if node != None:
            return node.nodeValue
        return None
    
    def getSpacing(self):
        node= self._getNodeAttribute(self.ATTRIBUTE_SPACING)
        if node != None:
            return node.nodeValue
        return None