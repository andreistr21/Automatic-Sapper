# Automatic-Sapper

### Description:
This project made by 4 students (including me) for learning purposes.

This project is self playing sapper game with additions. First a field is randomly generated, the field is divided into 
locations, each location can be one type of: standard, sand, water or swamp, and the cost of the action at that location 
depends on this. The player (the self-managing programme), can turn 90 degrees or take a step forward. Each location can
either be a house or a non-house, and with or without a mine.  

The player always appears in the top left corner, knowing where all the mines are. At the beginning, he uses a genetic 
algorithm to figure out the best path to all the mines, taking into account the type of locations he will pass through. 
After this, the player follows his route, reaching the location with the mine, the player makes a decision using a 
decision tree algorithm based on such parameters as: known (whether the mine model is known), power, new, location, 
stability and chain reaction (if there is even one mine nearby or if the mine is on a location with a house). A decision
can be: leave and mark the mine, defuse, defuse by explosion, remove and transport. In order to make a decision, the 
player had to determine if there was a house on the location, this was done with the help of a neural network by 
analysing the image.

## Technologies:
> Note: As this project was finished a long time ago and is now just uploaded to my personal GitHub, it is not possible
> to find out the versions of the modules.

* Python 3.7.9
* Scikit-learn
* Tkinter
* TensorFlow
* Pandas
* Numpy
* Matplotlib
* Opencv
* Joblib
* Seaborn

## Usage:
> Note: As I wrote above, the versions of the modules are not known if you want to run this program on your own, you may
> have some incompatibilities with the latest versions of the modules, and you will have to pick up the necessary 
> versions yourself.

If you want to run this program on your own, firstly you need to clone this project and install the necessary 
modules. 
- If you want just run this program, you need to download 
[this model](https://www.dropbox.com/s/6qo4z9easqnn9sl/model.rar?dl=0) and unpack it into `files/Neural_networks`, it 
should go like this `files/Neural_networks/model/training_500_epochs_ser`. After that, you can run `bin/Main/main.py` to
run this.

- If you want to train your own model, you need to download 
[this images](https://www.dropbox.com/s/r69999cuy20c7hm/Train.rar?dl=0) and unpack it into `files/Neural_networks`, It 
should go like this `files/Neural_networks/Train`. After that, you can run `bin/Main/LearnNeuralNetwork.py` to train your
model. After you trained it, you need to place it, like in step above.

## What have I done in this project?
#### I implemented:
- Almost the entire graphical interface
- Most of the mechanics (e.g. relocation, location types)
- Decision tree algorithm (except filling up csv file)
- House detection, using neural network (including search for ~30% of images)

