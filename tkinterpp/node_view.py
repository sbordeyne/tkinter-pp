try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from .canvases import ScrolledCanvas
from .variables import NodeVar
from collections import namedtuple
import math


Element = namedtuple("Element", ["id", "coords"])
BezierElement = namedtuple("BezierElement", ["id", "nodes"])


class NodeView(ScrolledCanvas):
    def __init__(self, master=None, **kwargs):
        super(NodeView, self).__init__(master, **kwargs)
        self.nodes = {}
        self.connections = []
        self.first_node_of_connection = None
        self._bezier_id = 0

    def create_node(self, coords, node_name, node_data=None, node_connections=None,
                    tags=None, width=1.0, state=tk.NORMAL):
        if node_data is None:
            node_data = {}
        if node_connections is None:
            node_connections = []
        if tags is None:
            tags = []
        tags.append(node_name)
        rectangle_bbox = list(coords) + [60, 30]
        text_pos = coords[0] + 5, coords[1] + 5
        rectangle_id = self.canv.create_rectangle(rectangle_bbox, tags=tags, width=width,
                                                  state=state)
        text_id = self.canv.create_text(text_pos, state=state, width=width)
        self.nodes[node_name] = {"variable": NodeVar(node_name, node_data, node_connections),
                                 "element_ids": [Element(rectangle_id, rectangle_bbox),
                                                 Element(text_id, text_pos)],
                                 "bezier_ids": []}
        self.canv.tag_bind(node_name, '<B1-Motion>', lambda evt, n=node_name: self._on_node_drag(evt, n))
        self.canv.tag_bind(node_name, '<Button-1>', lambda evt, n=node_name: self._create_connection(evt, n))
        return node_name

    def _on_node_drag(self, event, node):
        for e in self.nodes[node]["element_ids"]:
            eid = e.id
            coords = e.coords
            coords[0] = coords[0] + event.x
            coords[1] = coords[1] + event.y
            if len(coords) == 2:
                self.canv.itemconfig(eid, coords=coords)
            elif len(coords) == 4:
                self.canv.itemconfig(eid, bbox=coords)

    def _create_connection(self, event, node):
        if self.first_node_of_connection is None:
            self.first_node_of_connection = (node, (event.x, event.y))
        else:
            cp1 = self.first_node_of_connection[1]
            cp4 = (event.x, event.y)
            x_avg = (cp4[0] - cp1[0]) / 2
            cp2 = (x_avg, cp1[1])
            cp3 = (x_avg, cp4[1])
            bezier_id = self.create_bezier([cp1, cp2, cp3, cp4])
            node_a = self.first_node_of_connection[0]
            node_b = node
            self.nodes[node_a]["bezier_ids"].append(BezierElement(bezier_id, [node_a, node_b]))
            self.nodes[node_a]["variable"].connect(self.nodes[node]["variable"])
            self.first_node_of_connection = None

    def create_bezier(self, control_points):
        def bernstein(idx, degree):
            m = degree
            binom = math.comb(m, idx)
            return lambda u: binom * u ** idx * (1 - u) ** (m - idx)

        def bezier(cpts, u):
            rv = [0, 0]
            for idx, cp in enumerate(cpts):
                rv[0] += bernstein(idx, len(cpts))(u) * cp[0]
                rv[1] += bernstein(idx, len(cpts))(u) * cp[1]
            return rv

        tag_name = f"bezier{self._bezier_id}"
        self._bezier_id += 1

        # Start x and y coordinates, when t = 0
        x_start = control_points[0][0]
        y_start = control_points[0][1]

        # loops through
        n = 50
        for i in range(n):
            t = i / n
            x, y = bezier(control_points, t)

            self.canv.create_line(x, y, x_start, y_start, tags=[tag_name])
            # updates initial values
            x_start = x
            y_start = y
        return tag_name

