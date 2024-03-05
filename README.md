# Fingerprint_Security-Voice_code-Access-Task

## Overview
This Python desktop application utilizes voice fingerprint and spectrogram technology to identify individuals based on their unique vocal characteristics. The system can be trained on up to 8 individuals and operates in two distinct modes to ensure secure access.

## Features
- **Mode 1 – Security Voice Code**
  - Access is granted only if the user speaks a specific pass-code sentence.
   ![WhatsApp Image 2024-03-05 at 10 21 18 AM](https://github.com/salsabilmostafa/Fingerprint_Security-Voice_code-Access-Task/assets/115428975/8cf2836d-27c8-4665-9228-2846291c16a4)


- **Mode 2 – Security Voice Fingerprint**
  - Access is granted to the selected individual who say the valid pass-code sentence.
   ![WhatsApp Image 2024-03-05 at 10 25 27 AM](https://github.com/salsabilmostafa/Fingerprint_Security-Voice_code-Access-Task/assets/115428975/0b581bcd-d226-4ab6-a7e5-c8333364b4c7)

The program calculates matching probabilities and decides whether access should be granted or denied based on the input.


## Usage
1. Clone the repository.
    ```bash
    git clone https://github.com/salsabilmostafa/Fingerprint_Security-Voice_code-Access-Task.git
    ```
2. Add the datasets of 8 different people to the project folder then check for any needed adjustments in the code
   
3. Run the application.
    ```bash
    python Security_Voice_FP.py
    ```

## Dependencies
Ensure you have the following dependencies installed before running the application:
- Python 3.7 or above
- PyQt5
- Matplotlib
- Sounddevice
- Librosa
- Numpy
- os
- sklearn
- scipy
- random

## Contributions
Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.
