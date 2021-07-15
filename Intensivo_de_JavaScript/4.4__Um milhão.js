/*"""Crie uma lista de números de um a um milhão e, então, use um
laço for para exibir os números. (Se a saída estiver demorando demais,
interrompa pressionando CTRL-C ou feche a janela de saída.) 4.5 – Somando um
milhão: Crie uma lista de números de um a um milhão e, em seguida, use min()
e max() para garantir que sua lista realmente começa em um e termina em um
milhão. Além disso, utilize a função sum() para ver a rapidez com que Python é
capaz de somar um milhão de números.
""" */


let listaNum = []

for (let i = 1; i < 1000001; i++) {
    listaNum.push(i)   
}

console.log(listaNum.reduce((a,b)=>Math.max(a,b)))
console.log(listaNum.reduce((a,b)=>Math.min(a,b)))
const total = listaNum.reduce((total, currentElement) => total + currentElement)
console.log(total)