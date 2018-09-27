# Image-Classification-with-Tensorflow

Design and implement a RESTful API via the Flask framework, in the API, we do image recognition with tensorflow and we also use mongodb to store the user information.

## Getting Started

I tested the API in my own machine, the operating system is Ubuntu 18.04.1 LTS, x86_64 x86_64 x86_64 GNU/Linux. And the following is the detailed information about the CPU I'm using:

- processor	: 0
- vendor_id	: AuthenticAMD
- cpu family	: 21
- model		: 48
- model name	: AMD A10-7300 Radeon R6, 10 Compute Cores 4C+6G
- stepping	: 1
- microcode	: 0x6003104
- cpu MHz		: 1900.000
- cache size	: 2048 KB
- physical id	: 0
- siblings	: 1
- core id		: 0
- cpu cores	: 1
- apicid		: 0
- initial apicid	: 0
- fpu		: yes
- fpu_exception	: yes
- cpuid level	: 13
- wp		: yes
- flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 x2apic popcnt aes xsave avx f16c hypervisor lahf_lm svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw xop fma4 tbm ssbd vmmcall fsgsbase bmi1 xsaveopt arat npt svm_lock nrip_save vmcb_clean flushbyasid decodeassists
- bugs		: fxsave_leak sysret_ss_attrs null_seg spectre_v1 spectre_v2 spec_store_bypass
- bogomips	: 3800.00
- TLB size	: 1536 4K pages
- clflush size	: 64
- cache_alignment	: 64
- address sizes	: 43 bits physical, 48 bits virtual

### Prerequisites

Clone this repository to a directory of your choice.

### Installing

#### Install Python3, flask, flask-restfull, bcrypt:

1. `sudo apt install python3-pip`
2. `pip3 install flask`
3. `pip3 install flask-restful`
4. `sudo apt install python-pip`
5. `pip install bcrypt`

#### Install Postman:
##### For Ubuntu 16.04:
1. `wget https://dl.pstmn.io/download/latest/linux64 -O postman.tar.gz`
2. `sudo tar -xzf postman.tar.gz -C /opt`
3. `rm postman.tar.gz`
4. `sudo ln -s /opt/Postman/Postman /usr/bin/postman`
##### For Ubuntu 18.04:
-  `snap install postman`
#### Install Docker:
1. `sudo apt-get update`
2. `sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common`
3. `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
##### For x86_64/amd64:
4. `sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"`
#### Install Docker CE:
- `sudo apt-get update`
- `sudo apt-get install docker-ce`
#### Install Docker Compose:
1. `sudo curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
2. `sudo chmod +x /usr/local/bin/docker-compose`
#### Install MongoDB:
##### Step1:Add MongoDB Package Repository To Ubuntu
- `sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5`
- `echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list`
##### Step 2: Install MongoDB On Ubuntu 18.04
- `sudo apt update`
- `sudo apt install -y mongodb-org`
##### Step 3: Start MongoDB service:
- `sudo systemctl start mongod.service`
## Running the tests
Go to the folder where you clone the project and run the following command:
- `sudo docker-compose build`, this could take a while, once it said 
*successfully built*, and then we run `sudo docker-compose up`, to start the server.
And then we open postman, once it opened, we choose to type in the url, which is `localhost:5000`, and since we use POST data as input, therefore, we choose `POST`, and in the body tag, we choose *raw* and `JSON(application/json)`, after all is set, it should looks like this:
![image](https://github.com/zbian002/Image-Classification-with-Tensorflow/blob/master/images/1.png)
### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

