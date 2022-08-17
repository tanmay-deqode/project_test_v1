# terraform {

#   required_providers{

#     google = {
#         source = "hashicorp/google"
#         version = "3.5.0"
#     }
#   }
# }



# provider "google" {

#     credentials = file("/google/credentials.json")

#     project = "my-project-v1"
#     region = ""
#     zone = ""


# }

# resource "google_compute_network" "vpc" {

#     name = "terraform-n/w"

# }

locals {

  project = "my-project-v1"
}

provider "google-beta" {
  project = local.project

}

resource "google_service_account" "default_account" {
  provider     = google-beta
  account_id   = ""
  display_name = ""


}

resource "google_pubsub_topic" "testing_topic" {

  provider = google-beta
  name     = "demoTopic"

}


resource "google_storade_bucket" "testing_bucket" {

    provider = google-beta
    name = "${local.project}-gcf-source"
    location = "US"
    uniform_bucket_level_access = true
}




