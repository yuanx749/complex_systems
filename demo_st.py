import streamlit as st

from mcs import CA, ODE, PDE, Net


class Args:
    ...


def intro():
    st.header("Modeling and simulation of complex systems")
    st.markdown(":point_left: Please select a model on the left.")


def ode_demo():
    st.header("ODE")
    st.subheader("Lotka-Volterra equations")
    st.markdown(
        r"""
        $\frac{dx}{dt} = ax - bxy$\
        $\frac{dy}{dt} = dxy - cy$
        """
    )

    @st.cache
    def simulate():
        ode = ODE(**args_ode.__dict__)
        ode.initialize(x0=x0)
        ode.simulate(f=ode.lv(**args_lv.__dict__))
        return ode

    with st.form("parameters"):
        args_lv = Args()
        args_ode = Args()

        st.text("Parameters: ")
        col1, col2 = st.columns(2)
        args_lv.a = col1.number_input("a", min_value=0.01, value=1.1)
        args_lv.b = col2.number_input("b", min_value=0.01, value=0.4)
        args_lv.c = col1.number_input("c", min_value=0.01, value=0.4)
        args_lv.d = col2.number_input("d", min_value=0.01, value=0.1)

        st.text("Simulation: ")
        col3, col4 = st.columns(2)
        args_ode.max_step = col3.number_input("Max step", min_value=1, value=10000)
        args_ode.dt = col4.number_input("Step size for time", min_value=0.001, value=0.01, step=0.001, format="%.3f")

        args_ode.dim = 2
        x0 = (10, 10)
        if st.form_submit_button("Submit"):
            st.session_state["ode"] = simulate()

    if "ode" in st.session_state:
        model = st.session_state["ode"]
        fig = model.visualize()
        (ax,) = fig.axes
        ax.legend(["x", "y"])
        ax.set(
            xlabel="time",
            ylabel="states",
        )
        st.pyplot(fig)


def game_of_life():
    st.header("Cellular automata")
    st.subheader("Game of life")
    st.markdown("Conway's Game of Life.")

    @st.cache
    def simulate():
        ca = CA(max_step=max_step, size_x=x, size_y=y)
        ca.initialize()
        ca.simulate(F=ca.game_of_life)
        return ca

    with st.form("parameters"):
        st.text("Parameters: ")
        x = st.number_input("Number of cells in x dimension", min_value=1, value=50)
        y = st.number_input("Number of cells in y dimension", min_value=1, value=50)

        st.text("Simulation: ")
        max_step = st.number_input("Max step", min_value=1, value=100)

        if st.form_submit_button("Submit"):
            st.session_state["ca"] = simulate()

    if "ca" in st.session_state:
        max_step_ = max_step - 1
        model = st.session_state["ca"]
        step = st.slider("Step", min_value=0, max_value=max_step_, value=max_step_)
        fig = model.visualize(step=step)
        st.pyplot(fig)


def turing():
    st.header("PDE")
    st.subheader("Turing pattern")
    st.markdown(
        r"""
        Reaction-diffusion equations:

        $\frac{\partial u}{\partial t} = a(u-h) + b(v-k) + D_u \Delta u$\
        $\frac{\partial v}{\partial t} = c(u-h) + d(v-k) + D_v \Delta v$

        The state variables $u$ and $v$ represent concentrations of two substances. In this system, if the diffusion terms are ignored, the only homogeneous equilibrium state is $(h, k)$. The system can spontaneously generate a non-homogeneous pattern even small initial pertubations are applied.
        """
    )

    @st.cache
    def simulate():
        pde = PDE(**args_pde.__dict__)
        pde.initialize()
        pde.simulate(F=pde.turing(**args_turing.__dict__))
        return pde

    with st.form("parameters"):
        args_turing = Args()
        args_pde = Args()

        st.text("Parameters: ")
        col1, col2 = st.columns(2)
        args_turing.a = col1.number_input("a", value=1.0)
        args_turing.b = col2.number_input("b", value=-1.0)
        args_turing.c = col1.number_input("c", value=2.0)
        args_turing.d = col2.number_input("d", value=-1.5)
        args_turing.h = col1.number_input("h", value=1.0)
        args_turing.k = col2.number_input("k", value=1.0)
        args_turing.Du = col1.number_input("Du", min_value=1e-5, value=1e-4, step=1e-5, format="%.5f")
        args_turing.Dv = col2.number_input("Dv", min_value=1e-5, value=6e-4, step=1e-5, format="%.5f")

        st.text("Simulation: ")
        col3, col4 = st.columns(2)
        args_pde.max_step = col3.number_input("Max step", min_value=1, value=2500)
        args_pde.dt = col4.number_input("Step size for time", min_value=0.001, value=0.02, step=0.001, format="%.3f")
        args_turing.dh = args_pde.dh = col3.number_input("Spatial resolution", min_value=0.01, value=0.01)
        args_pde.size = col4.number_input("Grid size", min_value=1, value=100)
        args_pde.dim = 2

        if st.form_submit_button("Submit"):
            st.session_state["pde"] = simulate()

    if "pde" in st.session_state:
        max_step = args_pde.max_step - 1
        model = st.session_state["pde"]
        step = st.slider("Step", min_value=0, max_value=max_step, value=max_step)
        figs = model.visualize(step=step)
        (ax,) = figs[0].axes
        ax.set(title=r"Density of $u$")
        st.pyplot(figs[0])


def oscillator():
    st.header("Dynamical network")
    st.subheader("Synchronization of coupled oscillators")
    st.markdown(
        r"""
        In this example, nodes are oscillating in Zachary's Karate Club network.

        $\frac{d\theta_i}{dt} = b\theta_i + a\sum_{j\in N_i}(\theta_j-\theta_i)$

        Here $\theta_i$ is the state and $N_i$ is the neighborhood of node $i$. Stable trajetory occurs when $b - a\lambda_2 < 0$, where $a\ge 0$ and $\lambda_2$ is the second smallest eigenvalue (the spectral gap) of Laplacian matrix. The spectral gap of Karate Club graph is 0.4685, so when $a=2$ and $b=0.9$, the synchronization occurs.

        The colors are based on the states of the nodes.
        """
    )

    @st.cache(allow_output_mutation=True)
    def simulate():
        net = Net(max_step=max_step)
        net.initialize()
        net.simulate(**args_sync.__dict__)
        return net

    with st.form("parameters"):
        args_sync = Args()

        st.text("Parameters: ")
        col1, col2 = st.columns(2)
        args_sync.a = col1.number_input("a", min_value=0.1, value=2.0)
        args_sync.b = col2.number_input("b", min_value=0.1, value=0.9)

        st.text("Simulation: ")
        col3, col4 = st.columns(2)
        max_step = col3.number_input("Max step", min_value=1, value=2000)
        args_sync.dt = col4.number_input("Step size for time", min_value=0.001, value=0.01, step=0.001, format="%.3f")

        if st.form_submit_button("Submit"):
            st.session_state["net"] = simulate()

    if "net" in st.session_state:
        max_step_ = max_step - 1
        model = st.session_state["net"]
        step = st.slider("Step", min_value=0, max_value=max_step_, value=max_step_)
        fig = model.visualize(step=step)
        st.pyplot(fig)


def sidebar():
    demo_function = {
        "---": intro,
        "ODE": ode_demo,
        "Cellular automata": game_of_life,
        "PDE": turing,
        "Dynamical network": oscillator,
    }
    model = st.sidebar.selectbox("Select a model: ", demo_function.keys())
    demo_function[model]()


if __name__ == "__main__":
    try:
        sidebar()
    except Exception as e:
        st.exception(e)
