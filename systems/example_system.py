import sys
from canonada.system import System

# Import the pipelines from pipelines/example_pipelines.py
sys.path.append("../pipelines")
from pipelines import example_pipelines


# Define the pipeline system equivalent to `canonada run pipelines streaming_pipe streaming_pipe`
example_system = System(
    name="example_system",
    pipelines=[
        example_pipelines.streaming_pipe,
        example_pipelines.calculate_better_stats,
    ],
    description="This system runs the example pipelines sequentially. First `streaming_pipe` and then `calculate_better_stats`.",
)
