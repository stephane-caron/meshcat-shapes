#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron
# Copyright 2024 Inria

"""Frames represented by an origin and three colored axes.

Example:
    .. code:: python

        import meshcat
        import meshcat_shapes

        vis = meshcat.Visualizer().open()

        meshcat_shapes.frame(
            vis["my_frame"],
            axis_length=0.2,
            axis_thickness=0.01,
            opacity=0.8,
            origin_radius=0.02,
        )
"""

import meshcat
import numpy as np


def __attach_axes(
    handle: meshcat.Visualizer,
    length: float = 0.05,
    thickness: float = 0.002,
    opacity: float = 1.0,
) -> None:
    """Attach a set of three basis axes to a MeshCat handle.

    Args:
        handle: MeshCat handle to attach the basis axes to.
        length: Length of axis unit vectors.
        thickness: Thickness of axis unit vectors.
        opacity: Opacity of all three unit vectors.

    Note:
        As per the de-facto standard (Blender, OpenRAVE, RViz, ...), the
        x-axis is red, the y-axis is green and the z-axis is blue.
    """
    direction_names = ["x", "y", "z"]
    colors = [0xFF0000, 0x00FF00, 0x0000FF]
    rotation_axes = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
    position_cylinder_in_body = 0.5 * length * np.eye(3)
    for i in range(3):
        dir_name = direction_names[i]
        material = meshcat.geometry.MeshLambertMaterial(
            color=colors[i], opacity=opacity
        )
        transform_cylinder_to_body = meshcat.transformations.rotation_matrix(
            np.pi / 2, rotation_axes[i]
        )
        transform_cylinder_to_body[0:3, 3] = position_cylinder_in_body[i]
        cylinder = meshcat.geometry.Cylinder(length, thickness)
        handle[dir_name].set_object(cylinder, material)
        handle[dir_name].set_transform(transform_cylinder_to_body)


def frame(
    handle: meshcat.Visualizer,
    axis_length: float = 0.1,
    axis_thickness: float = 0.005,
    opacity: float = 1.0,
    origin_color: int = 0x000000,
    origin_radius: float = 0.01,
) -> None:
    """Set MeshCat handle to a frame, represented by an origin and three axes.

    Args:
        handle: MeshCat handle to attach the frame to.
        axis_length: Length of axis unit vectors, in [m].
        axis_thickness: Thickness of axis unit vectors, in [m].
        opacity: Opacity of all three unit vectors.
        origin_color: Color of the origin sphere.
        origin_radius: Radius of the frame origin sphere, in [m].

    Note:
        As per the de-facto standard (Blender, OpenRAVE, RViz, ...), the
        x-axis is red, the y-axis is green and the z-axis is blue.
    """
    material = meshcat.geometry.MeshLambertMaterial(
        color=origin_color, opacity=opacity
    )
    sphere = meshcat.geometry.Sphere(origin_radius)
    handle.set_object(sphere, material)
    __attach_axes(handle, axis_length, axis_thickness, opacity)
