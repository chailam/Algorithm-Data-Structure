"""
Author: Loi Chai Lam
Date: 14 May 2018

The Edge class and Vertex class used to represent a weighted graph.
It has the camera attribute inside the vertex to determine this Vertex is a camera or not

"""


class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def __str__(self):
        string = "u: " + str(self.u.vertex) + " " + str(self.u.camera) + " v: " + str(self.v.vertex) + " " + str(self.v.camera) + " weight: " + str(self.weight)
        return string


class Vertex:
    def __init__(self, vertex, camera):
        self.vertex = vertex
        self.camera = camera
        self.previous = ""

    def __str__(self):
        string = str(self.vertex) + " " + str(self.camera)
        return string
