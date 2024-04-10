from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import subprocess

app = Flask(__name__)
# CORS para Azure
CORS(app, resources={
    r"/azure/*": {"origins": "*"},
    r"/aws/*": {"origins": "*"}
})

# ----------------------------------------------------AZURE-----------------------------------------------------------#

# Função para criar Grupo de Recursos na Azure
@app.route('/azure/criar-grupo-recursos', methods=['POST'])
def criar_grupo_recursos_azure():
    terraform_dir = './azure/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_resource_group.Grupo_de_recursos'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Grupo de Recursos criado com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Grupo de Recursos: {e}"}), 500

# Função para criar Conta de Armazenamento na Azure
@app.route('/azure/criar-conta-armazenamento', methods=['POST'])
def criar_conta_armazenamento_azure():
    terraform_dir = './azure/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_storage_account.Conta_de_armazenamento'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Conta de Armazenamento criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Conta de Armazenamento: {e}"}), 500

# Função para criar VNET na Azure
@app.route('/azure/criar-vnet', methods=['POST'])
def criar_vnet_azure():
    terraform_dir = './azure/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_virtual_network.VNET'], cwd=terraform_dir, check=True)
        return jsonify({"message": "VNET criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar VNET: {e}"}), 500

# Função para criar Subrede Pública na Azure
@app.route('/azure/criar-subrede-publica', methods=['POST'])
def criar_subrede_publica_azure():
    terraform_dir = './azure/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_subnet.Subrede_Publica'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Subrede Pública criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Subrede Pública: {e}"}), 500

# Função para criar Subrede Privada na Azure
@app.route('/azure/criar-subrede-privada', methods=['POST'])
def criar_subrede_privada_azure():
    terraform_dir = './azure/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_subnet.Subrede_Privada'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Subrede Privada criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Subrede Privada: {e}"}), 500

# Função para criar Grupo de Segurança Linux na Azure
@app.route('/azure/criar-grupo-seguranca-linux', methods=['POST'])
def criar_grupo_seguranca_linux_azure():
    terraform_dir = './azure/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_network_security_group.Grupo_de_Seguranca_Linux'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Grupo de Segurança Linux criado com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Grupo de Segurança: {e}"}), 500

# Função para criar Grupo de Segurança Windows na Azure
@app.route('/azure/criar-grupo-seguranca-windows', methods=['POST'])
def criar_grupo_seguranca_windows_azure():
    terraform_dir = './azure/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_network_security_group.Grupo_de_Seguranca_Windows'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Grupo de Segurança Windows criado com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Grupo de Segurança: {e}"}), 500

# Função para criar Interface de IP Público Linux na Azure
@app.route('/azure/criar-interface-ip-linux', methods=['POST'])
def criar_interface_ip_linux_azure():
    terraform_dir = './azure/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_public_ip.public_ip_linux', '-target=azurerm_network_interface.Interface_de_rede_Linux'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Interface de IP Público Linux criada e associada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Interface de IP Público Linux: {e}"}), 500

# Função para criar Interface de IP Público Windows na Azure
@app.route('/azure/criar-interface-ip-windows', methods=['POST'])
def criar_interface_ip_windows_azure():
    terraform_dir = './azure/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_public_ip.public_ip_windows', '-target=azurerm_network_interface.Interface_de_rede_Windows'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Interface de IP Público Windows criada e associada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Interface de IP Público Windows: {e}"}), 500

# Função para criar Máquina Virtual Linux na Azure
@app.route('/azure/criar-maquina-virtual-linux', methods=['POST'])
def criar_maquina_virtual_linux_azure():
    terraform_dir = './azure/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_linux_virtual_machine.linux'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Máquina Virtual Linux criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Máquina Virtual Linux: {e}"}), 500

# Função para criar Máquina Virtual Windows na Azure
@app.route('/azure/criar-maquina-virtual-windows', methods=['POST'])
def criar_maquina_virtual_windows_azure():
    terraform_dir = './azure/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=azurerm_windows_virtual_machine.windows'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Máquina Virtual Windows criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Máquina Virtual Windows: {e}"}), 500

# ----------------------------------------------------AWS-----------------------------------------------------------#

# Função para criar VPC na AWS
@app.route('/aws/VPC', methods=['POST'])
def criar_vpc_aws():
    terraform_dir = './aws/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_vpc.vpc'], cwd=terraform_dir, check=True)
        return jsonify({"message": "VPC criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar VPC: {e}"}), 500

# Função para criar Subrede Pública na AWS
@app.route('/aws/Subrede Pública', methods=['POST'])
def criar_subrede_publica_aws():
    terraform_dir = './aws/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_subnet.Subrede_Publica'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Subrede Pública criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Subrede Pública: {e}"}), 500

# Função para criar Subrede Privada na AWS
@app.route('/aws/Subrede Privada', methods=['POST'])
def criar_subrede_privada_aws():
    terraform_dir = './aws/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_subnet.Subrede_Privada'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Subrede Privada criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Subrede Privada: {e}"}), 500

# Função para criar Gateway de Internet na AWS
@app.route('/aws/Gateway', methods=['POST'])
def criar_gateway_internet_aws():
    terraform_dir = './aws/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_internet_gateway.igw'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Gateway de Internet criado com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Gateway de Internet: {e}"}), 500

# Função para criar Tabela de Rotas na AWS
@app.route('/aws/Tabela de Rota', methods=['POST'])
def criar_tabela_rotas_aws():
    terraform_dir = './aws/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_route_table.public'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Tabela de Rotas criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Tabela de Rotas: {e}"}), 500

# Função para associar subrede pública à tabela de rotas na AWS
@app.route('/aws/Associar Tabela de Rota', methods=['POST'])
def associar_subrede_tabela_aws():
    terraform_dir = './aws/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_route_table_association.public'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Subrede Pública associada à Tabela de Rotas com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao associar Subrede Pública à Tabela de Rotas: {e}"}), 500

# Função para criar Grupo de Segurança Linux na AWS
@app.route('/aws/Grupo de Segurança Linux', methods=['POST'])
def criar_grupo_seguranca_linux_aws():
    terraform_dir = './aws/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_security_group.Grupo_de_Seguranca_LInux'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Grupo de Segurança criado com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Grupo de Segurança: {e}"}), 500

# Função para criar Grupo de Segurança Windows na AWS
@app.route('/aws/Grupo de Segurança Windows', methods=['POST'])
def criar_grupo_seguranca_windows_aws():
    terraform_dir = './aws/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_security_group.Grupo_de_Seguranca_Windows'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Grupo de Segurança criado com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Grupo de Segurança: {e}"}), 500

# Função para criar instância EC2 Linux na AWS
@app.route('/aws/Máquina Virtual Windows', methods=['POST'])
def criar_instancia_ec2_linux_aws():
    terraform_dir = './aws/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_instance.linux'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Instância EC2 Linux criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Instância EC2 Linux: {e}"}), 500

# Função para criar instância EC2 Windows na AWS
@app.route('/aws/Máquina Virtual Linux', methods=['POST'])
def criar_instancia_ec2_windows_aws():
    terraform_dir = './aws/'
    try:
        subprocess.run(['terraform', 'apply', '-auto-approve', '-target=aws_instance.windows'], cwd=terraform_dir, check=True)
        return jsonify({"message": "Instância EC2 Windows criada com sucesso!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Erro ao criar Instância EC2 Windows: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
