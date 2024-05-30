## Office-Sitting-Posture-Detecting

This is a software that can detect the sitting posture of a person, especially in the office.

We referred to the code from "https://github.com/nvinayvarma189/Sitting-Posture-Recognition" as a basis to extend.

The external vibrator product we use is from "https://www.adafruit.com/product/2305#description".

The results can output the processing time, leg status, hand status, back status, current posture status, percentage, and remind sentence.

If person sits a bad posture, the external vibrator will remind you.

## Files
`Sitting-Posture-Recognition-master/model.py` - contains architecture of the model.

`Sitting-Posture-Recognition-master/config_reader.py` - contains the parameters that are essential for the model to predict the key points. Keeping the specifications of the system in mind.

`Sitting-Posture-Recognition-master/util.py` - some functions required to calculate the co-ordinates of the key points.

`test.py` - Connecting the external vibrator that if "bad posture", it will remind people to adjust.

### Usage 

1. Please install all the requirements from `Sitting-Posture-Recognition-master/requirements.txt`.
2. Run `Sitting-Posture-Recognition-master/posture_realtime.py` for testing it in real time. Please sit sufficiently far away from the system showing your lateral view. The position of the camera should preferably be on the side of the person. Please note that this will require a system with atleast 8GB RAM. On a 4 GB RAM, the output is not at all smooth and the output lags very much from the input frame.
3. If you do not have the external vibrator, comment out lines 10 and 262 of `Sitting-Posture-Recognition-master/posture_realtime.py` so that the system won't run the `test.py`.

**NOTE**: The repository's files come from the code sources referenced above. We have not used all of them. We only used the “real time” part and added the vibrator peripheral, modified some of the function parameters and output results and their judgments.

Now the code is still in continuous development. All the parameters for recognizing the sitting posture can be modified to enable it to be adapted to different venues, maintaining the accuracy of the recognition.
