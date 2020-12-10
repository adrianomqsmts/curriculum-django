function typeWrite(elemento) {
  const textoArray = elemento.innerHTML.split('');
  const tamanho = textoArray.length;
  elemento.innerHTML = '';
  textoArray.forEach(function (letra, i) {

    setTimeout(function () {
      elemento.innerHTML += letra;
    }, 100 * i)

  });
}

