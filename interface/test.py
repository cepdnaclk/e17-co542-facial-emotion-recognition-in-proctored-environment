from flask import Flask, jsonify
# from google.cloud import storage
import joblib
import os
import numpy as np

DEFAULT_INPUT = np.random.rand(20)

print(DEFAULT_INPUT)