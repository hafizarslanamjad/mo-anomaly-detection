
# mo-anomaly-detection

An anomaly detection project using deep learning and PyTorch, designed to identify irregularities in images. This model uses a convolutional autoencoder with attention mechanisms to improve anomaly detection accuracy.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Training](#training)
  - [Testing](#testing)
  - [Inference](#inference)
- [Project Structure](#project-structure)
- [Features](#features)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Requirements
- Python >= 3.6
- PyTorch == 2.4.1+cu121
- Torchvision == 0.19.1+cu121
- CUDA 12.1 (for GPU support)

### Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/hafizarslanamjad/mo-anomaly-detection.git
   cd mo-anomaly-detection
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install PyTorch with CUDA support (if required)**:
   ```bash
   pip install torch==2.4.1+cu121 torchvision==0.19.1+cu121 --extra-index-url https://download.pytorch.org/whl/cu121
   ```

## Usage

### Training
To train the anomaly detection model, run:
```bash
python train.py --config configs/train_config.yaml
```

### Testing
To evaluate the model on the test set:
```bash
python test.py --config configs/test_config.yaml
```

### Inference
To perform anomaly detection on new images:
```bash
python inference.py --input /path/to/image
```

> **Note**: Adjust paths as needed, and make sure the images follow the directory structure specified in the configuration files.

## Project Structure

```
mo-anomaly-detection/
├── checkpoints/       # Model checkpoints
├── dataset/           # Training/testing data
├── models/            # Model architectures
├── utils/             # Helper functions
├── venv/              # Virtual environment (not included in Git)
├── train.py           # Training script
├── test.py            # Testing script
├── inference.py       # Inference script
├── configs/           # Configuration files
└── README.md          # Project documentation
```

## Features
- Convolutional Autoencoder with Attention Mechanisms
- Custom dataset processing for anomaly detection
- Configurable training, testing, and inference pipelines

## Results
The model achieves high accuracy in anomaly detection. Below are sample results:

![Sample Output](path/to/sample_output.png)

- **Accuracy**: 95%
- **F1 Score**: 0.92

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.