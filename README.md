# lab8

In today's lab we'll be focussing on connecting your machine learning application with Flask and Docker to run your application as a service on a Docker container. 

## Task 1

Let's create the repository for your application.

1. Create a repository in github and clone it to your local machine
2. Follow the structure in [Lab 6](https://github.com/sp21-E222/lab6) to get the necessary files needed for a minimum Flask application and add it to your repo.
    
    ```bash
    server.py
    Dockerfile
    Makefile
    requirements.txt
    ```
3. Add your yaml specification you created to the repository
4. Do the necessary changes to server.py so that it can read your specification file. Remember what package allows us to do this.

## Task 2

Getting your python code into your repo and writing definitions.

1. Create directory structure for your python code
    ```bash
    server.py
    master.yaml
    Dockerfile
    Makefile
    requirements.txt
    my_python_dir
    ```
2. Pickel your model and add it to your repository.

    Refer to the [Lab 6 notebook.](https://github.com/sp21-E222/lab6/blob/main/svm_classifier.ipynb)

3. Create .py files with a prediciton definition

    Create the prediction endpoint just like in lab 6


