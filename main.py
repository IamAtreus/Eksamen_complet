# This script made by Lars Enøe Atreus. UCL Vejle, 4. Semester, 2022
# This script used to train a model to predict faults in Photovoltaic panels.


import torch
import torch.nn as nn
import os
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

