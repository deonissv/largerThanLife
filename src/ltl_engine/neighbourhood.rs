use core::fmt;
use rand::{Rng, RngCore};
use std::cmp::min;
use std::fmt::Formatter;
use std::str::FromStr;

const NEUMANN: &str = "NN";
const MOORE: &str = "NM";

/// The two types of neighbourhoods used in cellular automata.
#[derive(Debug, Clone, PartialEq)]
pub enum Neighbourhood {
    Neumann,
    Moore,
}

impl FromStr for Neighbourhood {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            NEUMANN => Ok(Neighbourhood::Neumann),
            MOORE => Ok(Neighbourhood::Moore),
            _ => Err(()),
        }
    }
}

impl fmt::Display for Neighbourhood {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        match self {
            Neighbourhood::Moore => write!(f, "{}", MOORE),
            Neighbourhood::Neumann => write!(f, "{}", NEUMANN),
        }
    }
}

impl Neighbourhood {
    /// Generates a random neighborhood.
    ///
    /// # Arguments
    ///
    /// * `rng` - A mutable reference to a random number generator implementing the RngCore trait.
    ///
    /// # Returns
    ///
    /// A randomly generated Neighbourhood.
    ///
    pub fn randomize<T: RngCore>(rng: &mut T) -> Self {
        if rng.gen_bool(0.5) {
            Neighbourhood::Moore
        } else {
            Neighbourhood::Neumann
        }
    }

    /// Compute the area of the neighborhood.
    ///
    /// # Arguments
    ///
    /// * `rr` - The radius of the neighborhood.
    /// * `mm` - Is the centre cell included in neighbourhood.
    ///
    /// # Returns
    ///
    /// The area of the neighborhood.
    ///
    pub fn area(&self, rr: u8, mm: u8) -> u16 {
        let area = match self {
            Neighbourhood::Moore => u16::pow((rr * 2 + 1) as u16, 2),
            Neighbourhood::Neumann => u16::pow(rr as u16, 2) + u16::pow((rr + 1) as u16, 2),
        };
        min(if mm == 1 { area } else { area - 1 } as u16, 255)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use rand::rngs::mock::StepRng;
    use std::str::FromStr;

    #[test]
    fn from_str_moore() {
        let n = Neighbourhood::from_str("NM").unwrap();
        assert_eq!(n, Neighbourhood::Moore);
    }

    #[test]
    fn from_str_neumann() {
        let n = Neighbourhood::from_str("NN").unwrap();
        assert_eq!(n, Neighbourhood::Neumann);
    }

    #[test]
    #[should_panic]
    fn from_str_err() {
        assert_eq!(Neighbourhood::from_str("asd"), Err(()));
        Neighbourhood::from_str("asd").unwrap();
    }

    #[test]
    fn moore_to_string() {
        assert_eq!(Neighbourhood::Moore.to_string(), "NM");
    }

    #[test]
    fn neumann_to_string() {
        assert_eq!(Neighbourhood::Neumann.to_string(), "NN");
    }

    #[test]
    fn randomize_moore() {
        let mut rnd = StepRng::new(0, 1);
        assert_eq!(Neighbourhood::randomize(&mut rnd), Neighbourhood::Moore);
    }

    #[test]
    fn randomize_neumann() {
        let mut rnd = StepRng::new(u64::MAX, 1);
        assert_eq!(Neighbourhood::randomize(&mut rnd), Neighbourhood::Neumann);
    }

    #[test]
    fn moore_area_included() {
        let area = Neighbourhood::Moore.area(1, 1);
        assert_eq!(area, 9);
    }

    #[test]
    fn moore_area_excluded() {
        let area = Neighbourhood::Moore.area(1, 0);
        assert_eq!(area, 8);
    }

    #[test]
    fn moore_area_bigger_radius() {
        let area = Neighbourhood::Moore.area(3, 1);
        assert_eq!(area, 49);
    }

    #[test]
    fn neumann_area_included() {
        let area = Neighbourhood::Neumann.area(1, 1);
        assert_eq!(area, 5);
    }

    #[test]
    fn neumann_area_excluded() {
        let area = Neighbourhood::Neumann.area(1, 0);
        assert_eq!(area, 4);
    }

    #[test]
    fn neumann_area_bigger_radius() {
        let area = Neighbourhood::Neumann.area(3, 1);
        assert_eq!(area, 25);
    }
}
