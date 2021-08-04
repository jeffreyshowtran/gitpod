FROM ubuntu:focal

# Alpine update & upgrade
RUN apt update 

#minimal install of python3 and pip3 and clear apk cache
RUN apt install -y python3-dev python3 python3-pip

#install the libraries needed into the container 
RUN pip install --no-cache-dir pdfplumber 

#identify the working directory in github 
WORKDIR /work

#copy to all to work directory 
COPY . /work/

#run the python script pdf2txt1_v1.2
CMD [ "python3", "pdf2txt1_v1.2.py" ]


#best practice for pip installs is to run pip cache purge after all pip install calls
# Example install procedure is bellow 
# pip install numpy
# pip cache purge