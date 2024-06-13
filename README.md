# Self-Driving-Car-Neutral-Network
<a name="readme-top"></a>

## Demo 
<details>
  <summary>View here</summary>
<table>
  <tr>
    <td align="center">
      <img src="https://i.imgur.com/jLlW6VD.png" width="350" height="900" /><br>
      <code>Detect traffic signs</code>
    </td>
    <td  align="center">
      <img src="https://i.makeagif.com/media/6-12-2024/53seC4.gif" alt="GIF Image" class="gif-image" width="450">
      <br>
      <code>Run</code>
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <img src="https://i.makeagif.com/media/6-12-2024/Ypqbhc.gif" width="800"  /><br>
      <code>Obstacle</code>
    </td>
    
  </tr>
</table>


</details>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#built-with">Built With</a>
      <ul>
        <li><a href="#framework-and-library">Framework and library</a></li>
        <li><a href="#hardware">Hardware</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#step1-dataCollection">Step1 DataCollection</a></li>
        <li><a href="#step2-LabelData">Step2 LabelData</a></li>
        <li><a href="#step3-training">Step3 Training</a></li>
      </ul>
    </li>
    <li><a href="#reference-documents">Reference documents</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This project uses the deep learning convolutional neural network <b>U-Net-LSTM</b> to help cars recognize their lane along with <b>YOLOv8</b> to identify signs and vehicle owners.By using <b>U-Net-LSTM</b> the car can identify and draw lanes accurately in up to 96% of labeled images. Something that image processing is almost impossible to do, especially with images with many curves. With this method, vehicles can even drive on lanes without lane markings as long as they are clearly labeled.
<div  >
  <img   src="https://i.imgur.com/XvwQgE8.png" width="900"/><br>
</div>

## Built With

### Framework and library

* Pytorch
* Python
* Opencv
* Pyfirmata
* Socket

### Hardware

<table>
<!-- row 2 -->
  <tr>
    <td align="center">
      <img src="https://i.imgur.com/pNezTwx.png"  width="450" height= "450"/><br>
      <code> Raspberry pi zero 2 w</code>
    </td>
    <td align="center">
      <img src="https://i.imgur.com/zIRz3nN.png" alt="gradient-markdown-logo" width="450" height= "450"/><br>
      <code> Camera 5MP v1.3cho Raspberry Pi</code>
    </td>
  </tr>
  <!-- row 1 -->
  <tr>
    <td colspan="2" align="center">
      <img src="https://i.imgur.com/4OPxFpN.jpeg" alt="default-header" width="900"/><br>
      <code> Other </code>
    </td>
  </tr>
  
</table>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

### Step1 DataCollection
* Run main.py to collect lane data as seen by the vehicle through the camera. Below is a link to the dataset used in the project
* Lane data: <a href="https://drive.google.com/file/d/1GKYfGK38hvXVCX6oazzpI21_XqZrIMYk/view?usp=sharing">Link</a> 

### Step2 LabelData
* Run main.py to label the newly collected data
* Watch the <a href="https://www.youtube.com/watch?v=wuZtUMEiKWY">video</a> to label data and training an object recognition model using yolov8
* My traffic sign dataset: <a href="https://universe.roboflow.com/object-detection-9zsot/detect-traffic-sign-3or9q">Link </a>

### Step3 Training
* Run train.py with your new dataset
* You can use my dataset by downloading <a href="https://drive.google.com/file/d/18v-cEUSF5dV9o1QiKWcoKiYGNQdjvOPW/view?usp=drive_link">here </a> and replace folder with the same name
### Step4 Predict
* Run predict.py to see how the model can recognize the lane
* Run server.py in your laptop 
* Run client.py in CodeInCar dicrectory
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Reference documents
Sincere thanks to the team who wrote this <a href="https://arxiv.org/pdf/1903.02193">paper </a>. This research has been very helpful in creating this project
<p align="right">(<a href="#readme-top">back to top</a>)</p>