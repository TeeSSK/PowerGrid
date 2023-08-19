# PowerGrid

## Description

Term-project for education, aim to solve the problem Vertex Cover.

## Run project via Python locally

There are two files are used as inputs as a `sys.argv`: one is an input file and the other is a file used to store the result. <br>
If you aren't install ortools yet, you need to run this command before run the python file.  

```
pip install ortools
```

The command shown below is an example for running this project:

```
python powerGrid.py ./data/input/rand-50-200.txt ./data/output/outtest.txt
```

## Run project via Docker

First, build docker image via `docker build -t $yourtagname .` and create docker container for running docker image. <br>
There are two file for mouting volume from host directory to directory inside the container. <br>
  1. `$(pwd)"/data/input` map to `/input`.
  2.  `$(pwd)"/data/output` map to `/output`.  
 
  and access as `sys.argv` behind powergrid (name of docker image).

### Example command is below:
```
docker run -v "$(pwd)"/data/input:/input -v "$(pwd)"/data/output:/output powergrid /input/rand-50-200.txt /output/outtest.txt
```
