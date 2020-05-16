# League-of-Legends-Diamond-Ranked-Games-Kaggle-Competition

## Getting Started

League of Legends is a MOBA (multiplayer online battle arena) where 2 teams (blue and red) face off. There are 3 lanes, a jungle, and 5 roles. The goal is to take down the enemy Nexus to win the game.

The column blueWins is the target value (the value we are trying to predict). A value of 1 means the blue team has won. 0 otherwise. 


### Installing

This model runs on Python 3.7.0 bulit with Keras

Install the Required libraries

```
pip install -r requirements.txt
```

### Run The model

```
python model.py
```

### Evaltation

The model scored 72% on the test set after training for 100 epoch.