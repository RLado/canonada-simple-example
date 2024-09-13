"""
Example nodes for the pipeline (this modules do not need to be in a specific directory)
"""

def add_offset(signal: dict, offset: float) -> dict:
    """
    Adds a given offset to a signal

    Args:
        signal (dict): A dictionary with the signal values
        offset (float): The offset to add to the signal

    Returns:
        dict: A dictionary with the signal values plus the offset
    """

    signal["signal"] = [value + offset for value in signal["signal"]]
    return signal
    
def get_signal_max(signal: dict) -> float:
    """
    Returns the maximum value of a signal

    Args:
        signal (dict): A dictionary with the signal values

    Returns:
        float: The maximum value of the signal
    """

    return max(signal["signal"])

def calculate_mean(signal: dict) -> float:
    """
    Returns the mean value of a signal

    Args:
        signal (dict): A dictionary with the signal values

    Returns:
        float: The mean value of the signal
    """

    return sum(signal["signal"]) / len(signal["signal"])

def list_stats(signals: dict, maximum: float, mean: float)->dict:
    """
    Returns a dictionary with the stats of the signals

    Args:
        signals (dict): A dictionary with the signals
        maximum (float): The maximum value of the signals
        mean (float): The mean value of the signals

    Returns:
        dict: A dictionary with the stats of the signals
    """

    return {
        "id": signals["id"],
        "maximum": maximum,
        "mean": mean,
    }
    
def calculate_better_stats(signal: dict, stats: dict) -> dict:
    """
    Returns a dictionary with the stats of the signals

    Args:
        signal (dict): A dictionary with the signal values
        stats (dict): A dictionary with the stats of the signals

    Returns:
        dict: A dictionary with the stats of the signals
    """
    assert signal["id"] == stats["id"], "Canonada will ensure that catalog keys match. If this assertion fails, blame Canonada." # Always True

    return {
        "id": signal["id"],
        "length": len(signal["signal"]),
        "resolution": signal["signal"][1] - signal["signal"][0],
        "maximum": stats["maximum"],
        "mean": stats["mean"],
    }