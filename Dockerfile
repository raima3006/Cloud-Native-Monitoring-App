#chose docker image
FROM python:3.9-slim-buster         

#set working directory
WORKDIR /app        

#help docker file to access requirment dependencies
COPY requirements.txt .      

#install required packages and no-cache will take responsibility for cache releted problem
RUN pip3 install --no-cache-dir -r requirements.txt       

#COPY everything (.) from app directory to current or working directory (.)
COPY . .        

#set env for flask app
ENV FLASK_RUN_HOST=0.0.0.0

# container will run on this port
EXPOSE 5000         

#app will run
CMD ["flask", "run"]        

