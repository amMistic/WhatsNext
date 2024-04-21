# WhatsNext: AI Text Generator

<img src="https://github.com/amMistic/WhatsNext/assets/134824444/68aa4089-da2b-4a24-91fb-dfe0c946118b" alt="AI Text Generator" width="550" height="500">



## Introduction
Welcome to WhatsNext, an AI text generator powered by LSTM models trained on the New York Times comments dataset. This project enables users to generate predictive text based on their input, aiding writers, content creators, and conversational interfaces.

## Setup
### Prerequisites
- Python 3.x
- pip

### Clone Repository
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/your-username/whatsnext.git
```

### Installation
Navigate to the project directory:
```bash
cd whatsnext
```

Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Usage
1. **Prepare Dataset:** Before running the model, prepare your dataset in a CSV format containing text data. You can use the New York Times comments dataset or any other text dataset of your choice.

2. **Train Model:** Use the provided Jupyter notebook or Python script to train the LSTM model on your dataset.

3. **Generate Text:** Once the model is trained, you can use it to generate text by providing a partial sentence or phrase as input.

## Model Details
- **TensorFlow Version:** 2.15.0
- **Model Architecture:** LSTM
- **Vocabulary Size:** 17
- **Embedding Size:** 10
- **LSTM Units:** 256
- **Dropout Rate:** 0.5

## Model Architecture
<img src="https://github.com/amMistic/WhatsNext/assets/134824444/00678e98-08d8-45a0-9fdf-c78cbbfbeb04" alt="Model" width="300" height="700">

## Code and Outputs
### Example Code Snippet
![Example Code](images/code_snippet.png)

### Example Output
![Example Output](images/output.png)

## Dataset Used
The model was trained on the [New York Times comments dataset](https://www.kaggle.com/datasets/aashita/nyt-comments) available on Kaggle.

TODO :
- Add the demo video
- Code Snippets with outputs of each section
  
<!-- ## Demo Video -->
<!-- [![Demo Video](https://img.youtube.com/vi/your-video-id/0.jpg)](https://www.youtube.com/watch?v=your-video-id) -->
