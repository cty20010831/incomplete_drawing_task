# UChicago_MA_Thesis_Experiment
This repository stores the JsPsych code for setting up the experiment for my MA thesis at UChicago. It utilizes [**Cognition.run**](https://www.cognition.run/) to run the experiment and store participants' responses on the server provided by **Cognition.run**. This allows users to download the data in json format by navigating to the *UChicago_MA_Thesis_Experiment* task section in my **Cognition.run** homepage.

## Hosting and Running the Experiment Website
From the participants' side, they can participate in this experiment by clicking the [experiment website](https://kvpbgcbdhz.cognition.run).

After a participant complete the experiment, they submitted response will be available on *UChicago_MA_Thesis_Experiment* task section in my **Cognition.run** homepage, allowing me to download json-format data (see the [example output data](sample_output.json)).

## Github Repository Navigation
The following is the **directory layout** of this repo:

    .
    ├── \.github/workflows  # deploy website via Cognition.run       
    ├── \public
        ├── \images                      # folder to store incomplete shapes
        ├── \jspsych                     # folder to store jspsych css and javscript files, alongside plugins used in this study
        ├── \videos                      # folder to store videos for mood induction
        ├── public/mood_creativity.html  # html file of the experiment webpage
    ├── .gitignore
    ├── README.md
    ├── sample_output.json  # sample output data

## Points of Concern
One imporant point of concern right row is that, despite the covenience offered by **Cognition.run**, free-account users can only upload a video with size less than 2MB. This leads to potential issues for me to upload the videos used for mood induction, which is very likely to exceed the size limit. 

One workaround is I can think of is utilizing serverless web application on [AWS](https://aws.amazon.com/free/webapps/?gclid=CjwKCAjw0YGyBhByEiwAQmBEWnM9sV53l-OWSyEKQyv-kAG2KBINRIsA7x-uipJRll8sgzetWVttVBoCAFIQAvD_BwE&trk=6f75e631-3b71-4d44-a71d-d557bcd37563&sc_channel=ps&ef_id=CjwKCAjw0YGyBhByEiwAQmBEWnM9sV53l-OWSyEKQyv-kAG2KBINRIsA7x-uipJRll8sgzetWVttVBoCAFIQAvD_BwE:G:s&s_kwcid=AL!4422!3!531871356401!p!!g!!hosting%20site!2038938166!74770369169), including S3, API Gateway, Lambda, DynamoDB, and CloudFront. This will allows me to create a website that allows me to handle requests to pariticipate the experiment via API control and also insert/save and download data using DynamoDB. Some pontential resources to look for:
- [Deploying Serverless Web Application on AWS: S3, API Gateway, Lambda, DynamoDB, and CloudFront (Youtube Video)](https://www.youtube.com/watch?v=pK52mfm69i0);
- [AWS Project: Architect and Build an End-to-End AWS Web Application from Scratch, Step by Step (Youtube Video)](https://www.youtube.com/watch?v=7m_q1ldzw0U);
- [AWS Lambda + API Gateway + DynamoDB + S3 = Dynamic Web App (Youtube Video)](https://www.youtube.com/watch?v=PzNQXYWQQ7c).

Another potential workaround is to apply for and use a web server provided by University of Chicago that can run PHP (see this [link](https://websites.uchicago.edu/website-options/self-service/)), so that I can save each participant's data as a CSV or JSON file on the server. Some pontential resources to look for: 
- [Saving jsPsych data to a web server using PHP](https://kywch.github.io/jsPsych-in-Qualtrics/save-php/);
- [Data Storage, Aggregation, and Manipulation (jsPsych documentation)](https://www.jspsych.org/7.0/overview/data/).

## To-do

