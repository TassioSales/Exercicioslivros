/*""" Use o terceiro argumento da função range() para criar
uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos
os números."""  */

let listaImpares = []

for(var i = 1; i < 20; i++){
    if (i % 2 != 0) {
        listaImpares.push(i)
    }
}
console.log(listaImpares)