FROM ubuntu:20.10

# set the working directory
WORKDIR ./docker_image

# copy all the files to the container
COPY . .

# install dependencies
#RUN pip install --no-cache-dir -r requirements.txt
RUN ./docker_before_install.sh

# define the port number the container should expose
EXPOSE 5000

# run the command
CMD ["ls"]
