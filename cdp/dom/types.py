'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: dom
Experimental: False
'''

from dataclasses import dataclass, field
import typing

from ..page import types as page


class NodeId(int):
    '''
    Unique DOM node identifier.
    '''
    @classmethod
    def from_response(cls, response):
        return cls(response)

    def __repr__(self):
        return 'NodeId({})'.format(int.__repr__(self))


class BackendNodeId(int):
    '''
    Unique DOM node identifier used to reference a node that may not have been pushed to the
    front-end.
    '''
    @classmethod
    def from_response(cls, response):
        return cls(response)

    def __repr__(self):
        return 'BackendNodeId({})'.format(int.__repr__(self))



class PseudoType:
    '''
    Pseudo element type.
    '''
    FIRST_LINE = "first-line"
    FIRST_LETTER = "first-letter"
    BEFORE = "before"
    AFTER = "after"
    BACKDROP = "backdrop"
    SELECTION = "selection"
    FIRST_LINE_INHERITED = "first-line-inherited"
    SCROLLBAR = "scrollbar"
    SCROLLBAR_THUMB = "scrollbar-thumb"
    SCROLLBAR_BUTTON = "scrollbar-button"
    SCROLLBAR_TRACK = "scrollbar-track"
    SCROLLBAR_TRACK_PIECE = "scrollbar-track-piece"
    SCROLLBAR_CORNER = "scrollbar-corner"
    RESIZER = "resizer"
    INPUT_LIST_BUTTON = "input-list-button"


class ShadowRootType:
    '''
    Shadow root type.
    '''
    USER_AGENT = "user-agent"
    OPEN = "open"
    CLOSED = "closed"

class Quad(typing.List):
    '''
    An array of quad vertices, x immediately followed by y for each point, points clock-wise.
    '''
    @classmethod
    def from_response(cls, response):
        return cls(response)

    def __repr__(self):
        return 'Quad({})'.format(typing.List.__repr__(self))



@dataclass
class BackendNode:
    '''
    Backend node with a friendly name.
    '''
    #: `Node`'s nodeType.
    node_type: int

    #: `Node`'s nodeName.
    node_name: str

    backend_node_id: BackendNodeId

    @classmethod
    def from_response(cls, response):
        return cls(
            node_type=int(response.get('nodeType')),
            node_name=str(response.get('nodeName')),
            backend_node_id=BackendNodeId.from_response(response.get('backendNodeId')),
        )


@dataclass
class Node:
    '''
    DOM interaction is implemented in terms of mirror objects that represent the actual DOM nodes.
    DOMNode is a base node mirror type.
    '''
    #: Node identifier that is passed into the rest of the DOM messages as the `nodeId`. Backend
    #: will only push node with given `id` once. It is aware of all requested nodes and will only
    #: fire DOM events for nodes known to the client.
    node_id: NodeId

    #: The id of the parent node if any.
    parent_id: NodeId

    #: The BackendNodeId for this node.
    backend_node_id: BackendNodeId

    #: `Node`'s nodeType.
    node_type: int

    #: `Node`'s nodeName.
    node_name: str

    #: `Node`'s localName.
    local_name: str

    #: `Node`'s nodeValue.
    node_value: str

    #: Child count for `Container` nodes.
    child_node_count: int

    #: Child nodes of this node when requested with children.
    children: typing.List['Node']

    #: Attributes of the `Element` node in the form of flat array `[name1, value1, name2, value2]`.
    attributes: typing.List

    #: Document URL that `Document` or `FrameOwner` node points to.
    document_url: str

    #: Base URL that `Document` or `FrameOwner` node uses for URL completion.
    base_url: str

    #: `DocumentType`'s publicId.
    public_id: str

    #: `DocumentType`'s systemId.
    system_id: str

    #: `DocumentType`'s internalSubset.
    internal_subset: str

    #: `Document`'s XML version in case of XML documents.
    xml_version: str

    #: `Attr`'s name.
    name: str

    #: `Attr`'s value.
    value: str

    #: Pseudo element type for this node.
    pseudo_type: PseudoType

    #: Shadow root type.
    shadow_root_type: ShadowRootType

    #: Frame ID for frame owner elements.
    frame_id: page.FrameId

    #: Content document for frame owner elements.
    content_document: 'Node'

    #: Shadow root list for given element host.
    shadow_roots: typing.List['Node']

    #: Content document fragment for template elements.
    template_content: 'Node'

    #: Pseudo elements associated with this node.
    pseudo_elements: typing.List['Node']

    #: Import document for the HTMLImport links.
    imported_document: 'Node'

    #: Distributed nodes for given insertion point.
    distributed_nodes: typing.List['BackendNode']

    #: Whether the node is SVG.
    is_svg: bool

    @classmethod
    def from_response(cls, response):
        return cls(
            node_id=NodeId.from_response(response.get('nodeId')),
            parent_id=NodeId.from_response(response.get('parentId')),
            backend_node_id=BackendNodeId.from_response(response.get('backendNodeId')),
            node_type=int(response.get('nodeType')),
            node_name=str(response.get('nodeName')),
            local_name=str(response.get('localName')),
            node_value=str(response.get('nodeValue')),
            child_node_count=int(response.get('childNodeCount')),
            children=[Node.from_response(i) for i in response.get('children')],
            attributes=[str(i) for i in response.get('attributes')],
            document_url=str(response.get('documentURL')),
            base_url=str(response.get('baseURL')),
            public_id=str(response.get('publicId')),
            system_id=str(response.get('systemId')),
            internal_subset=str(response.get('internalSubset')),
            xml_version=str(response.get('xmlVersion')),
            name=str(response.get('name')),
            value=str(response.get('value')),
            pseudo_type=PseudoType.from_response(response.get('pseudoType')),
            shadow_root_type=ShadowRootType.from_response(response.get('shadowRootType')),
            frame_id=page.FrameId.from_response(response.get('frameId')),
            content_document='Node'.from_response(response.get('contentDocument')),
            shadow_roots=[Node.from_response(i) for i in response.get('shadowRoots')],
            template_content='Node'.from_response(response.get('templateContent')),
            pseudo_elements=[Node.from_response(i) for i in response.get('pseudoElements')],
            imported_document='Node'.from_response(response.get('importedDocument')),
            distributed_nodes=[BackendNode.from_response(i) for i in response.get('distributedNodes')],
            is_svg=bool(response.get('isSVG')),
        )


@dataclass
class RGBA:
    '''
    A structure holding an RGBA color.
    '''
    #: The red component, in the [0-255] range.
    r: int

    #: The green component, in the [0-255] range.
    g: int

    #: The blue component, in the [0-255] range.
    b: int

    #: The alpha component, in the [0-1] range (default: 1).
    a: float

    @classmethod
    def from_response(cls, response):
        return cls(
            r=int(response.get('r')),
            g=int(response.get('g')),
            b=int(response.get('b')),
            a=float(response.get('a')),
        )


@dataclass
class ShapeOutsideInfo:
    '''
    CSS Shape Outside details.
    '''
    #: Shape bounds
    bounds: Quad

    #: Shape coordinate details
    shape: typing.List

    #: Margin shape bounds
    margin_shape: typing.List

    @classmethod
    def from_response(cls, response):
        return cls(
            bounds=Quad.from_response(response.get('bounds')),
            shape=[typing.Any(i) for i in response.get('shape')],
            margin_shape=[typing.Any(i) for i in response.get('marginShape')],
        )


@dataclass
class Rect:
    '''
    Rectangle.
    '''
    #: X coordinate
    x: float

    #: Y coordinate
    y: float

    #: Rectangle width
    width: float

    #: Rectangle height
    height: float

    @classmethod
    def from_response(cls, response):
        return cls(
            x=float(response.get('x')),
            y=float(response.get('y')),
            width=float(response.get('width')),
            height=float(response.get('height')),
        )


@dataclass
class BoxModel:
    '''
    Box model.
    '''
    #: Content box
    content: Quad

    #: Padding box
    padding: Quad

    #: Border box
    border: Quad

    #: Margin box
    margin: Quad

    #: Node width
    width: int

    #: Node height
    height: int

    #: Shape outside coordinates
    shape_outside: ShapeOutsideInfo

    @classmethod
    def from_response(cls, response):
        return cls(
            content=Quad.from_response(response.get('content')),
            padding=Quad.from_response(response.get('padding')),
            border=Quad.from_response(response.get('border')),
            margin=Quad.from_response(response.get('margin')),
            width=int(response.get('width')),
            height=int(response.get('height')),
            shape_outside=ShapeOutsideInfo.from_response(response.get('shapeOutside')),
        )
