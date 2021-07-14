// """ Você acabou de descobrir que sua nova
// mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
// dois convidados.
// • Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
// mostre uma mensagem in`rmando que você pode convidar apenas duas
// pessoas para o jantar.
// • Utilize pop() para remover os convidados de sua lista, um de cada vez, até
// que apenas dois nomes permaneçam em sua lista. Sempre que remover um
// nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
// saiba que você sente muito por não poder convidá-la para o jantar.
// • Apresente uma mensagem para cada uma das duas pessoas que continuam
// na lista, permitindo que elas saibam que ainda estão convidadas.
// • Utilize del para remover os dois últimos nomes de sua lista, de modo que você
// tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
// uma lista vazia no `nal de seu programa.
// """

nomes_pessoas = ["Ana", "Maria", 'Jose']

console.log(`Gostaria de te convidar para um jantar ${nomes_pessoas[0]}`)
console.log(`Gostaria de te convidar para um jantar ${nomes_pessoas[1]}`)
console.log(`Gostaria de te convidar para um jantar ${nomes_pessoas[2]}`)

console.log(`Os convidados ${nomes_pessoas[0]}, ${nomes_pessoas[1]}, ${nomes_pessoas[2]} não iram comparacer\n`)


console.log('IREI CONVIDAR')
nomes_pessoas[0] = "Matheus"
nomes_pessoas[1] = "Lucas"
nomes_pessoas[2] = "Rodrigo"

console.log(`Gostaria de te convidar para um jantar ${nomes_pessoas[0]}`)
console.log(`Gostaria de te convidar para um jantar ${nomes_pessoas[1]}`)
console.log(`Gostaria de te convidar para um jantar ${nomes_pessoas[2]}`)

console.log('\n')

console.log("Encontrei uma mesa maior, irei chamar Tassio, Julia, Jhon")

nomes_pessoas.push("Tassio")
nomes_pessoas.push("Julia")
nomes_pessoas.push('Jhon')

console.log(`Gostaria de te convidar para um jantar ${nomes_pessoas[0]}`)
console.log(`Gostaria de te convidar para um jantar ${nomes_pessoas[4]}`)
console.log(`Gostaria de te convidar para um jantar ${nomes_pessoas[5]}`)

console.log('\n')

console.log('Devido a erros do restaurante irei apenas convidar so duas pessoas')


nomes_pessoas.pop(1)
nomes_pessoas.pop(2)
nomes_pessoas.pop(3)
nomes_pessoas.pop(4)

console.log('irei convidar apenas')
console.log(nomes_pessoas[0])
console.log(nomes_pessoas[1])

console.log(`Gostaria de te convidar para um jantar ${nomes_pessoas[0]}`)
console.log(`Gostaria de te convidar para um jantar ${nomes_pessoas[1]}`)

nomes_pessoas.pop()
nomes_pessoas.pop()
console.log(nomes_pessoas)


