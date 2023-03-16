use pyo3::prelude::*;

use crate::ltl_engine::board::Board;
use crate::py_config::PyConfig;

#[pyclass]
#[derive(Debug, PartialEq)]
pub struct PyBoard {
    pub board: Board,
}

#[pymethods]
impl PyBoard {
    #[new]
    fn new(size: u64, config: &PyConfig) -> Self {
        PyBoard {
            board: Board::new(size, config.config.clone()),
        }
    }

    #[getter]
    fn board(&self) -> PyObject {
        Python::with_gil(|py| {
            self.board.cells.to_object(py)
        })
    }

    fn reset(&mut self) -> () {
        self.board.reset();
    }

    fn get_cell(&self, x: usize, y: usize) -> PyObject {
       Python::with_gil(|py| {
            self.board.get_cell(x, y).to_object(py)
        })
    }

    fn set_cell(&mut self, x: usize, y: usize, value: u8) -> () {
        self.board.set_cell(x, y, value);
    }

    fn randomize(&mut self, seed: Option<u64>) -> () {
        self.board.randomize(seed)
    }

    fn cell_up(&mut self, x: usize, y: usize) -> () {
        self.board.cell_up(x, y)
    }

    fn cell_down(&mut self, x: usize, y: usize) -> () {
        self.board.cell_down(x, y)
    }

    fn update(&mut self) -> () {
        self.board.update()
    }
}
