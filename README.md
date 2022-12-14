# rosbag-topic-remove

> Filter out topics from a rosbag

## Use case

Say you have too much topics in a rosbag (ROS1 or ROS2) and that you want to keep a copy of this rosbag without data from a specific sensor. `rosbag-topic-remove` will :

* Filter out topics based on their name
* Filter out topics based on [glob](https://en.wikipedia.org/wiki/Glob_(programming))-like wildcard patterns
* Preserve your original rosbag
<!-- * Convert your rosbag from ROS1 to ROS2, if needed -->

## Installation

`rosbag-topic-remove` can be installed from PyPi :

```console
pip install rosbag-topic-remove
```

## Usage

`rosbag-topic-remove` can be used both as a command line application and in Python code.

### Command line

A basic use of `rosbag-topic-remove` is to simply call it from the command line.

```console
rosbag-topic-remove /path/to/rosbag -t /topic/to_delete
rosbag-topic-remove /path/to/rosbag -t *sensor*
```

Here are all the CLI options of `rosbag-topic-remove`:

```console
$ rosbag-topic-remove -h
usage: rosbag-topic-remove [-h] [-o OUTBAG] [-t TOPICS [TOPICS ...]] [-f]
                           inbag

positional arguments:
  inbag                 Input bag

options:
  -h, --help            show this help message and exit
  -o OUTBAG, --output OUTBAG, --outbag OUTBAG
                        Filtered bag
  -t TOPICS [TOPICS ...], --topics TOPICS [TOPICS ...]
                        Topics to remove from the rosbag
  -f, --force           Force output file overwriting

```

### Python Code API

You can also call `rosbag-topic-remove` directly into your Python code :

```py
from rosbag_topic_remove import BagTopicRemover

data_path = "path/to/a/rosbag.bag"  # ROS1
data_path = "path/to/a/rosbag"  # ROS2
rbag_rem = BagTopicRemover(data_path)

# Change the input bag
rbag_rem.inbag = "path/to/another/rosbag"

# Remove /cmd_vel
rbag_rem.remove("/cmd_vel")

# Remove /cmd_vel
rbag_rem.remove("/cmd_vel")

# Remove all camera info topics
rbag_rem.remove("/*/camera_info")

# Remove all topics from the IMU and from the GPS
rbag_rem.remove(("/imu/*", "/gps/*"))

# Export a rosbag with all topics filtered
rbag_rem.export("path/to/save/this/filtered/rosbag.bag")  # ROS1
rbag_rem.export("path/to/save/that/filtered/rosbag")  # ROS2
```

## Contributing

Pull requests are welcome and don't hesitate to open issues

(Recommended) [flit](https://flit.pypa.io) is used to package this module. Development packages can be installed using `flit` :

```console
python -m venv venv
source venv/bin/activate
pip install flit
flit install
```

(Alternative) Development requirements can be installed using pip :

```console
python -m venv venv
source venv/bin/activate
pip install -r requirements/requirements-dev.txt
```

## Acknowledgements

This package relies strongly on [`rosbags`](https://ternaris.gitlab.io/rosbags) for working with rosbags. Hats off to the team at [Ternaris](https://ternaris.com) for developing and maintaining it.

## License

This project is licensed under a [MIT](LICENSE) license
