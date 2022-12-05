# The PEP 484 type hints stub file for the QtXml module.
#
# Generated by SIP 6.7.0
#
# Copyright (c) 2022 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt6.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import enum
import typing

import PyQt6.sip

from PyQt6 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]


class QDomImplementation(PyQt6.sip.simplewrapper):

    class InvalidDataPolicy(enum.Enum):
        AcceptInvalidChars = ... # type: QDomImplementation.InvalidDataPolicy
        DropInvalidChars = ... # type: QDomImplementation.InvalidDataPolicy
        ReturnNullNode = ... # type: QDomImplementation.InvalidDataPolicy

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDomImplementation') -> None: ...

    def isNull(self) -> bool: ...
    @staticmethod
    def setInvalidDataPolicy(policy: 'QDomImplementation.InvalidDataPolicy') -> None: ...
    @staticmethod
    def invalidDataPolicy() -> 'QDomImplementation.InvalidDataPolicy': ...
    def createDocument(self, nsURI: str, qName: str, doctype: 'QDomDocumentType') -> 'QDomDocument': ...
    def createDocumentType(self, qName: str, publicId: str, systemId: str) -> 'QDomDocumentType': ...
    def hasFeature(self, feature: str, version: str) -> bool: ...
    def __ne__(self, other: object): ...
    def __eq__(self, other: object): ...


class QDomNode(PyQt6.sip.simplewrapper):

    class EncodingPolicy(enum.Enum):
        EncodingFromDocument = ... # type: QDomNode.EncodingPolicy
        EncodingFromTextStream = ... # type: QDomNode.EncodingPolicy

    class NodeType(enum.Enum):
        ElementNode = ... # type: QDomNode.NodeType
        AttributeNode = ... # type: QDomNode.NodeType
        TextNode = ... # type: QDomNode.NodeType
        CDATASectionNode = ... # type: QDomNode.NodeType
        EntityReferenceNode = ... # type: QDomNode.NodeType
        EntityNode = ... # type: QDomNode.NodeType
        ProcessingInstructionNode = ... # type: QDomNode.NodeType
        CommentNode = ... # type: QDomNode.NodeType
        DocumentNode = ... # type: QDomNode.NodeType
        DocumentTypeNode = ... # type: QDomNode.NodeType
        DocumentFragmentNode = ... # type: QDomNode.NodeType
        NotationNode = ... # type: QDomNode.NodeType
        BaseNode = ... # type: QDomNode.NodeType
        CharacterDataNode = ... # type: QDomNode.NodeType

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDomNode') -> None: ...

    def columnNumber(self) -> int: ...
    def lineNumber(self) -> int: ...
    def nextSiblingElement(self, taName: str = ..., namespaceURI: str = ...) -> 'QDomElement': ...
    def previousSiblingElement(self, tagName: str = ..., namespaceURI: str = ...) -> 'QDomElement': ...
    def lastChildElement(self, tagName: str = ..., namespaceURI: str = ...) -> 'QDomElement': ...
    def firstChildElement(self, tagName: str = ..., namespaceURI: str = ...) -> 'QDomElement': ...
    def save(self, a0: QtCore.QTextStream, a1: int, a2: 'QDomNode.EncodingPolicy' = ...) -> None: ...
    def toComment(self) -> 'QDomComment': ...
    def toCharacterData(self) -> 'QDomCharacterData': ...
    def toProcessingInstruction(self) -> 'QDomProcessingInstruction': ...
    def toNotation(self) -> 'QDomNotation': ...
    def toEntity(self) -> 'QDomEntity': ...
    def toText(self) -> 'QDomText': ...
    def toEntityReference(self) -> 'QDomEntityReference': ...
    def toElement(self) -> 'QDomElement': ...
    def toDocumentType(self) -> 'QDomDocumentType': ...
    def toDocument(self) -> 'QDomDocument': ...
    def toDocumentFragment(self) -> 'QDomDocumentFragment': ...
    def toCDATASection(self) -> 'QDomCDATASection': ...
    def toAttr(self) -> 'QDomAttr': ...
    def clear(self) -> None: ...
    def isNull(self) -> bool: ...
    def namedItem(self, name: str) -> 'QDomNode': ...
    def isComment(self) -> bool: ...
    def isCharacterData(self) -> bool: ...
    def isProcessingInstruction(self) -> bool: ...
    def isNotation(self) -> bool: ...
    def isEntity(self) -> bool: ...
    def isText(self) -> bool: ...
    def isEntityReference(self) -> bool: ...
    def isElement(self) -> bool: ...
    def isDocumentType(self) -> bool: ...
    def isDocument(self) -> bool: ...
    def isDocumentFragment(self) -> bool: ...
    def isCDATASection(self) -> bool: ...
    def isAttr(self) -> bool: ...
    def setPrefix(self, pre: str) -> None: ...
    def prefix(self) -> str: ...
    def setNodeValue(self, a0: str) -> None: ...
    def nodeValue(self) -> str: ...
    def hasAttributes(self) -> bool: ...
    def localName(self) -> str: ...
    def namespaceURI(self) -> str: ...
    def ownerDocument(self) -> 'QDomDocument': ...
    def attributes(self) -> 'QDomNamedNodeMap': ...
    def nextSibling(self) -> 'QDomNode': ...
    def previousSibling(self) -> 'QDomNode': ...
    def lastChild(self) -> 'QDomNode': ...
    def firstChild(self) -> 'QDomNode': ...
    def childNodes(self) -> 'QDomNodeList': ...
    def parentNode(self) -> 'QDomNode': ...
    def nodeType(self) -> 'QDomNode.NodeType': ...
    def nodeName(self) -> str: ...
    def isSupported(self, feature: str, version: str) -> bool: ...
    def normalize(self) -> None: ...
    def cloneNode(self, deep: bool = ...) -> 'QDomNode': ...
    def hasChildNodes(self) -> bool: ...
    def appendChild(self, newChild: 'QDomNode') -> 'QDomNode': ...
    def removeChild(self, oldChild: 'QDomNode') -> 'QDomNode': ...
    def replaceChild(self, newChild: 'QDomNode', oldChild: 'QDomNode') -> 'QDomNode': ...
    def insertAfter(self, newChild: 'QDomNode', refChild: 'QDomNode') -> 'QDomNode': ...
    def insertBefore(self, newChild: 'QDomNode', refChild: 'QDomNode') -> 'QDomNode': ...
    def __ne__(self, other: object): ...
    def __eq__(self, other: object): ...


class QDomNodeList(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDomNodeList') -> None: ...

    def isEmpty(self) -> bool: ...
    def size(self) -> int: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...
    def length(self) -> int: ...
    def at(self, index: int) -> QDomNode: ...
    def item(self, index: int) -> QDomNode: ...
    def __ne__(self, other: object): ...
    def __eq__(self, other: object): ...


class QDomDocumentType(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomDocumentType') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def internalSubset(self) -> str: ...
    def systemId(self) -> str: ...
    def publicId(self) -> str: ...
    def notations(self) -> 'QDomNamedNodeMap': ...
    def entities(self) -> 'QDomNamedNodeMap': ...
    def name(self) -> str: ...


class QDomDocument(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, name: str) -> None: ...
    @typing.overload
    def __init__(self, doctype: QDomDocumentType) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomDocument') -> None: ...

    def toByteArray(self, indent: int = ...) -> QtCore.QByteArray: ...
    def toString(self, indent: int = ...) -> str: ...
    @typing.overload
    def setContent(self, text: QtCore.QByteArray, namespaceProcessing: bool) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, text: str, namespaceProcessing: bool) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, dev: QtCore.QIODevice, namespaceProcessing: bool) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, text: QtCore.QByteArray) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, text: str) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, dev: QtCore.QIODevice) -> typing.Tuple[bool, str, int, int]: ...
    @typing.overload
    def setContent(self, reader: QtCore.QXmlStreamReader, namespaceProcessing: bool) -> typing.Tuple[bool, str, int, int]: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def documentElement(self) -> 'QDomElement': ...
    def implementation(self) -> QDomImplementation: ...
    def doctype(self) -> QDomDocumentType: ...
    def elementById(self, elementId: str) -> 'QDomElement': ...
    def elementsByTagNameNS(self, nsURI: str, localName: str) -> QDomNodeList: ...
    def createAttributeNS(self, nsURI: str, qName: str) -> 'QDomAttr': ...
    def createElementNS(self, nsURI: str, qName: str) -> 'QDomElement': ...
    def importNode(self, importedNode: QDomNode, deep: bool) -> QDomNode: ...
    def elementsByTagName(self, tagname: str) -> QDomNodeList: ...
    def createEntityReference(self, name: str) -> 'QDomEntityReference': ...
    def createAttribute(self, name: str) -> 'QDomAttr': ...
    def createProcessingInstruction(self, target: str, data: str) -> 'QDomProcessingInstruction': ...
    def createCDATASection(self, data: str) -> 'QDomCDATASection': ...
    def createComment(self, data: str) -> 'QDomComment': ...
    def createTextNode(self, data: str) -> 'QDomText': ...
    def createDocumentFragment(self) -> 'QDomDocumentFragment': ...
    def createElement(self, tagName: str) -> 'QDomElement': ...


class QDomNamedNodeMap(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QDomNamedNodeMap') -> None: ...

    def contains(self, name: str) -> bool: ...
    def isEmpty(self) -> bool: ...
    def size(self) -> int: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...
    def length(self) -> int: ...
    def removeNamedItemNS(self, nsURI: str, localName: str) -> QDomNode: ...
    def setNamedItemNS(self, newNode: QDomNode) -> QDomNode: ...
    def namedItemNS(self, nsURI: str, localName: str) -> QDomNode: ...
    def item(self, index: int) -> QDomNode: ...
    def removeNamedItem(self, name: str) -> QDomNode: ...
    def setNamedItem(self, newNode: QDomNode) -> QDomNode: ...
    def namedItem(self, name: str) -> QDomNode: ...
    def __ne__(self, other: object): ...
    def __eq__(self, other: object): ...


class QDomDocumentFragment(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomDocumentFragment') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...


class QDomCharacterData(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomCharacterData') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def setData(self, a0: str) -> None: ...
    def data(self) -> str: ...
    def length(self) -> int: ...
    def replaceData(self, offset: int, count: int, arg: str) -> None: ...
    def deleteData(self, offset: int, count: int) -> None: ...
    def insertData(self, offset: int, arg: str) -> None: ...
    def appendData(self, arg: str) -> None: ...
    def substringData(self, offset: int, count: int) -> str: ...


class QDomAttr(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomAttr') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def setValue(self, a0: str) -> None: ...
    def value(self) -> str: ...
    def ownerElement(self) -> 'QDomElement': ...
    def specified(self) -> bool: ...
    def name(self) -> str: ...


class QDomElement(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomElement') -> None: ...

    def text(self) -> str: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def attributes(self) -> QDomNamedNodeMap: ...
    def setTagName(self, name: str) -> None: ...
    def tagName(self) -> str: ...
    def hasAttributeNS(self, nsURI: str, localName: str) -> bool: ...
    def elementsByTagNameNS(self, nsURI: str, localName: str) -> QDomNodeList: ...
    def setAttributeNodeNS(self, newAttr: QDomAttr) -> QDomAttr: ...
    def attributeNodeNS(self, nsURI: str, localName: str) -> QDomAttr: ...
    def removeAttributeNS(self, nsURI: str, localName: str) -> None: ...
    @typing.overload
    def setAttributeNS(self, nsURI: str, qName: str, value: str) -> None: ...
    @typing.overload
    def setAttributeNS(self, nsURI: str, qName: str, value: float) -> None: ...
    @typing.overload
    def setAttributeNS(self, nsURI: str, qName: str, value: int) -> None: ...
    def attributeNS(self, nsURI: str, localName: str, defaultValue: str = ...) -> str: ...
    def hasAttribute(self, name: str) -> bool: ...
    def elementsByTagName(self, tagname: str) -> QDomNodeList: ...
    def removeAttributeNode(self, oldAttr: QDomAttr) -> QDomAttr: ...
    def setAttributeNode(self, newAttr: QDomAttr) -> QDomAttr: ...
    def attributeNode(self, name: str) -> QDomAttr: ...
    def removeAttribute(self, name: str) -> None: ...
    @typing.overload
    def setAttribute(self, name: str, value: str) -> None: ...
    @typing.overload
    def setAttribute(self, name: str, value: int) -> None: ...
    @typing.overload
    def setAttribute(self, name: str, value: int) -> None: ...
    @typing.overload
    def setAttribute(self, name: str, value: float) -> None: ...
    @typing.overload
    def setAttribute(self, name: str, value: int) -> None: ...
    def attribute(self, name: str, defaultValue: str = ...) -> str: ...


class QDomText(QDomCharacterData):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomText') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def splitText(self, offset: int) -> 'QDomText': ...


class QDomComment(QDomCharacterData):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomComment') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...


class QDomCDATASection(QDomText):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomCDATASection') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...


class QDomNotation(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomNotation') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def systemId(self) -> str: ...
    def publicId(self) -> str: ...


class QDomEntity(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomEntity') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def notationName(self) -> str: ...
    def systemId(self) -> str: ...
    def publicId(self) -> str: ...


class QDomEntityReference(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomEntityReference') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...


class QDomProcessingInstruction(QDomNode):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: 'QDomProcessingInstruction') -> None: ...

    def nodeType(self) -> QDomNode.NodeType: ...
    def setData(self, d: str) -> None: ...
    def data(self) -> str: ...
    def target(self) -> str: ...
