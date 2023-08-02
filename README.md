# Game Recommender System

This is a simple game recommender system built using Python and frontend is built using Streamlit, a popular Python library for creating web applications with interactive visualizations. The recommender system uses collaborative filtering to suggest similar games based on user-selected games.

## Link to the project https://game-recommender.onrender.com

## Snapshot of project
![Screenshot 2023-08-02 183826](https://github.com/MZKhan18/Game-Recommender-System/assets/83308074/3a6c0779-fcf7-4e8e-917f-02b2b32e13ea)


## How it works

1. The system loads precomputed data from two pickle files: `game_dict.pkl` and `similarity.pkl`.
2. `game_dict.pkl` contains information about different games, such as name, icon, rating, download count, and URL link.
3. `similarity.pkl` stores precomputed similarity scores between different games, which are used to find similar games for the selected input.

## Getting Started

1. Clone the repository to your local machine.
2. Make sure you have Python and the required libraries installed. You can use the `requirements.txt` file to install the necessary packages.
3. Run the Streamlit app by executing the following command in your terminal:

```bash
streamlit run app.py
```

4. The web application will launch in your default web browser.

## How to Use

1. Select a game from the dropdown list.
2. Click on the "Recommend Similar Games" button.
3. The system will display five similar games along with their icons, ratings, download counts, and URL links.

## Dataset

The dataset used for this recommender system contains information about various games. Each entry in the dataset includes the following attributes:

- **name**: The name of the game.
- **icon**: The icon or logo of the game.
- **rating**: The rating of the game.
- **count**: The download count of the game.
- **URL**: The URL link to the game.

## Note

This is a simple example of a game recommender system using collaborative filtering. Depending on the dataset and the number of games, the accuracy and quality of recommendations can be improved using more sophisticated machine learning algorithms.
