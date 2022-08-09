# terraform {
#   required_providers {
#     aws = {
#       source  = hashicorp / aws
#       version = "~> 4.0"
#     }
#   }
# }

provider "aws" {
  region                   = "us-east-1"
  shared_credentials_files = ["/home/deq/.aws/credentials"]

  #   access_key = var.AWS_Credentials.access_key
  #   secret_key = var.AWS_Credentials.secret_key
}

resource "aws_iam_role" "aws_iam_role_test_v1" {

  name = "aws_iam_role_test_v1"

  assume_role_policy = <<EOF

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF

}

data "archive_file" "zip_file" {

  type        = "zip"
  source_dir  = "${path.module}/python/"
  output_path = "${path.module}/python/app.zip"

}


resource "aws_lambda_function" "testing_data_v1" {
  filename      = "${path.module}/python/App.zip"
  function_name = "aws_lambda_function_test_v1"
  role          = aws_iam_role.aws_iam_role_test_v1.arn
  handler       = "app.lambda_helper"
  runtime       = "python3.9"


}

data "archive_file" "zip_file_v1" {

  type        = "zip"
  source_dir  = "${path.module}/python/env/lib/python3.10/site-packages/"
  output_path = "${path.module}/python/custem_librarys.zip"

}
resource "aws_lambda_layer_version" "custem_librarys" {

  filename   = "${path.module}/python/custem_librarys.zip"
  layer_name = "custem_librarys"

  compatible_runtimes = ["python3.9"]

}

