"""Rosbag topic remover

Remove topics from rosbags

Usage:
------

 $ rosbag-topic-remove INBAG [OPTIONS]

Remove topics from INBAG.bag,
    save the resulting rosbag in INBAG_filt.bag:

 $ rosbag-topic-remove INBAG.bag --topics /topic_to_remove
 $ rosbag-topic-remove INBAG.bag -t /camera*/*_raw /imu/*

Remove topics from INBAG.bag,
    save in OUTBAG.bag:

 $ rosbag-topic-remove INBAG.bag -o OUTBAG.bag --topics /cmd_vel
 $ rosbag-topic-remove INBAG.bag -o OUTBAG.bag -t /gps/*

Available options are:

options:
  -h, --help            show this help message and exit
  -o OUTBAG, --output OUTBAG, --outbag OUTBAG
                        Filtered bag
  -t TOPICS [TOPICS ...], --topics TOPICS [TOPICS ...]
                        Topics to remove from the rosbag
  -f, --force           Force output file overwriting

Version:
--------

- rosbag-topic-remove v0.0.2
"""
from __future__ import annotations

import argparse
from pathlib import Path

from . import utils as u
from .topic_remover import BagTopicRemover


def parse_arguments():
    """Parse rosbag-topic-remove arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "inbag",
        type=u.path_type(),
        help="Input bag",
    )
    parser.add_argument(
        "-o",
        "--output",
        "--outbag",
        dest="outbag",
        help="Filtered bag",
    )
    parser.add_argument(
        "-t",
        "--topics",
        type=str,
        nargs="+",
        help="Topics to remove from the rosbag",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Force output file overwriting",
    )
    return parser.parse_args()


def main():
    """Main function"""
    args = parse_arguments()
    inpath = args.inbag
    outpath = args.outbag

    rosbag_rem = BagTopicRemover(inpath)
    rosbag_rem.remove(args.topics)
    if outpath:
        rosbag_rem.export(outpath, force_out=args.force)
    else:
        # Default path:
        # /path/to/my/rosbag => /path/to/my/rosbag_filt
        # /path/to/my/rosbag.bag => /path/to/my/rosbag_filt.bag
        inpath = Path(inpath)
        def_outfile = f"{inpath.stem}_filt{inpath.suffix}"
        default_outpath = inpath.parent / def_outfile
        rosbag_rem.export(default_outpath, force_out=args.force)


if __name__ == "__main__":
    main()
