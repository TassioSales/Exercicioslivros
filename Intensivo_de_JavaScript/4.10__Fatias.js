/*"""Usando um dos programas que você escreveu neste capítulo,
acrescente várias linhas no final do programa que façam o seguinte: • Exiba a
mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para
exibir os três primeiros itens da lista desse programa.
• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir
três itens do meio da lista.
• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para
exibir os três últimos itens da lista.""" */

dogs_name = ['Swam', 'Noki', 'Luca', 'Dandara', 'Mila', 'Dani', 'Negão', 'Dipsi', 'Taigo', 'Oke', 'Mancha']

console.log(`Os Três primeiros itens da lista são: ${dogs_name.slice(0,3)}`)
console.log(`OS Três itens do meio da lista são: ${dogs_name.slice(4,7)}`)
console.log(`OS Três ultimos do meio da lista são: ${dogs_name.slice(8,11)}`)