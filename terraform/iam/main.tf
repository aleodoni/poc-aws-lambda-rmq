resource "aws_iam_role" "lambda" {
  name = "spl_voting_lambda"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = [
          "lambda.amazonaws.com",
          "apigateway.amazonaws.com"
        ]
      }
      Action = "sts:AssumeRole"
      Sid = ""
    }]
  })
}