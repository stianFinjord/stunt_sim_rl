import omni.isaac.core.utils.stage as stage_utils
import omni.isaac.core.utils.prims as prim_utils
from omni.isaac.core.robots import Robot
from omni.isaac.core.utils.nucleus import get_assets_root_path
from omni.isaac.core.utils.stage import add_reference_to_stage
from omni.isaac.core.simulation_context import SimulationContext
import numpy as np

def main():
    # Initialize the simulation context
    simulation_context = SimulationContext(physics_dt=0.01, rendering_dt=0.01, backend="torch")

    # Get assets root path
    assets_root_path = get_assets_root_path()

    # Add a simple robot to the stage
    robot_prim_path = "/World/Robot"
    usd_path = assets_root_path + "/Isaac/Robots/Franka/franka.usd"
    add_reference_to_stage(usd_path=usd_path, prim_path=robot_prim_path)

    # Load the robot
    robot = Robot(
        prim_path=robot_prim_path,
        name="franka",
        position=np.array([0, 0, 0]),
        orientation=np.array([1, 0, 0, 0])
    )

    # Play the simulation
    simulation_context.play()

    # Run the simulation for a few seconds
    for _ in range(100):
        simulation_context.step()

    # Stop the simulation
    simulation_context.stop()

    print("Simulation completed successfully!")

if __name__ == "__main__":
    main()