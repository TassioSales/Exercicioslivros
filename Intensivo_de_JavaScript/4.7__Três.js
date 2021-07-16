/*"""Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
exibir os números de sua lista.""" */

var listaMultiploDeTres = []

for(var i = 3; i < 30; i++){
    if(i % 3 == 0){
        listaMultiploDeTres.push(i)
    }
}

console.log(listaMultiploDeTres)