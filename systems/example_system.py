from canonada.system import System

# Import the pipelines from pipelines/example_pipelines.py
import pipelines.example_pipelines as example_pipelines


# Define the pipeline system equivalent to `canonada run pipelines streaming_pipe calculate_better_stats`
example_system = System(
    name="example_system",
    pipelines=[
        example_pipelines.streaming_pipe,
        example_pipelines.calculate_better_stats,
    ],
    description="This system runs the example pipelines sequentially. First `streaming_pipe` and then `calculate_better_stats`.",
)
