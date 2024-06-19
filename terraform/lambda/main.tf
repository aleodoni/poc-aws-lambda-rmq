resource "null_resource" "install_layer_dependencies" {
  provisioner "local-exec" {
    command = "pip install -r ../lambda/requirements.txt -t libcode --prefer-binary"
  }
  triggers = {
    trigger = timestamp()
  }
}

resource "null_resource" "copy_code" {
  provisioner "local-exec" {
    command = "cp -fR ../lambda/* libcode"
  }
  triggers = {
    trigger = timestamp()
  }
}

data "archive_file" "allcode" {
  type        = "zip"
  source_dir = "libcode"
  output_path = "outputs/allcode.zip"

  depends_on = [
      null_resource.install_layer_dependencies,
      null_resource.copy_code
    ]
}


resource "aws_lambda_function" "splvoting" {
    filename = data.archive_file.allcode.output_path   
    function_name = "lambdaSplVoting"
    role = var.iam_role_arn
    handler = "handler.handler"
    runtime = "python3.12"
}