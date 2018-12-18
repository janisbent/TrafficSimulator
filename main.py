import argparse
from simulator.simulator import Simulator

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--nlanes", default=1, help="Number of lanes")
    parser.add_argument("--ncars", default=1, help="Number of cars")
    return parser.parse_args()


def main():
    sim = Simulator(parse_args())
    sim.setup()
    sim.run()


if __name__ == "__main__":
    main()
