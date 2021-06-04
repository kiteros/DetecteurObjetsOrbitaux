import argparse

parser = argparse.ArgumentParser(description='Satellite Streaks Detection')

parser.add_argument('--i', type=str)
parser.add_argument('--h', type=str)
parser.add_argument('--o', type = str)
parser.add_argument('--n', type = int, default = 1)
parser.add_argument('--hough', type = int, default = 200)
parser.add_argument('--param', type = str)
parser.add_argument('--folder', type = str)
parser.add_argument('--listimg', type = str)
parser.set_defaults(load_lines=False)
parser.set_defaults(save_lines=True)

args = parser.parse_args()

def get_args():
    return args