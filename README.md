[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/yuanx749/complex_systems.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/yuanx749/complex_systems/context:python)
[![Maintainability](https://api.codeclimate.com/v1/badges/6ef4b6837545f2bc2e22/maintainability)](https://codeclimate.com/github/yuanx749/complex_systems/maintainability)

# complex_systems
This package is mainly for educational purpose. Instead of writing scattered and redundant scripts, it is implemented using OOP, thus enabling a coherent scheme and easy extension to incorporate more models.

Modeling and simulation of complex systems:
- Difference equation
- ODE
- Cellular automaton
- PDE
- Dynamical network

## demo
See [demo.md](demo.md) or run `jupyter notebook demo.ipynb`.

## install
```bash
pip install -r requirements.txt
```
Alternatively, using `setuptools`, run in the cloned directory:
```bash
python -m pip install --upgrade pip
pip install .
```
Install in development mode:
```bash
pip install -e .[dev]
```
Uninstall:
```bash
pip uninstall modeling-complex-systems
```
