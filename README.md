# turtlecircle

A ROS 2 Python package that commands a turtle in the [turtlesim](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html) simulator to move in a circle. Developed as part of the Barunastra internship program.

---

## Prerequisites
- **ROS 2 Jazzy** installed and sourced
- `turtlesim` package available (`ros-jazzy-turtlesim`)
- Python 3.8+

---

## Installation

1. Clone the repository into your ROS 2 workspace:

```bash
cd ~/ros2_ws/src
git clone https://github.com/Asphyxiale/turtlecirlce.git
```

2. Build the package:

```bash
cd ~/ros2_ws
colcon build --packages-select turtlesimulator
```

3. Source the workspace:

```bash
source ~/ros2_ws/install/setup.bash
```

---

## Usage

Start the turtlesim node and the circle controller together:

```bash
ros2 launch turtlesimulator turtlesimulator_launch.py
```

The turtle will begin drawing a circle in the simulator window.

---

## Package Structure

```
turtlecirlce/
├── launch/                  # Launch files
│   └── turtlesimulator_launch.py
├── resource/                # Package resource marker
├── test/                    # Test files
├── turtlesimulator/         # Python source
│   └── turtlesimulator.py   # Circle controller node
├── package.xml
├── setup.cfg
└── setup.py
```

---

## How It Works

The `turtlesimulator` node publishes velocity commands to the `/turtle1/cmd_vel` topic. By setting a constant linear velocity and a constant angular velocity, the turtle traces a continuous circle in the turtlesim window.

---

## Troubleshooting

**`turtlesim_node` not found**
Install the turtlesim package for your ROS 2 distro:
```bash
sudo apt install ros-jazzy-turtlesim
```

**Package not found after build**
Make sure you have sourced the workspace:
```bash
source ~/ros2_ws/install/setup.bash
```

**No movement visible**
Confirm both nodes are running and check that `/turtle1/cmd_vel` is receiving messages:
```bash
ros2 topic echo /turtle1/cmd_vel
```

---
