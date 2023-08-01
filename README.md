# complex_systems

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/da8e233aa8514f40a2e8042b2ef2302f)](https://app.codacy.com/gh/yuanx749/complex_systems/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/6ef4b6837545f2bc2e22/maintainability)](https://codeclimate.com/github/yuanx749/complex_systems/maintainability)

This repo is mainly for educational purpose. Instead of writing scattered and redundant scripts, it is implemented using OOP, thus enabling a coherent scheme and easy extension to incorporate more models.

Modeling and simulation of complex systems:

- Difference equation
- ODE
- Cellular automaton
- PDE
- Dynamical network

## Demo

Navigate to [Streamlit](https://share.streamlit.io/yuanx749/complex_systems/main/demo_st.py) to play with a demo.

Alternatively, see this [notebook](demo/demo.md) or run `jupyter notebook demo/demo.ipynb`.

## Install

Use as an application without installation of the package:

```bash
pip install -r requirements.txt
```

Then work only in the repo root directory.

Alternatively, use as an installed package. On Windows, using `setuptools`, run in the cloned directory:

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
