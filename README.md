# gRPC Image Rotation Service

A client server model implementing gRPC interface for image processing (rotating and mean filter) in Python.

**Installation Requirement**
- 
Install Python 2.7 or 3.8 and pip3
pip3 can be installed with following command:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```
check Python version with the following command:
```
python --version
```
Run `./setup` and `./build`. If not successfull run the follow command:
```
chmod +x ./setup
chmod +x ./build
```
**Running Instructions**
- 
- run `./server.py --host {hostname} --port {port}` to start server. Notice this is only running localhost for now so hostname would not make any changes to the file. It is required for future improvement purposes.
- run `./client.py --host{hostname} --port{port} --input {input image path} --output {output path} --rotate NONE --mean` to have client connect to server and send request. Note that hostname is not supported as this only runs on localhost for now. Please make sure the port number is correct though. 
- rotate and mean are options for opertaions on input image. They are optional but you need to enter at least one, you can also perform two operations simultaneously.
- for more detailed descriptions on the argument options, enter
`./client.py -h`
- make sure the input image is JPEG or PNG, and it's either 'RGB' for color and 'L' for grayscale

**Future Improvements**
-
***High Volume Request Support***
The current server does not support high volume traffic well. When large number of requests happen concurrently, long delay will happen. When the service is scaling to more engineers, this should ideally be written in a different language like C++ where we would have total control of memory and better handle large number of threads.

***Faster Mean Filter***
When doing mean filter, Scipy's convolve2d is slower compare to openCV, which is not supported by Python 2.7. For a larger scale service, it is preferred to use openCV. However, switching from Python 2.7 to Python 3.8 might create problem for our existing codebase. Ideally we should specify the usage of Python 3.8 and use openCV for mean filter.

***Host***
Right now the host argument is a dummy as the code is running on localhost. With more time, server should be deployed on cloud.

***Secure Channel***
In production code, we should create secure channel with credentials for security reasons.

***Streaming gRPC***
Ideally we should send and receive streams of data to ensure better handling for larger data

***Support Nore Image Type***
With more time, we should also implement support for other image types (i.e. TIFF) as well as image mode (i.e. RGBA)

***Multiple Servers***
Create load balancer and multiple servers to handle large volume of input