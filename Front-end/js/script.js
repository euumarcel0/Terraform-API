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

document.querySelector(".window__close").addEventListener("click", () => {
  document.querySelector(".container").style.display = "none";

  setTimeout(() => {
    window.alert(
      "Oh No! What did you do? Now you have to refresh to open the app again"
    );
  }, 500);
});

document.querySelector(".window__maximize").addEventListener("click", () => {
  if (min == false) {
    min = true;
    console.log(min);
    document.querySelector(".container").style.width = "90%";
    document.querySelector(".container").style.height = "90%";
  } else {
    min = false;
    document.querySelector(".container").style.width = "100%";
    document.querySelector(".container").style.height = "100%";
  }
});

document.querySelector(".window__minimize").addEventListener("click", () => {
  console.log("hello world");

  document.querySelector(".container").style.transform = "scale(0)";

  setTimeout(() => {
    window.alert(
      "The app is minimized but cannot be opened again because the virtual codepen macos crashed!"
    );
  }, 500);
});

// Função para criar Grupo de Recursos
async function criarRecursosAzure(recursos) {
  try {
      const response = await fetch("http://localhost:5000/api", {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({
              platform: 'azure',
              resources_to_create: recursos
          })
      });

      if (!response.ok) {
          throw new Error('Erro ao criar recursos da Azure');
      }

      const data = await response.json();
      console.log(data.message); // Você pode fazer algo mais com a mensagem, como exibir em um modal, por exemplo
  } catch (error) {
      console.error(error);
      // Tratar o erro aqui, como exibir uma mensagem de erro para o usuário
  }
}

// Event listener para o botão de criar Grupo de Recursos
document.getElementById('grupo-recursos-btn').addEventListener('click', function() {
  criarRecursosAzure(['resource_group']);
});

// Event listener para o botão de criar Conta de Armazenamento
document.getElementById('conta-armazenamento-btn').addEventListener('click', function() {
  criarRecursosAzure(['storage_account']);
});

// Event listener para o botão de criar VNET
document.getElementById('vnet-btn').addEventListener('click', function() {
  criarRecursosAzure(['virtual_network']);
});

// Event listener para o botão de criar Subrede Pública
document.getElementById('subnet-publica-btn').addEventListener('click', function() {
  criarRecursosAzure(['subnet_publica']);
});

// Event listener para o botão de criar Subrede Privada
document.getElementById('subnet-privada-btn').addEventListener('click', function() {
  criarRecursosAzure(['subnet_privada']);
});

// Event listener para o botão de criar Grupo de Segurança
document.getElementById('grupo-seguranca-btn').addEventListener('click', function() {
  criarRecursosAzure(['network_security_group']);
});

// Event listener para o botão de criar IP Público Linux
document.getElementById('ip-publico-linux-btn').addEventListener('click', function() {
  criarRecursosAzure(['public_ip_linux']);
});

// Event listener para o botão de criar IP Público Windows
document.getElementById('ip-publico-windows-btn').addEventListener('click', function() {
  criarRecursosAzure(['public_ip_windows']);
});

// Event listener para o botão de criar Interface de Rede Linux
document.getElementById('interface-rede-linux-btn').addEventListener('click', function() {
  criarRecursosAzure(['interface_de_rede_linux']);
});

// Event listener para o botão de criar Interface de Rede Windows
document.getElementById('interface-rede-windows-btn').addEventListener('click', function() {
  criarRecursosAzure(['interface_de_rede_windows']);
});

// Event listener para o botão de criar Máquina Virtual Linux
document.getElementById('maquina-virtual-linux-btn').addEventListener('click', function() {
  criarRecursosAzure(['linux_virtual_machine']);
});

// Event listener para o botão de criar Máquina Virtual Windows
document.getElementById('maquina-virtual-windows-btn').addEventListener('click', function() {
  criarRecursosAzure(['windows_virtual_machine']);
});

