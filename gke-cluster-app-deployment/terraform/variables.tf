variable "name" {
  default = "demo-cluster"
}

variable "project" {
  default = "gke-demo-309918"
}

variable "location" {
  default = "us-central1"
}

variable "initial_node_count" {
  default = 1
}

variable "machine_type" {
  default = "n1-standard-1"
}