# meshcat-shapes

[![Build](https://img.shields.io/github/actions/workflow/status/stephane-caron/meshcat-shapes/build.yml?branch=main)](https://github.com/stephane-caron/meshcat-shapes/actions)
[![Documentation](https://img.shields.io/github/actions/workflow/status/stephane-caron/meshcat-shapes/docs.yml?branch=main&label=docs)](https://stephane-caron.github.io/meshcat-shapes/)
[![Coverage](https://coveralls.io/repos/github/stephane-caron/meshcat-shapes/badge.svg?branch=main)](https://coveralls.io/github/stephane-caron/meshcat-shapes?branch=main)
[![Conda version](https://img.shields.io/conda/vn/conda-forge/meshcat-shapes.svg)](https://anaconda.org/conda-forge/meshcat-shapes)
[![PyPI version](https://img.shields.io/pypi/v/meshcat-shapes)](https://pypi.org/project/meshcat-shapes/)

Additional shapes to decorate [MeshCat](https://github.com/meshcat-dev/meshcat-python) scenes:

| [``meshcat_shapes.frame``](https://stephane-caron.github.io/meshcat-shapes/shapes.html#module-meshcat_shapes.frame) | [``meshcat_shapes.point``](https://stephane-caron.github.io/meshcat-shapes/shapes.html#module-meshcat_shapes.point) | [``meshcat_shapes.textarea``](https://stephane-caron.github.io/meshcat-shapes/shapes.html#module-meshcat_shapes.textarea) |
|--------------------------|--------------------------|-----------------------------|
| <a href="https://stephane-caron.github.io/meshcat-shapes/shapes.html#module-meshcat_shapes.frame"><img src="https://github.com/stephane-caron/meshcat-shapes/raw/main/gallery/frame.png" width="250"></a> | <a href="https://stephane-caron.github.io/meshcat-shapes/shapes.html#module-meshcat_shapes.point"><img src="https://github.com/stephane-caron/meshcat-shapes/raw/main/gallery/point.png" width="250"></a> | <a href="https://stephane-caron.github.io/meshcat-shapes/shapes.html#module-meshcat_shapes.textarea"><img src="https://github.com/stephane-caron/meshcat-shapes/raw/main/gallery/textarea.png" width="250"></a> |

PRs are welcome: open one if you have implemented a shape that can be useful to others.

## Installation

### From conda-forge

```console
conda install -c conda-forge meshcat-shapes
```

### From PyPI

```console
pip install meshcat-shapes
```

## Usage

```python
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

meshcat_shapes.point(
    vis["red_point"],
    opacity=0.3,
    radius=0.05,
    color=0xFF0000,
)

meshcat_shapes.textarea(vis["text"], "super easy")
```
