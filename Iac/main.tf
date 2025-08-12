
terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

provider "aws" {
  region = "us-east-1"
}

# S3
resource "aws_s3_bucket" "artifacts" {
  bucket = "packmybag-artifacts-20250814"
  tags = {
    Project = "PackMyBag"
    Env = "prod"
  }
}

# DynamoDB
resource "aws_dynamodb_table" "packing_lists" {
  name = "packing_lists"
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
