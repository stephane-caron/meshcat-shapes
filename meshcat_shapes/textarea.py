#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2023 Inria
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This file incorporates work covered by the following copyright and permission
# notice:
#
#     geometry.py from https://github.com/rdeits/meshcat-python/pull/32
#     Copyright (c) 2018 Shen Shen
#     License: MIT


"""Text area.

Notes:
    To be simplified once https://github.com/rdeits/meshcat-python/pull/111
    makes it to a released version of meshcat-python.
"""

import meshcat
from meshcat.geometry import Geometry, Mesh, MeshPhongMaterial, Texture


class Plane(Geometry):
    def __init__(self, width=1, height=1, widthSegments=1, heightSegments=1):
        super(Plane, self).__init__()
        self.width = width
        self.height = height
        self.widthSegments = widthSegments
        self.heightSegments = heightSegments

    def lower(self, object_data):
        return {
            "uuid": self.uuid,
            "type": "PlaneGeometry",
            "width": self.width,
            "height": self.height,
            "widthSegments": self.widthSegments,
            "heightSegments": self.heightSegments,
        }


class TextTexture(Texture):
    def __init__(self, text, font_size=100, font_face="sans-serif"):
        super(TextTexture, self).__init__()
        self.text = text
        # font_size will be passed to the JS side as is; however if the
        # text width exceeds canvas width, font_size will be reduced.
        self.font_size = font_size
        self.font_face = font_face

    def lower(self, object_data):
        return {
            "uuid": self.uuid,
            "type": "_text",
            "text": self.text,
            "font_size": self.font_size,
            "font_face": self.font_face,
        }


def textarea(
    handle: meshcat.Visualizer,
    text: str,
    width: float = 10.0,
    height: float = 10.0,
    **kwargs,
) -> None:
    """
    Set MeshCat handle to a text area.

    Args:
        handle: MeshCat handle to attach the frame to.
        text: Content to write inside the text area.
        width: Text area width.
        height: Text area height.
        kwargs: Keyword arguments, see :class:`TextTexture`.

    Note:
        As per the de-facto standard (Blender, OpenRAVE, RViz, ...), the
        x-axis is red, the y-axis is green and the z-axis is blue.
    """
    handle.set_object(
        Mesh(
            Plane(width=width, height=height),
            MeshPhongMaterial(
                map=TextTexture(text, **kwargs),
                transparent=True,
                needsUpdate=True,
            ),
        )
    )
