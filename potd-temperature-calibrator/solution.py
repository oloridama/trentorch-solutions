import numpy as np


def temperature_calibrator(z: np.ndarray, tau: float) -> np.ndarray:
    """
    z: logits.
    tau: temperature, tau > 0.

    p = softmax(z / tau), using an overflow-safe softmax (subtract the
    max before exponentiating). Divide by tau, never multiply.

    Return p.
    """
    # TODO: scale by dividing, then stable softmax.
    scaled_z = z / tau
    max_val = np.max(scaled_z)
    exp_z = np.exp(scaled_z - max_val)
    p =  exp_z / np.sum(exp_z)
    return p
