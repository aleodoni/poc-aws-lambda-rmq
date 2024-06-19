module "iam" {
  source = "./iam"
}

module "lambda-spl" {
  source = "./lambda"

  iam_role_arn = module.iam.iam_role_arn
}

module "eventbridge" {
  source = "./eventbridge"

  lambda_function_arn = module.lambda-spl.lambda_function_arn
  lambda_function_name = module.lambda-spl.lambda_function_name
}

# module "gw" {
#   source = "./apigateway"

#   lambda_helloworld_invokearn = module.hello-world.lambda_helloworld_invokearn
#   lambda_function_name = module.hello-world.lambda_function_name
# }

# output "Main_Url" {
#   value = module.gw.main_url
# }