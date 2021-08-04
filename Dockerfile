FROM ubuntu:focal

# Alpine update & upgrade
RUN apt update 

#minimal install of python3 and pip3 and clear apk cache
RUN apt install -y python3-dev python3 python3-pip

#install the libraries needed into the container 
RUN pip install --no-cache-dir pdfplumber 

#identify the working directory 
WORKDIR /work

#copy to all to work directory 
COPY . /work/

#run the python script pdf2txt1_v1.2
CMD [ "python3", "pdf2txt1_v1.2.py" ]

# when you run the container in the file system: 
# > docker run -it --entrypoint /bin/bash -v /workspace/gitpod:/gitpod test
# the kicker here is to redirect the default volume where the container is looking 
# to the volume where the data files live 