# rosbag-topic-compare

TODO: Change README after the code

> Determine the topic consistency in a rosbag dataset

This package is a rewriting of [`rosbag-compare`](https://github.com/IamPhytan/rosbag-compare) for rosbags in both ROS1 and ROS2.

## Use case

Say you have a bunch of rosbags inside a folder and you don't know whether or not all those rosbags have the same topics. `rosbag-topic-compare` will :

* retrieve the topics contained in each rosbag
* export a summary of the ros topics in a JSON file
* plot the topics that are missing for each rosbag :

![Summary of missing topics](preview.png)

## Installation

`rosbag-compare` can be installed from PyPi :

```console
$ pip install rosbag-topic-compare
```

Or, if you want the plotting feature:

```console
$ pip install rosbag-topic-compare[plot]
```

## Usage

`rosbag-topic-compare` can be used both as a command line application and in Python code.

### Command line

A basic use of `rosbag-topic-compare` is to simply call it with the path of the folder that contains rosbags. This will simply print out a YAML string with a summary of the comparison.

```console
$ rosbag-topic-compare /path/to/folder/with/rosbags
```

You can also generate a figure that will show what topics are missing in each rosbag with the `--plot/-p` flag. This figure helps when you want to find out if all rosbags in a dataset contains all or some of the expected topics.

```console
$ rosbag-topic-compare -p /path/to/your/rosbag/dataset
```

Here are all the CLI options of `rosbag-topic-compare`:

```console
$ rosbag-topic-compare -h
usage: rosbag-topic-compare [-h] [-m METADATA] [-p] [--fig FIG] bagfolder

positional arguments:
  bagfolder             Dataset directory path

options:
  -h, --help            show this help message and exit
  -m METADATA, --metadata METADATA
                        Metadata summary output path
  -p, --plot            Plotting mode : display a summary plot
  --fig FIG, --summary-figure-path FIG
                        Path for saving a topic consistency figure

```

### Python Code API

You can also call `rosbag-topic-compare` directly into your Python code :

```py
from rosbag_compare import BagTopicComparator

data_path = "/path/to/folder/with/rosbags"
rbag_comp = BagTopicComparator(data_path)

# This step may take time as it open each rosbag separately
# Will show a progress bar
rbag_comp.extract_data()

# Export summary to a JSON file
rbag_comp.export_metadata()  # Defaults to topics_<foldername>.json
rbag_comp.export_metadata("topics.json")
rbag_comp.export_metadata("topics.yaml")

# Generate a figure with the name of the
# missing topics for each rosbag
rbag_comp.plot()                               # Show figure
rbag_comp.plot(img_path="topics_summary.jpg")  # Save figure to path

# Create a new comparator from exported metadata
rbag_comp = BagTopicComparator.from_json("topics.json")
rbag_comp = BagTopicComparator.from_yaml("topics.yaml")
```

## Contributing

Pull requests are welcome and don't hesitate to open issues

(Recommended) [flit](https://flit.pypa.io) is used to package this module. Development packages can be installed using `flit` :

```console
$ python -m venv venv
$ source venv/bin/activate
$ pip install flit
$ flit install
```

(Alternative) Development requirements can be installed using pip :

```console
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements/requirements-dev.txt
```

## Acknowledgements

This package relies strongly on [`rosbags`](https://ternaris.gitlab.io/rosbags) for working with rosbags. Hats off to the team at [Ternaris](https://ternaris.com) for developing and maintaining it.

## License

This project is licensed under a [MIT](LICENSE) license
