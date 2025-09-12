from roboflow import Roboflow
rf = Roboflow(api_key="HwIYu3zVL2SPcVB9c21X")
project = rf.workspace("competition-o98lu").project("obstacles-yywad")
version = project.version(5)
dataset = version.download("yolov5")
