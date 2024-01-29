#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2024 Inria

"""Point represented by a sphere.

Example:
    .. code:: python

        import meshcat
        import meshcat_shapes

        vis = meshcat.Visualizer().open()

        meshcat_shapes.point(
            vis["red_point"],
            opacity=0.3,
            radius=0.05,
            color=0xFF0000,
        )
"""

import meshcat


def point(
    handle: meshcat.Visualizer,
    radius: float = 0.01,
    color: int = 0x000000,
    opacity: float = 1.0,
) -> None:
    """Set MeshCat handle to a point, represented by a sphere.

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
