

// yo mero
function calcularVolumenVacio(radioEsfera) {

    const pi = 3.14
    const radioCilindro = radioEsfera
    const alturaCilindro = 2 * radioEsfera
    const volumenCilindro = pi * radioCilindro ** 2 * alturaCilindro
  
    const volumenEsfera = (4 / 3) * pi * radioEsfera ** 3
  
    const volumenVacio = volumenCilindro - volumenEsfera
  
    return volumenVacio
  }

  // gpt
function volumenVacioLata(radio) {
    const pi = 3.14
    const altura = 2 * radio
    
    const volumenCilindro = pi * Math.pow(radio, 2) * altura
    
    const volumenEsfera = (4 / 3) * pi * Math.pow(radio, 3)
    
    const volumenVacio = volumenCilindro - volumenEsfera
    
    return parseFloat(volumenVacio.toFixed(2))
}

  function calcularVolumenVacio(radioEsfera) {
    const pi = 3.14
    const radioCilindro = radioEsfera
    const alturaCilindro = 2 * radioEsfera
    const volumenCilindro = pi * radioCilindro ** 2 * alturaCilindro
  
    const volumenEsfera = (4 / 3) * pi * radioEsfera ** 3
  
    const volumenVacio = volumenCilindro - volumenEsfera
  
    return volumenVacio
  }