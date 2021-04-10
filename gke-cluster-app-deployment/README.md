# Pre-requestites
1. Google Cloud Account
2. Terraform setup
3. Docker Deamon
4. Git

# Dockerize app
1. Clone this project using https://github.com/auburnhacks-devops/terraform-gke.git
2. cd into gke-cluster-app-deployment/app
3. Run the following commands to push the image into GCR
```shell
$ export PROJECT_ID="$(gcloud config get-value project -q)"
$ gcloud auth configure-docker
$ gcloud builds --project gke-demo-309918 submit --tag gcr.io/gke-demo-309918/covidtracking:v1 .
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


