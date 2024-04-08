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
        # Aplica as configurações do Terraform para o recurso específico
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_{}'.format(resource_type)], cwd=terraform_dir, check=True)
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
        # Criar Grupo de Recursos
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_resource_group.Grupo_de_recursos'], cwd=terraform_dir, check=True)
        # Criar Conta de Armazenamento 
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_storage_account.Conta_de_armazenamento'], cwd=terraform_dir, check=True)
        # Criar VNET
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_virtual_network.VNET'], cwd=terraform_dir, check=True)
        # Criar Subrede Pública
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_subnet.Subrede_Publica'], cwd=terraform_dir, check=True)
        # Criar Subrede Privada
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_subnet.Subrede_Privada'], cwd=terraform_dir, check=True)
        # Criar Grupo de Segurança
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_network_security_group.Grupo_de_Seguranca'], cwd=terraform_dir, check=True)
        # Criar Interface de IP Público Linux e Associar 
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_public_ip.public_ip_linux', '-target=azurerm_network_interface.Interface_de_rede_Linux'], cwd=terraform_dir, check=True)
        # Criar Interface de IP Público Windows e Associar 
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_public_ip.public_ip_windows', '-target=azurerm_network_interface.Interface_de_rede_Windows'], cwd=terraform_dir, check=True)
        # Criar Maquina Virtual Windows
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_windows_virtual_machine.windows'], cwd=terraform_dir, check=True)
        # Criar Maquina Virtual Linux
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_linux_virtual_machine.linux'], cwd=terraform_dir, check=True)
        
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
def Criar():
    data = request.get_json()
    platform = data.get('platform')
    resources_to_create = data.get('resources_to_create')

    if not platform or not resources_to_create:
        return jsonify({"error": "Platform and resources to create are required"}), 400

    if platform == 'azure':
        # Chama a função para criar recursos na Azure
        message = Criar_AZURE(resources_to_create)
        return jsonify({"message": message}), 200
    elif platform == 'aws':
        # Chama a função para criar recursos na AWS
        message = Criar_AWS(resources_to_create)
        return jsonify({"message": message}), 200
    else:
       return jsonify({"error": "Invalid platform"}), 400

# Endipoint para Destruir
@app.route('/destruir', methods=['POST'])
def Destruir():
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

# Endipoint para exibir MENU
@app.route('/menu', methods=['GET'])
def menu():
    menu_options = {
        "aws": {
            "create": [
                "vpc",
                "subnet_publica",
                "subnet_privada",
                "internet_gateway",
                "route_table",
                "route_table_association",
                "security_group_linux",
                "security_group_windows",
                "ec2_linux",
                "ec2_windows"
            ],
            "destroy": "Destruir todos os recursos AWS"
        },
        "azure": {
            "create": [
                "resource_group",
                "storage_account",
                "virtual_network",
                "subnet_publica",
                "subnet_privada",
                "network_security_group",
                "public_ip_linux",
                "public_ip_windows",
                "interface_de_rede_linux",
                "interface_de_rede_windows",
                "linux_virtual_machine",
                "windows_virtual_machine"
            ],
            "destroy": "Destruir todos os recursos Azure"
        }
    }
    return jsonify(menu_options), 200

if __name__ == '__main__':
    app.run(debug=True)
