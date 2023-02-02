# complex_systems

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/da8e233aa8514f40a2e8042b2ef2302f)](https://www.codacy.com/gh/yuanx749/complex_systems/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=yuanx749/complex_systems&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/6ef4b6837545f2bc2e22/maintainability)](https://codeclimate.com/github/yuanx749/complex_systems/maintainability)

This package is mainly for educational purpose. Instead of writing scattered and redundant scripts, it is implemented using OOP, thus enabling a coherent scheme and easy extension to incorporate more models.

Modeling and simulation of complex systems:

- Difference equation
- ODE
- Cellular automaton
- PDE
- Dynamical network

## demo

Navigate to [Streamlit](https://share.streamlit.io/yuanx749/complex_systems/main/demo_st.py) to play with a demo.

Alternatively, see [demo.md](demo.md) or run `jupyter notebook demo.ipynb`.

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
