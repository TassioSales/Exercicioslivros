/*Pense em pelo menos três animais diferentes que tenham uma
característica em comum. Armazene os nomes desses animais em uma lista e,
então, utilize um laço for para exibir o nome de cada animal.
• Modifique seu programa para exibir uma frase sobre cada animal, por
exemplo, Um cachorro seria um ótimo animal de estimação.
• Acrescente uma linha no final de seu programa informando o que esses
animais têm em comum. Você poderia exibir uma frase como Qualquer um
desses animais seria um ótimo animal de estimação!*/

var animais = ['Papagaio', 'Cachorro', 'Gato', 'Calopsita']

for(animal in animais){
    if (animais[animal] == "Papagaio"){
        console.log(`O ${animais[animal]} fala demais`);
    }else if (animais[animal] == "Cachorro"){
        console.log(`O ${animais[animal]} e o melhor amigo do homen`)
    }else if (animais[animal] == "Gato"){
        console.log(`O ${animais[animal]} e o mais independente`)
    }else if (animais[animal] == "Calopsita"){
        console.log(`A ${animais[animal]} canta muito`)
    }
}