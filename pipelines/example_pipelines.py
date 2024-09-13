# Import the Canonada Classes
from canonada.pipeline import Node, Pipeline

# Import the nodes from pipelines/nodes/example_nodes.py 
from .nodes import example_nodes

# Simple pipeline
streaming_pipe = Pipeline("streaming_pipe", [
        # Read each signal from the catalog and add an offset defined in the parameters
        Node(
            func=example_nodes.add_offset, 
            input=["raw_signals", "params:section_1.offset"], # Load raw_signals from the catalog and the offset from the parameters
            output=["offset_signals"], # If not declared in the catalog, the output is saved in memory and passed onwards
            name="create_offsets",
            description="Adds parametrized offset to the signals"
            ),
        # Save the previous output to disk with a dummy module
        Node(
            func=lambda x: x, # Just pass the input to the output
            input=["offset_signals"],
            output=["offset_signals_catalog"],
            name="save_offsets",
            description="Saves the offset signals using the datahandler specified in the catalog"
        ),
        # Calculate the maximum value of each signal
        Node(
            func=example_nodes.get_signal_max,
            input=["offset_signals"],
            output=["max_values"],
            name="get_signal_max",
            description="Calculates the maximum value of the signals"
        ),
        # Calculate the mean value of each signal
        Node(
            func=example_nodes.calculate_mean,
            input=["offset_signals"],
            output=["mean_values"],
            name="calculate_mean",
            description="Calculates the mean value of the signals"
        ),
        # Save the stats of the signals in a CSV file
        Node(
            func=example_nodes.list_stats,
            input=["offset_signals", "max_values", "mean_values"],
            output=["stats"], # It will be saved in the defined file in the catalog
            name="list_stats",
            description="Returns the stats of the signals"
        )
    ],
    description="This pipeline reads signals from the catalog, adds an offset, calculates the maximum and mean values, and saves the stats to disk"
)
streaming_pipe.max_workers = 50 # You can optionally set the maximum number of workers running concurrently (by default uses as many workers as cores in the machine)

# Pipeline that joins two catalog entries
calculate_better_stats = Pipeline("calculate_better_stats", [
        Node(
            func=example_nodes.calculate_better_stats,
            input=["offset_signals_catalog", "stats"],
            output=["better_stats"], # It will be saved in the defined file in the catalog
            name="calculate_better_stats",
            description="Calculates better stats using the offset signals and the stats, and save data to disk"
        ),
    ],
    description="This pipeline joins two catalog ensuring they match and calculates better stats"
)