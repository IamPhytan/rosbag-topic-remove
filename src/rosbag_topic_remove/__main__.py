"""Rosbag topic remover

Remove topics from rosbags

Usage:
------

 $ rosbag-topic-remove INBAG [OPTIONS]

Remove topics from INBAG.bag,
    save the resulting rosbag in INBAG_filt.bag:

 $ rosbag-topic-compare INBAG.bag --topics /topic_to_remove
 $ rosbag-topic-compare INBAG.bag -t /camera*/*_raw /imu/*

Remove topics from INBAG.bag,
    save in OUTBAG.bag:

 $ rosbag-topic-compare INBAG.bag -o OUTBAG.bag --topics /cmd_vel
 $ rosbag-topic-compare INBAG.bag -o OUTBAG.bag -t /gps/*

Available options are:

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output bag
  -t TOPICS, --metadata METADATA
                        Metadata summary output path
  -p, --plot            Plotting mode : display a summary plot
  --fig FIG, --summary-figure-path FIG
                        Path for saving a topic consistency figure

Version:
--------

- rosbag-topic-remove v0.0.0
"""
from __future__ import annotations

import argparse
from pathlib import Path

from . import utils as u
from .topic_remover import BagTopicRemover
