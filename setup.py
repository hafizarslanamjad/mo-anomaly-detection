from setuptools import setup, find_packages

setup(
    name="mo-anomaly-detection",
    version="0.1.0",
    author="Hafiz Arslan Amjad",
    author_email="hafizarslanamjad47@gmail.com",
    description="An anomaly detection project using deep learning and PyTorch",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hafizarslanamjad/mo-anomaly-detection",
    packages=find_packages(exclude=("checkpoints", "dataset", "venv")),
    install_requires=[
        "numpy",
        "torch==2.4.1+cu121",      # Specify the exact Torch version with CUDA support
        "torchvision==0.19.1+cu121", # Specify the exact Torchvision version with CUDA support
        "Pillow",                    # Required for image processing
        "matplotlib",                # For plotting
        "tqdm",                      # For progress bars
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
