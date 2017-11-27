import argparse

from .infocheck import InfoCheck
from .imgcopier import ImageCopier


class Base:
    def __init__(self):
        p = argparse.ArgumentParser(
            description='Extract paintings from WikiArt dataset')

        p.add_argument('--style',
                       type=str,
                       default='',
                       help='Painting style (e.g. realism, baroque)')

        p.add_argument('--genre',
                       type=str,
                       default='',
                       help='Painting genre (e.g. portrait, landscape)')

        p.add_argument('--date',
                       type=str,
                       default='',
                       help='Year that painting was created (e.g. 1960) or range (e.g. 1900,1999)')

        p.add_argument('--in_csv',
                       type=str,
                       default='train_info.csv',
                       help='Location of CSV file')

        p.add_argument('--in_dir',
                       type=str,
                       default='input',
                       help='Directory in which to store paintings')

        p.add_argument('--out_dir',
                       type=str,
                       default='output',
                       help='Directory in which to store paintings')

        p.add_argument('--remove_original',
                       type=bool,
                       default=False,
                       help='Remove image from original directory '
                            'when extracting')

        self.args = p.parse_args()

    def start(self):
        ImageCopier(
            self.args,
            InfoCheck(self.args).list_paintings)


def main():
    Base().start()
    print("Done.")
