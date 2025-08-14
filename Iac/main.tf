
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
    random = { source = "hashicorp/random", version = "~> 3.0" }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "random_string" "suffix" {
  length  = 4
  special = false
  upper   = false
}

# S3
resource "aws_s3_bucket" "artifacts" {
  bucket = "packmybag-artifacts-${random_string.suffix.id}"
  force_destroy = true
  tags = {
    Project = "PackMyBag"
    Env = "ci-test"
  }
}

# DynamoDB
resource "aws_dynamodb_table" "packing_lists" {
  name = "packing_lists-${random_string.suffix.id}"
  billing_mode = "PAY_PER_REQUEST"
  hash_key = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

output "s3_bucket" {
  value = aws_s3_bucket.artifacts.bucket
}

output "ddb_table" {
  value = aws_dynamodb_table.packing_lists.name
}
