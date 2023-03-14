use pyo3::exceptions;
use pyo3::prelude::*;
use std::str::FromStr;

use crate::ltl_engine::neighbourhood::Neighbourhood;

#[pyclass]
#[derive(Debug, Clone, PartialEq)]
pub enum PyNeighbourhood {
    Neumann,
    Moore,
}

impl PyNeighbourhood {
    pub fn to_neighbourhood(&self) -> Neighbourhood {
        match self {
            PyNeighbourhood::Neumann => Neighbourhood::Neumann,
            PyNeighbourhood::Moore => Neighbourhood::Moore,
        }
    }

    pub fn from_neighbourhood(neighbourhood: Neighbourhood) -> Self {
        match neighbourhood {
            Neighbourhood::Neumann => PyNeighbourhood::Neumann,
            Neighbourhood::Moore => PyNeighbourhood::Moore,
        }
    }
}

#[pymethods]
impl PyNeighbourhood {
    #[new]
    fn new(neighbourhood: &str) -> PyResult<Self> {
        let n = match Neighbourhood::from_str(neighbourhood) {
            Ok(n) => n,
            Err(_) => {
                return Err(PyErr::new::<exceptions::PyTypeError, _>(
                    "NN or NM options are available",
                ))
            }
        };
        Ok(PyNeighbourhood::from_neighbourhood(n))
    }

    fn __str__(&self) -> String {
        self.to_neighbourhood().to_string()
    }
}
