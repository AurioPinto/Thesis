# Bachelor Thesis

![Tongji logo](./Imgs/TJ.png)

---

Title

- ML-Based Image Enhancement of Low-Quality QR Code Images for Fast Data Decoding

# Aims

The current research aim is to construct a fast system to enhance the quality of QR Code images to improve the
decoding success rate, hence decreasing the time required to read the data contained in 2D bar
codes. The system is an Convolutional Neural Network (CNN) with a structure of an auto-encoder,
trained with a TensorFlow toolkit on self-generated images. The input is an image with a poor
resolution and quality and the output is a clear, noise-less picture of the same QR Code. The output of
the CNN can then be used to decode the QR Code’s data with any preferred decoding algorithm.
The system has been deployed on the Raspberry Pi 3B+ and evaluated in different simulation
obtaining an increase of about +100% success rate of correct decoding of low-quality QR Code
images.

|       System        |                                                                 2.7                                                                 |                                                                                                                 3.5                                                                                                                 |                                                                                                 3.6                                                                                                 |
| :-----------------: | :---------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|      Linux CPU      | [![Build Status](https://ci.pytorch.org/jenkins/job/pytorch-master/badge/icon)](https://ci.pytorch.org/jenkins/job/pytorch-master/) |                                                 [![Build Status](https://ci.pytorch.org/jenkins/job/pytorch-master/badge/icon)](https://ci.pytorch.org/jenkins/job/pytorch-master/)                                                 |                                                                                         <center>—</center>                                                                                          |
|      Linux GPU      | [![Build Status](https://ci.pytorch.org/jenkins/job/pytorch-master/badge/icon)](https://ci.pytorch.org/jenkins/job/pytorch-master/) |                                                 [![Build Status](https://ci.pytorch.org/jenkins/job/pytorch-master/badge/icon)](https://ci.pytorch.org/jenkins/job/pytorch-master/)                                                 |                                                                                         <center>—</center>                                                                                          |
|  Windows CPU / GPU  |                                                         <center>—</center>                                                          | [![Build Status](https://ci.pytorch.org/jenkins/job/pytorch-builds/job/pytorch-win-ws2016-cuda9-cudnn7-py3-trigger/badge/icon)](https://ci.pytorch.org/jenkins/job/pytorch-builds/job/pytorch-win-ws2016-cuda9-cudnn7-py3-trigger/) |                                                                                         <center>—</center>                                                                                          |
| Linux (ppc64le) CPU |                                                         <center>—</center>                                                          |                                                                                                         <center>—</center>                                                                                                          |           [![Build Status](https://powerci.osuosl.org/job/pytorch-master-nightly-py3-linux-ppc64le/badge/icon)](https://powerci.osuosl.org/job/pytorch-master-nightly-py3-linux-ppc64le/)           |
| Linux (ppc64le) GPU |                                                         <center>—</center>                                                          |                                                                                                         <center>—</center>                                                                                                          | [![Build Status](https://powerci.osuosl.org/job/pytorch-linux-cuda92-cudnn7-py3-mpi-build-test-gpu/badge/icon)](https://powerci.osuosl.org/job/pytorch-linux-cuda92-cudnn7-py3-mpi-build-test-gpu/) |

---

### Image Enhancement

- Image De-Blur and Enhancement

![](./Imgs/Enhance.png)

# Convolutional neural network Model

- The enhancer developed is based on a Convolutional Neural Network or in short CNN, trained
  from zero and built on a structure usually referred as auto-encoder. CNNs are particular kinds of
  Neural Networks (NN) which simulate the convolution operation. The convolution I\*K between an
  input matrix I and another matrix, the kernel or filter, K is obtained by translate pixel-by-pixel the
  kernel

![CNN model](./Imgs/CNN.png)
