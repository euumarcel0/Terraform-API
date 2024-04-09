//THIS APP IS NOT THE EXACT COPY OF THE APP STORE BUT IS SIMILAR TO IT ;).... and btw inspired by Aysenur Turk's pen (who i follow A LOT).

const side_bar_btns = document.querySelectorAll("#sidebar-btn");


side_bar_btns.forEach((elem) => {
  elem.addEventListener("click", () => {
    for (let index = 0; index < side_bar_btns.length; index++) {
      side_bar_btns[index].classList.remove("active");
    }
    elem.classList.add("active");
  });
});

let min = true;

// ----------------------------------------------------AZURE----------------------------------------------------------- //

// Função para criar recursos na Azure
async function criarRecursosAzure(recurso) {
  try {
      const response = await fetch(`http://localhost:5000/azure/${recurso}`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({})
      });

      if (!response.ok) {
          throw new Error(`Erro ao criar ${recurso} na Azure`);
      }

      const data = await response.json();
      console.log(data.message); // Você pode fazer algo mais com a mensagem, como exibir em um modal, por exemplo
      
      // Atualiza o conteúdo do modal com o resultado
      document.getElementById('modal-message').innerText = data.message;
      
      // Abre o modal
      openModal();
  } catch (error) {
      console.error(error);
      // Tratar o erro aqui, como exibir uma mensagem de erro para o usuário
      
      // Atualiza o conteúdo do modal com a mensagem de erro
      document.getElementById('modal-message').innerText = error.message;
      
      // Abre o modal
      openModal();
  }
}

// Event listener para o botão de criar Grupo de Recursos
document.getElementById('grupo-recursos-btn').addEventListener('click', function() {
  criarRecursosAzure('criar-grupo-recursos');
});

// Event listener para o botão de criar Conta de Armazenamento
document.getElementById('conta-armazenamento-btn').addEventListener('click', function() {
  criarRecursosAzure('criar-conta-armazenamento');
});

// Event listener para o botão de criar VNET
document.getElementById('vnet-btn').addEventListener('click', function() {
  criarRecursosAzure('criar-vnet');
});

// Event listener para o botão de criar Subrede Pública
document.getElementById('subnet-publica-btn').addEventListener('click', function() {
  criarRecursosAzure('criar-subrede-publica');
});

// Event listener para o botão de criar Subrede Privada
document.getElementById('subnet-privada-btn').addEventListener('click', function() {
  criarRecursosAzure('criar-subrede-privada');
});

// Event listener para o botão de criar Grupo de Segurança
document.getElementById('grupo-seguranca-btn').addEventListener('click', function() {
  criarRecursosAzure('criar-grupo-seguranca-linux');
});

// Event listener para o botão de criar IP Público Linux
document.getElementById('ip-publico-linux-btn').addEventListener('click', function() {
  criarRecursosAzure('criar-interface-ip-linux');
});

// Event listener para o botão de criar IP Público Windows
document.getElementById('ip-publico-windows-btn').addEventListener('click', function() {
  criarRecursosAzure('criar-interface-ip-windows');
});

// Event listener para o botão de criar Interface de Rede Linux
document.getElementById('interface-rede-linux-btn').addEventListener('click', function() {
  criarRecursosAzure('criar-interface-ip-linux');
});

// Event listener para o botão de criar Interface de Rede Windows
document.getElementById('interface-rede-windows-btn').addEventListener('click', function() {
  criarRecursosAzure('criar-interface-ip-windows');
});

// Event listener para o botão de criar Máquina Virtual Linux
document.getElementById('maquina-virtual-linux-btn').addEventListener('click', function() {
  criarRecursosAzure('criar-maquina-virtual-linux');
});

// Event listener para o botão de criar Máquina Virtual Windows
document.getElementById('maquina-virtual-windows-btn').addEventListener('click', function() {
  criarRecursosAzure('criar-maquina-virtual-windows');
});

// ----------------------------------------------------AWS---------------------------------------------------------- //

// Função para criar recursos na AWS
async function criarRecursosAWS(recurso) {
  try {
      const response = await fetch(`http://localhost:5000/aws/${recurso}`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({})
      });

      if (!response.ok) {
          throw new Error(`Erro ao criar ${recurso} na AWS`);
      }

      const data = await response.json();
      console.log(data.message); // Você pode fazer algo mais com a mensagem, como exibir em um modal, por exemplo
      
      // Atualiza o conteúdo do modal com o resultado
      document.getElementById('modal-message').innerText = data.message;
      
      // Abre o modal
      openModal();
  } catch (error) {
      console.error(error);
      // Tratar o erro aqui, como exibir uma mensagem de erro para o usuário
      
      // Atualiza o conteúdo do modal com a mensagem de erro
      document.getElementById('modal-message').innerText = error.message;
      
      // Abre o modal
      openModal();
  }
}

// Event listener para o botão de criar VPC na AWS
document.getElementById('aws-vpc-btn').addEventListener('click', function() {
  criarRecursosAWS('VPC');
});

// Event listener para o botão de criar Subrede Pública na AWS
document.getElementById('aws-subnet-publica-btn').addEventListener('click', function() {
  criarRecursosAWS('SubPub');
});

// Event listener para o botão de criar Subrede Privada na AWS
document.getElementById('aws-subnet-privada-btn').addEventListener('click', function() {
  criarRecursosAWS('SubPriv');
});

// Event listener para o botão de criar Gateway de Internet na AWS
document.getElementById('aws-gateway-btn').addEventListener('click', function() {
  criarRecursosAWS('gtw');
});

// Event listener para o botão de criar Tabela de Rotas na AWS
document.getElementById('aws-tabela-rota-btn').addEventListener('click', function() {
  criarRecursosAWS('tabela');
});

// Event listener para o botão de associar Subrede à Tabela de Rotas na AWS
document.getElementById('aws-associar-tabela-rota-btn').addEventListener('click', function() {
  criarRecursosAWS('associartb');
});

// Event listener para o botão de criar Grupo de Segurança Linux na AWS
document.getElementById('aws-grupo-seguranca-linux-btn').addEventListener('click', function() {
  criarRecursosAWS('GSlinux');
});

// Event listener para o botão de criar Grupo de Segurança Windows na AWS
document.getElementById('aws-grupo-seguranca-windows-btn').addEventListener('click', function() {
  criarRecursosAWS('GSwindows');
});

// Event listener para o botão de criar Máquina Virtual Linux na AWS
document.getElementById('aws-maquina-virtual-linux-btn').addEventListener('click', function() {
  criarRecursosAWS('EC2linux');
});

// Event listener para o botão de criar Máquina Virtual Windows na AWS
document.getElementById('aws-maquina-virtual-windows-btn').addEventListener('click', function() {
  criarRecursosAWS('EC2windows');
});


// ----------------------------------------------------MODAL----------------------------------------------------------- //

// Função para abrir o modal
function openModal() {
  document.getElementById('modal-content').style.display = "block"; // Mostra o modal
  document.body.classList.add('modal-open'); // Adiciona a classe modal-open ao body
}

// Função para fechar o modal
function closeModal() {
  document.getElementById('modal-message').innerText = ''; // Limpa o conteúdo do modal
  document.getElementById('modal-content').style.display = "none"; // Esconde o modal
  document.body.classList.remove('modal-open'); // Remove a classe modal-open do body
}

// Adicionar um ouvinte de evento para fechar o modal quando o usuário clicar fora dele
document.addEventListener('DOMContentLoaded', function() {
  const modalContent = document.getElementById('modal-content');
  const closeModalButton = document.getElementById('close-modal');

  closeModalButton.addEventListener('click', closeModal);

  // Ajuste no ouvinte de evento para fechar o modal quando o usuário clicar fora dele
  window.onclick = function(event) {
      if (event.target == modalContent) { // Certifique-se de que o ID do modal esteja correto
          closeModal();
      }
  }
});

document.addEventListener('click', function(event) {
  if (event.target == modalContent) {
      closeModal();
  }
});