# OpenCVProject
This is a working OpenCV project developed with my team members.

Directions for use:

1.	First step is to add images to train OpenCV in the Resources Folder name these folders starting from 0 to how many people’s faces you want to train the app. For example, if I want to train OpenCV to recognize two faces I will name the Folders with the pictures of each person 0 and 1.

2.	Now go to the Webcam_Recognizing.py and add the names of the people you added to the name array and number it with the number you named the folder. For example if you named the folder for the person named John with 0, then type 0: “John”.

3.	Uncomment the code, which will create a .yml file which contains the vector information of all faces.

4.	Comment the line, which reads this .yml file to recognize faces after you train OpenCV.

5.	Now save this file.

6.	First time you run the app, you must train the app to recognize the faces.

7.	Open File Explorer and navigate manually or navigate using cd commands with PowerShell terminal to the folder where Webcam_Recognizing.py file is located.

8.	Now type python followed by a space and type Webcam_Recognizing.py then press enter. 

9.	It will train the faces, which will take a while depending on the resolution of photos. (Larger the photo resolution the better).

10.	Now press ‘s’ key on keyboard to stop the execution of the app following which all windows will close.

11.	Comment the line, which trains the app for the first time and uncomment the lines, which reads from the .yml file.


