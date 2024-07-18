# incomplete_drawing_task
This repository stores the JsPsych code for setting up the experiment for my MA thesis at UChicago. It utilizes [**Cognition.run**](https://www.cognition.run/) to run the experiment and store participants' responses on the server provided by **Cognition.run** and further allows users to download the data in json format. 

## Hosting and Running the Experiment Website
In order to stream the three large-size videos, I used the team account from Akram Bakkour's lab to clone this github repository to **Cognition.run**. 

From the participants' side, they can participate in this experiment by clicking the [experiment website](https://s9e279qf6f.cognition.run) hosted by **Cognition.run** web server.

After participants have completed the experiment, their submitted response will be available on *incomplete_shape_drawing* task section on **Cognition.run** homepage (team account from Akram Bakkour's lab), allowing me to download json-format data (see the [example output data](sample_output.json)).

## Github Repository Navigation
The following is the **directory layout** of this repo:

    .
    ├── \.github/workflows               # deploy website via Cognition.run       
    ├── \public
        ├── \images                      # folder to store incomplete shapes
        ├── \jspsych                     # folder to store jspsych css and javscript files, alongside plugins used in this study
        ├── \videos                      # folder to store videos for mood induction
        ├── public/mood_creativity.html  # html file of the experiment webpage
    ├── .gitignore
    ├── README.md
    ├── sample_output.json               # sample output data
    ├── sample_response.gif              # sample response using the website

## Mood Induction Videos
The three mood induction videos (for positive valence and high arousal, positive valence and low arousal, and neutral conditions) are stored in [Google Drive](https://drive.google.com/drive/u/0/folders/1TgkST_8BaKBVv45mN1DDP4-GMQafI4mG?ths=true). 