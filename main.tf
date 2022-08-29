# provider "google" {
#   credentials = file("gcp/rugged-reality-360906-20432e567e30.json")

#   project = "rugged-reality-360906"
#   region  = "us-central1"
#   zone    = "us-central1-c"
# }


# resource "google_storage_bucket" "test_bucket" {

#   name     = "dlt_data01"
#   location = "us-central1"

# }

# # data "archive_file" "zip_file_maker" {

# #   type        = "zip"
# #   source_dir  = "${path.module}/api/env/lib/python3.10/site-packages/"
# #   output_path = "${path.module}/api/custem_librarys.zip"


# # }


# resource "google_storage_bucket_object" "archive" {
#   name   = "app.zip"
#   bucket = google_storage_bucket.test_bucket.name
#   source = "/home/deq/Documents/projects/problemStatement_DET/api/app.zip"
# }



# # resource "google_cloudfunctions_function" "dit_problem_statement" {
# #   name        = "cloud_func"
# #   description = "cloud function"
# #   runtime     = "python3.10"

# #   available_memory_mb = 128

# #   source_archive_bucket = google_storage_bucket.test_bucket.name
# #   source_archive_object = google_storage_bucket_object.archive.name

# #   trigger_http                 = true
# # #   https_trigger_security_level = "SECURE_ALWAYS"
# #   timeout                      = 60
# #   entry_point                  = "forms"
# #   labels = {
# #     my-label = "dlt_data-test"
# #   }

# # #   environment_variables = {
# # #     MY_ENV_VAR = "my-env-var-value"
# # #   }
# # }

# resource "google_cloudfunctions_function" "function" {
#   name        = "function-test"
#   description = "My function"
#   runtime     = "nodejs16"

#   available_memory_mb          = 128
#   source_archive_bucket        = google_storage_bucket.test_bucket.name
#   source_archive_object        = google_storage_bucket_object.archive.name
#   trigger_http                 = true
# #   https_trigger_security_level = "SECURE_ALWAYS"
#   timeout                      = 60
#   entry_point                  = "helloGET"
#   labels = {
#     my-label = "my-label-value"
#   }

#   environment_variables = {
#     MY_ENV_VAR = "my-env-var-value"
#   }
# }

# # resource "google_cloudfunctions_function_iam_member" "invoker" {
# #   project        = google_cloudfunctions_function.function.project
# #   region         = google_cloudfunctions_function.function.region
# #   cloud_function = google_cloudfunctions_function.function.name

# #   role   = "roles/cloudfunctions.invoker"
# #   member = "user:myFunctionInvoker@example.com"
# # }

