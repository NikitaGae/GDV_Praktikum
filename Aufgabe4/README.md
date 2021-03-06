# GDV-SoSe2022 - Assignment 4

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#how-to-use">How to use</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

As part of the course "Grafische Datenverarbeitung" in the summer term 2022 at HS-Furtwangen we are asked to write our own projects in Python via Visual Studio Code.  


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started


### Prerequisites
Before using our project, please make sure you have downloaded and installed all the following software:
* Python 3 (version 3.10.2) from [python.org](https://www.python.org/downloads/)
* pip (version 19.3 or newer) from https://pip.pypa.io/en/stable/installation/
* OpenCV (version 4.5.5.62 or newer) as explained on https://pypi.org/project/opencv-python/
 

<!-- USAGE EXAMPLES -->
## Usage

Our program creates a mosaic from a selected image. To create the mosaic, the selected image is divided into several small squares. For each of these small squares, the "Best Match" is then found from a database. At the end, all "Best Matches" are merged back into one image and create a mosaic. 


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- HOWTOUSE -->
## How to use

1. Open file "aufgabe4.py" with the editor of your choice.
2. Download the Database [Caltech-101 image data set](https://data.caltech.edu/records/20086) and import it into the folder "data". Please check if your path in line 54 is accurate.
3. Read an Image you want to make a Mosaic of in line 64/65
4. Set the file name to the name you want to safe the file with in line 29
5. Run with Python.
6. To end the window press "q". 


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Fynn Janke - fynn.janke@hs-furtwangen.de</br>
Nikita G??rtner - nikita.gaertner@hs-furtwangen.de</br>
Vivien Sch??llkopf - vivien.christin.schoellkopf@hs-furtwangen.de


<p align="right">(<a href="#top">back to top</a>)</p>
