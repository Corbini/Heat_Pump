from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class Connection(QGraphicsItemGroup):
    def __init__(self, first: QGraphicsPixmapItem, second: QGraphicsItemGroup, scene: QGraphicsScene):
        super().__init__()
        scene.addItem(self)

        self.first = first
        self.second = second

        self.point_stor = []
        self.gen_points(first, second)

        self.gen_lines()

    def __del__(self):
        for child in self.group():
            child.setParentItem(None)
            del child

        super().__del__()

    def gen_points(self, first: QGraphicsItemGroup, second: QGraphicsItemGroup):
        vector = second.scenePos() - first.scenePos()
        distance_x = abs(vector.x())
        distance_y = abs(vector.y())
        print(vector, distance_x, distance_y)
        offset = QPointF(0, 0)
        if distance_x > distance_y:
            offset.setX(vector.x())
        else:
            offset.setY(vector.y())

        # start point
        self.point_stor.append(first.scenePos())

        # points in between
        self.gen_point(offset)
        self.gen_point(vector - offset)

        # end point
        self.point_stor.append(second.scenePos())

    def gen_point(self, offset: QPointF):
        if offset == QPointF(0, 0):
            return

        self.point_stor.append(QPointF( self.point_stor[-1] + offset))

    def gen_lines(self):
        begin = self.point_stor[0]

        for point in self.point_stor[1:]:
            self.addToGroup(QGraphicsLineItem(begin.x(), begin.y(), point.x(), point.y()))
            begin = point

        pass

