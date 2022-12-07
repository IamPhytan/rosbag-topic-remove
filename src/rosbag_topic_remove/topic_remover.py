"""Rosbag Topic Remover : Delete topics from a rosbag"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from rosbags.rosbag1 import Reader as Reader1
from rosbags.rosbag2 import Reader as Reader2
from tqdm import tqdm

import fnmatch

if TYPE_CHECKING:
    from typing import Sequence, Tuple


class BagTopicRemover:
    """Topic remover class to delete some topics from a rosbag"""

    def __init__(self, path: Path | str) -> None:
        self._inbag = Path(path)

    @property
    def inbag(self):
        """The inbag property."""
        return self._inbag

    @inbag.setter
    def inbag(self, value: Path | str):
        """Setter for `inbag`"""
        if Path(value).is_file():
            self._inbag = value
        else:
            raise ValueError(f"{value} is not an existing file")

    @staticmethod
    def filter_out_topics(
        bag_topics: Sequence[str], patterns_to_remove: Sequence[str]
    ) -> Tuple[str]:
        """Filter out topics

        Examples:
        >>> bag_topics = ('/cmd_vel', '/imu/data', '/imu/data_raw', '/imu/odom', '/lidar_packets', '/map', '/velocity')
        >>> to_filter = ('/imu/*', '/lidar_packets')
        >>> BagTopicRemover.filter_out_topics(bag_topics, to_filter)
        ('/cmd_vel', '/map', '/velocity')
        >>> to_filter = ('/cmd_vel', '/map', '/velocity')
        >>> BagTopicRemover.filter_out_topics(bag_topics, to_filter)
        ('/imu/data', '/imu/data_raw', '/imu/odom', '/lidar_packets')
        >>> bag_topics = ('/imu/data', '/imu/data_raw', '/imu/odom')
        >>> to_filter = ('/camera/image_raw')
        >>> BagTopicRemover.filter_out_topics(bag_topics, to_filter)
        ('/imu/data', '/imu/data_raw', '/imu/odom')

        Args:
            bag_topics: input rosbag's topics
            patterns_to_remove: topics to filter out

        Returns:
            tuple: Filtered topics that were not targeted by the pattern
        """
        # Accumulate a list of topics
        topics_to_remove = []
        for pattern in patterns_to_remove:
            pattern_topics = fnmatch.filter(bag_topics, pattern)
            topics_to_remove.extend(pattern_topics)

        # Keep only one copy of each element in the list
        topics_to_remove = tuple(set(topics_to_remove))

        filtered_topics = tuple(
            topic for topic in bag_topics if topic not in topics_to_remove
        )
        return filtered_topics
