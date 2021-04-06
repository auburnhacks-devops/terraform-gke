# Pre-requestites
1. Google Cloud Account
2. Terraform setup
3. Docker Deamon
4. Git

# Create a Basic Hello-world app
1. Clone this project using https://github.com/auburnhacks-devops/terraform-gke.git
2. cd into gke-cluster-app-deployment/app
3. Run "docker build -t hello-world-app:latest ." to build docker image from Dockerfile
4. Run the following commands to push the docker image
```shell
$ export PROJECT_ID="$(gcloud config get-value project -q)"
$ gcloud auth configure-docker
$ docker tag hello-world-app:latest "gcr.io/${PROJECT_ID}/hello-world-app:latest"
$ docker push "gcr.io/${PROJECT_ID}/hello-world-app:latest"
```

# Create GKE Cluster using terraform
1. cd into gke-cluster-app-deployment/terraform
2. Run the following commands to launch GKE cluster
```shell
$ terraform init
$ terraform plan
$ terraform apply
```
Note: It will take few minutes to create the cluster.


