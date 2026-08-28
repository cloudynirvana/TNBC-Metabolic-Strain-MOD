"""Google Colab setup helpers for TNBC-Metabolic-Strain-MOD.

Run the bootstrap cell in Colab, then use the helpers below to clone/sync
this repository and report the active accelerator.
"""

from pathlib import Path
import os
import subprocess
import sys

REPO_URL = "https://github.com/cloudynirvana/TNBC-Metabolic-Strain-MOD.git"
REPO_DIR = Path("/content/TNBC-Metabolic-Strain-MOD")


def run(cmd):
    print("$", " ".join(cmd))
    return subprocess.run(cmd, check=True, text=True)


def setup_repo():
    if REPO_DIR.exists():
        run(["git", "-C", str(REPO_DIR), "pull", "--ff-only"])
    else:
        run(["git", "clone", REPO_URL, str(REPO_DIR)])
    run([sys.executable, "-m", "pip", "install", "-q", "-r", str(REPO_DIR / "requirements-colab.txt")])
    print(f"Repository ready: {REPO_DIR}")
    return REPO_DIR


def accelerator_report():
    try:
        import torch
        print("PyTorch:", torch.__version__)
        print("CUDA available:", torch.cuda.is_available())
        if torch.cuda.is_available():
            print("GPU:", torch.cuda.get_device_name(0))
            print("CUDA:", torch.version.cuda)
    except ImportError:
        print("PyTorch is not installed; NumPy/SciPy CPU workflows remain available.")

    try:
        import tensorflow as tf
        print("TensorFlow GPUs:", tf.config.list_physical_devices("GPU"))
    except ImportError:
        pass

    print("COLAB_GPU:", os.environ.get("COLAB_GPU", "not set"))
