

import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
tf.enable_resource_variables()
tf.enable_eager_execution()
try:
    import t3f
except ImportError:
    # Install T3F if it's not already installed.
    # !git clone https: // github.com/Bihaqo/t3f.git
    # !cd t3f
    # pip install .
    import t3f
