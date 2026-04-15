🧠 Kidney Stone Detection Using CNN on Ultrasound Images

📌 Introduction

Kidney stone disease is one of the most common urological disorders worldwide. It occurs when solid deposits of minerals and salts form in the kidneys, leading to pain, infection, or even kidney damage.

Early detection is very important for effective treatment. Ultrasound imaging is widely used because it is:

Non-invasive
Low-cost
Radiation-free

However, manual analysis of ultrasound images depends on expert doctors and may lead to human error.

This project uses a Convolutional Neural Network (CNN) to automatically classify kidney ultrasound images into:

Normal
Stone
📚 Literature Review

Previous research supports the use of deep learning in medical imaging:

Chen et al. (2020): Achieved 90%+ accuracy using CNN on CT images
Hussein et al. (2021): Used transfer learning (VGG16, ResNet) for ultrasound images
Mishra et al. (2022): Improved accuracy using CNN on small datasets

These studies show that CNN models are highly effective for medical image classification.

📊 Dataset Overview
Source: Mendeley Data – Kidney Ultrasound Images
Total Images: 9,416
Normal: 4,414
Stone: 5,002
Data Split:
Training: 80%
Validation: 10%
Testing: 10%
Image Size: 150 × 150 pixels
🏗️ Model Architecture

The CNN model consists of:

4 Convolutional Layers (ReLU activation)
MaxPooling after each convolution layer
Flatten Layer
Dense Layer (512 neurons)
Output Layer (Sigmoid for binary classification)
⚙️ Training Configuration
Optimizer: RMSprop
Loss Function: Binary Crossentropy
Epochs: 10–30
Batch Size: 20
Image Scaling: 1./255
📈 Results
Training Accuracy: ~100%
Validation Accuracy: ~99%
Testing Accuracy: ~98–99%
📉 Performance Graphs
Training vs Validation Accuracy
Training vs Validation Loss
✅ Conclusion

This project demonstrates that a CNN model can accurately classify kidney ultrasound images.

🔑 Key Takeaways
Achieved ~99% validation accuracy
Lightweight and fast model
Requires minimal preprocessing
Can be integrated into:
Medical diagnostic systems
Mobile healthcare applications
🚀 Future Work
Use larger and more diverse datasets
Apply transfer learning (e.g., ResNet, VGG16)
Deploy model as a web or mobile application
Improve real-time prediction performance
🛠️ Technologies Used
Python
TensorFlow / Keras
NumPy
Matplotlib
📬 Contact

Shahzad Ali
📧 Shahzaadali839@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/shahzadali007/
