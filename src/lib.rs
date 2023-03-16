mod ltl_engine;
mod py_board;
mod py_config;
mod py_neighbourhood;

use pyo3::prelude::*;

#[pymodule]
fn py_ltl_engine(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<py_neighbourhood::PyNeighbourhood>()?;
    m.add_class::<py_config::PyConfig>()?;
    m.add_class::<py_board::PyBoard>()?;
    Ok(())
}
