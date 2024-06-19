output "lambda_splvoting_invokearn" {
  value = aws_lambda_function.splvoting.invoke_arn
}

output "lambda_function_name" {
  value = aws_lambda_function.splvoting.function_name
}

output "lambda_function_arn" {
  value = aws_lambda_function.splvoting.arn
}
