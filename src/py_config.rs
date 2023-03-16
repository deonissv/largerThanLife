use pyo3::prelude::*;
use pyo3::types::{IntoPyDict, PyType};

use crate::ltl_engine::config::Config;
use crate::py_neighbourhood::PyNeighbourhood;

#[pyclass]
#[derive(Debug, Clone, PartialEq)]
pub struct PyConfig {
    pub config: Config,
}

#[pymethods]
impl PyConfig {
    #[new]
    fn new(rr: u8, cc: u8, mm: u8, ss: (u16, u16), bb: (u16, u16), nn: PyNeighbourhood) -> Self {
        PyConfig {
            config: Config {
                rr,
                cc,
                mm,
                ss,
                bb,
                nn: nn.to_neighbourhood(),
            },
        }
    }

    #[getter]
    fn rr(&self) -> u8 {
        self.config.rr
    }

    #[getter]
    fn cc(&self) -> u8 {
        self.config.cc
    }

    #[getter]
    fn mm(&self) -> u8 {
        self.config.mm
    }

    #[getter]
    fn ss(&self) -> (u16, u16) {
        self.config.ss
    }

    #[getter]
    fn bb(&self) -> (u16, u16) {
        self.config.bb
    }

    #[getter]
    fn nn(&self) -> PyNeighbourhood {
        PyNeighbourhood::from_neighbourhood(self.config.nn.clone())
    }

    #[getter]
    fn __dict__(&self) -> PyObject {
        Python::with_gil(|py| {
            let key_vals = &[
                ("rr", self.config.rr.to_object(py)),
                ("cc", self.config.cc.to_object(py)),
                ("mm", self.config.mm.to_object(py)),
                ("ss", self.config.ss.to_object(py)),
                ("bb", self.config.bb.to_object(py)),
                ("nn", self.config.nn.to_string().to_object(py)),
            ];
            key_vals.into_py_dict(py).into()
        })
    }

    #[classmethod]
    fn randomize(_cls: &PyType, seed: Option<u64>) -> Self {
        PyConfig {
            config: Config::randomize(seed),
        }
    }
}
