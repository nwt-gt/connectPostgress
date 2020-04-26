FROM ubuntu:latest

# install system-wide deps for python and node
RUN apt-get -yqq update
RUN apt-get -yqq install python-pip python3.6 python-dev libpq-dev
# copy our application code
ADD pythoncodes /opt/flask-app
WORKDIR /opt/flask-app

RUN pip install -r requirements.txt
CMD ["bash"]

# default input
#ENTRYPOINT [ "sh", "runPythonScript.sh"]
# dafault add on to the input. ["inputfilename","outoutfile name"]
#CMD ["dataset.csv","24-5-2020"]
# start from base
