# Azure fundamentals(assignment-1)
Training Azure distribution

# Resources used
##  Resource Group --> cloud_training
##  Subscription --> MLE Group 
1. SSH-Key 
    - For Remote connection
2. Storage Account
    - To store files uploaded
3. Virtual Network
    - To categorize subnet.
4. Disk
    - Extended disk (8GB)
5. OS Disk
    - To store OS interface
6. Network Interface
7. Network Security group
8. Public IP address
9. Virtual Machine
    - To install application and run server
    - OS: Linux (ubuntu 20.04)
    - Image Size: Standard D2s v3 (2 vcpus, 8 GiB memory)

#   Flask Application
- A server for collecting filenames presented in azure storage container.
- Runs on localhost on VM machine via nginx server.

# Access to server
-   http://ggndp.eastus.cloudapp.azure.com:5000/ can be used to access server and see results.

> **_NOTE:_**
The above link will only work if VM is up and running at the time.

# Result
![Alt text](./utils/FolderList.jpg?raw=true "Server Response")

# Billing (ggndp:ml-ops-1)
![Alt text](./utils/BillingInfo.png?raw=true "Billing Information ggndp:")



# Docker Basics(assignment-2)
# Resources used
##  Resource Group --> cloud_training
##  Subscription --> MLE Group 
1. SSH-Key 
    - For Remote connection
2. Storage Account
    - To store files uploaded
3. Virtual Network
    - To categorize subnet.
4. Container Registory
    - Allows to build, store, and manage container images
5. OS Disk
    - To store OS interface
6. Network Interface
7. Network Security group
8. Public IP address
9. Virtual Machine
    - To install application and run server
    - OS: Linux (ubuntu 20.04)
    - Image Size: Standard D2s v3 (2 vcpus, 8 GiB memory)

#   Flask Application
- A server for collecting filenames presented in azure storage container.
- Runs on localhost on VM machine via docker interface.

 Access to server
-   http://ggndp.eastus.cloudapp.azure.com:5000/ can be used to access server and see results.

> **_NOTE:_**
The above link will only work if VM is up and running at the time.

# Result
![Alt text](./utils/ACR_result.jpg?raw=true "Server Response")

# Docker Running on VM
![Alt text](./utils/VM_docker.jpg?raw=true "Docker running on VM")

# Repository created
![Alt text](./utils/ACR_repo.jpg?raw=true "Repository created")

# Billing Info (Cummulated with ACR)
![Alt text](./utils/Billing_ACR.png?raw=true "Billing info (cummulated with ACR)")




