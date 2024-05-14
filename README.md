## Office-Sitting-Posture-Detecting

This is a software that can detect the sitting position of a person in the office.

We used the code from "https://github.com/nvinayvarma189/Sitting-Posture-Recognition" as a basis to extend.

The output can tell you how a person sits, including back posture, arm posture, and leg posture, and outputs (analyse/evaluate) whether the person's sitting posture is “bad posture” or not.

## Files
`Sitting-Posture-Recognition-master/model.py` - contains architecture of the model.

`Sitting-Posture-Recognition-master/config_reader.py` - contains the parameters that are essential for the model to predict the key points. Keeping the specifications of the system in mind.

`Sitting-Posture-Recognition-master/util.py` - some functions required to calculate the co-ordinates of the key points.

`test.py` - Connecting the external vibrator that if "bad posture", it will remind people to adjust.

### Usage 

1. Please install all the requirements from `Sitting-Posture-Recognition-master/requirements.txt`.
2. Run `Sitting-Posture-Recognition-master/posture_realtime.py` for testing it in real time. Please sit sufficiently far away from the system showing your lateral view. Please note that this will require a system with atleast 8GB RAM. On a 4 GB RAM, the output is not at all smooth and the output lags very much from the input frame.

**NOTE**: The repository's files come from the code sources referenced above. We have not used all of them. We only used the “real time” part and added the vibrator peripheral, modified some of the function parameters and output results and their judgments.

Now the code is still in continuous development.
