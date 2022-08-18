terraform {

  required_providers{

    google = {
        source = "hashicorp/google"
        version = "3.5.0"
    }
  }
}



provider "google" {

    credentials = file("gcp/creating-our-211-8c4d0b19-37a3dbad487a.json")

    project = "my-project-v1"
    region = "europe-north1"
    zone = "europe-north1-a"


}

resource "google_compute_network" "vpc" {

    name = "terraform-n/w"

}

# locals {

#   project = "my-project-v1"
# }

# provider "google-beta" {
#   project = local.project

# }

# resource "google_service_account" "default_account" {
#   provider     = google-beta
#   account_id   = ""
#   display_name = ""


# }

# resource "google_pubsub_topic" "testing_topic" {

#   provider = google-beta
#   name     = "demoTopic"

# }


# resource "google_storade_bucket" "testing_bucket" {

#     provider = google-beta
#     name = "${local.project}-gcf-source"
#     location = "US"
#     uniform_bucket_level_access = true
# }


# resource "google_storage_bucket_object" "object" {
#   provider = google-beta
#   name   = "function-source.zip"
#   bucket = google_storage_bucket.bucket.name
#   source = "function-source.zip"  # Add path to the zipped function source code
# }

# resource "google_cloudfunctions2_function" "function" {
#   provider = google-beta
#   name = "test-function"
#   location = "us-central1"
#   description = "a new function"

#   build_config {
#     runtime = "nodejs16"
#     entry_point = "helloPubSub"  # Set the entry point 
#     environment_variables = {
#         BUILD_CONFIG_TEST = "build_test"
#     }
#     source {
#       storage_source {
#         bucket = google_storage_bucket.bucket.name
#         object = google_storage_bucket_object.object.name
#       }
#     }
#   }

#   service_config {
#     max_instance_count  = 3
#     min_instance_count = 1
#     available_memory    = "256M"
#     timeout_seconds     = 60
#     environment_variables = {
#         SERVICE_CONFIG_TEST = "config_test"
#     }
#     ingress_settings = "ALLOW_INTERNAL_ONLY"
#     all_traffic_on_latest_revision = true
#     service_account_email = google_service_account.account.email
#   }

#   event_trigger {
#     trigger_region = "us-central1"
#     event_type = "google.cloud.pubsub.topic.v1.messagePublished"
#     pubsub_topic = google_pubsub_topic.topic.id
#     retry_policy = "RETRY_POLICY_RETRY"
#   }
# }



