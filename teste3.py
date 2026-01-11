<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>irei voltar com minha ex?</title>

  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin-top: 100px;
    }

    #nao {
      position: absolute;
    }
  </style>
</head>
<body>

  <h2>vou voltar com minha ex?</h2>

  <button onclick="sim()">Sim</button>
  <button id="nao" onmouseover="fugir()">Não</button>

  <p id="resposta"></p>

  <script>
    function sim() {
      document.getElementById("resposta").innerText =
        "AMÉMMMM";
    }

    function fugir() {
      const botao = document.getElementById("nao");

      const largura = window.innerWidth - 100;
      const altura = window.innerHeight - 50;

      const x = Math.random() * largura;
      const y = Math.random() * altura;

      botao.style.left = x + "px";
      botao.style.top = y + "px";
    }
  </script>

</body>
</html>