#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
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

"""
Point represented by a sphere.
"""

import meshcat


def point(
    handle: meshcat.Visualizer,
    radius: float = 0.01,
    color: int = 0x000000,
    opacity: float = 1.0,
) -> None:
    """
    Set MeshCat handle to a point, represented by a sphere.

    Args:
        handle: MeshCat handle to attach the frame to.
        radius: Radius of the sphere, in [m].
        color: Color of the sphere.
        opacity: Opacity of all three unit vectors.
    """
    material = meshcat.geometry.MeshLambertMaterial(
        color=color, opacity=opacity
    )
    sphere = meshcat.geometry.Sphere(radius)
    handle.set_object(sphere, material)
