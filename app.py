from flask import Flask, request, jsonify
import json
import subprocess

app = Flask(__name__)

# Criar Recursos na AWS
def Criar_AWS(resource_type):
    terraform_dir = './aws/'
    try:
        # Inicializa o Terraform
        subprocess.run(['terraform', 'init'], cwd=terraform_dir, check=True)
        # Aplica as configurações do Terraform
        subprocess.run(['terraform', 'apply', '-auto-approve'], cwd=terraform_dir, check=True)
        return f"AWS {resource_type} creation initiated"
    except subprocess.CalledProcessError as e:
        return f"Error creating AWS {resource_type}: {e.output}"

# Destruir Recursos na AWS
def Destruir_AWS():
    terraform_dir = './aws/'
    try:
        # Destroi os recursos criados pelo Terraform
        subprocess.run(['terraform', 'destroy', '-auto-approve'], cwd=terraform_dir, check=True)
        return "AWS resources destroyed"
    except subprocess.CalledProcessError as e:
        return f"Error destroying AWS resources: {e.output}"

# Criar Recursos na AZURE
def Criar_AZURE(resource_type):
    terraform_dir = './azure/'
    try:
        # Inicializa o Terraform
        subprocess.run(['terraform', 'init'], cwd=terraform_dir, check=True)
        # Aplica as configurações do Terraform
        subprocess.run(['terraform', 'apply', '-auto-approve'], cwd=terraform_dir, check=True)
        return f"Azure {resource_type} creation initiated"
    except subprocess.CalledProcessError as e:
        return f"Error creating Azure {resource_type}: {e.output}"

# Destruir Recursos na AZURE
def Destruir_AZURE():
    terraform_dir = './azure/'
    try:
        # Destroi os recursos criados pelo Terraform
        subprocess.run(['terraform', 'destroy', '-auto-approve'], cwd=terraform_dir, check=True)
        return "Azure resources destroyed"
    except subprocess.CalledProcessError as e:
        return f"Error destroying Azure resources: {e.output}"

# Endpoint de Criação de Recursos
@app.route('/api', methods=['POST'])
def create_resource():
    data = request.get_json()
    platform = data.get('platform')
    resource_type = data.get('resource_type')

    if not platform or not resource_type:
        return jsonify({"error": "Platform and resource type are required"}), 400

    if platform == 'aws':
        # Chama a função para criar recursos na AWS
        message = Criar_AWS(resource_type)
        return jsonify({"message": message}), 200
    elif platform == 'azure':
        # Chama a função para criar recursos no Azure
        message = Criar_AZURE(resource_type)
        return jsonify({"message": message}), 200
    else:
        return jsonify({"error": "Invalid platform"}), 400

@app.route('/destruir', methods=['POST'])
def destroy_resource():
    data = request.get_json()
    platform = data.get('platform')

    if not platform:
        return jsonify({"error": "Platform is required"}), 400

    if platform == 'aws':
        # Chama a função para destruir recursos na AWS
        message = Destruir_AWS()
        return jsonify({"message": message}), 200
    elif platform == 'azure':
        # Chama a função para destruir recursos no Azure
        message = Destruir_AZURE()
        return jsonify({"message": message}), 200
    else:
        return jsonify({"error": "Invalid platform"}), 400

if __name__ == '__main__':
    app.run(debug=True)
