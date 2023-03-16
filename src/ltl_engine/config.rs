use crate::ltl_engine::neighbourhood::Neighbourhood;
use rand::{Rng, RngCore, SeedableRng};
use rand_pcg::Pcg32;

/// A struct representing configuration for larger than life game.
#[derive(Debug, Clone, PartialEq)]
pub struct Config {
    pub rr: u8,
    pub cc: u8,
    pub mm: u8,
    pub ss: (u16, u16),
    pub bb: (u16, u16),
    pub nn: Neighbourhood,
}

impl Config {
    /// Creates a new instance of `Config` with the given parameters.
    ///
    /// # Arguments
    ///
    /// * `rr` - The radius of the neighborhood.
    /// * `cc` - The number of cell states.
    /// * `mm` - Is the centre cell included in neighbourhood.
    /// * `ss` - The range of the number of neighbors required for a live cell to survive.
    /// * `bb` - The range of the number of neighbors required for a dead cell to come to life.
    /// * `nn` - The neighborhood type.
    ///
    /// # Returns
    ///
    /// A new instance of `Config` with the given parameters.
    pub fn new(rr: u8, cc: u8, mm: u8, ss: (u16, u16), bb: (u16, u16), nn: Neighbourhood) -> Self {
        Config {
            rr,
            cc,
            mm,
            ss,
            bb,
            nn,
        }
    }

    pub fn randomize(seed: Option<u64>) -> Self {
        match seed {
            None => {
                let rng = rand::thread_rng();
                Self::generate_random_config(rng)
            }
            Some(seed_num) => {
                let rng = Pcg32::seed_from_u64(seed_num);
                Self::generate_random_config(rng)
            }
        }
    }

    /// Randomize the values of all parameters in the config.
    ///
    /// # Arguments
    ///
    /// * `seed` - An optional seed to use when generating random values for the parameters.
    ///
    /// # Returns
    ///
    /// A new instance of `Config` with randomly generated parameters.
    fn generate_random_config<T: RngCore>(mut rng: T) -> Config {
        let rr: u8 = rng.gen_range(1..=10);
        let mm = rng.gen_bool(0.5) as u8;
        let nn = Neighbourhood::randomize(&mut rng);
        let max_neighborhood_count = nn.area(rr, mm);
        let ss_min = rng.gen_range(0..max_neighborhood_count);
        let ss_max = rng.gen_range(ss_min..=max_neighborhood_count);
        let bb_min = rng.gen_range(0..max_neighborhood_count);
        let bb_max = rng.gen_range(bb_min..=max_neighborhood_count);
        Config {
            rr,
            cc: rng.gen_range(1..=25),
            mm,
            ss: (ss_min, ss_max),
            bb: (bb_min, bb_max),
            nn,
        }
    }
}
