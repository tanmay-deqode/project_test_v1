provider "google" {
  credentials = file("gcp/rugged-reality-360906-20432e567e30.json")

  project = "rugged-reality-360906"
  region  = "us-central1"
  zone    = "us-central1-c"
}

resource "google_storage_bucket" "bucket" {
  name     = "td1"
  location = "us-central1"
}

resource "google_storage_bucket_object" "archive" {
  name   = "demo.zip"
  bucket = google_storage_bucket.bucket.name
  source = "/home/deq/Documents/projects/problemStatement_DET/data/demo.zip"
}

resource "google_cloudfunctions_function" "function1" {
  name        = "function-test"
  description = "My function"
  runtime     = "nodejs16"

  available_memory_mb   = 128
  source_archive_bucket = google_storage_bucket.bucket.name
  source_archive_object = google_storage_bucket_object.archive.name
  trigger_http          = true
  timeout               = 60
  entry_point           = "helloGET"
  labels = {
    my-label = "demodata"
  }
}

# IAM entry for a single user to invoke the function
# resource "google_cloudfunctions_function_iam_member" "invoker" {
#   project        = google_cloudfunctions_function.function.project
#   region         = google_cloudfunctions_function.function.region
#   cloud_function = google_cloudfunctions_function.function.name

#   role   = "roles/cloudfunctions.invoker"
#   member = "user:myFunctionInvoker@example.com"
# }