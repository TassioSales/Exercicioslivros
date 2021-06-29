"""Um dicionário Python pode ser usado para modelar um
dicionário de verdade. No entanto, para evitar confusão, vamos chamá-lo de
glossário.
• Pense em cinco palavras relacionadas à programação que você conheceu
nos capítulos anteriores. Use essas palavras como chaves em seu glossário e
armazene seus significados como valores.
• Mostre cada palavra e seu significado em uma saída formatada de modo
elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu
significado, ou apresentar a palavra em uma linha e então exibir seu
significado indentado em uma segunda linha. Utilize o caractere de quebra
de linha (n) para inserir uma linha em branco entre cada par palavrasignificado em sua saída"""

glosario = {
            "python":' é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.',
            "java":" é o ambiente computacional, ou plataforma, criada pela empresa estadunidense Sun Microsystems, e vendida para a Oracle depois de alguns anos. A plataforma permite desenvolver programas utilizando a linguagem de programação Java.",
            "C":" é uma linguagem de programação compilada de propósito geral, estruturada, imperativa, procedural, padronizada pela Organização Internacional para Padronização, criada em 1972 por Dennis Ritchie na empresa AT&T Bell Labs para desenvolvimento do sistema operacional Unix.",
            "R":" é uma linguagem de programação multi-paradigma orientada a objetos, programação funcional, dinâmica, fracamente tipada, voltada à manipulação, análise e visualização de dados. Foi criado originalmente por Ross Ihaka e por Robert Gentleman no departamento de Estatística da Universidade de Auckland, Nova Zelândia",
            "HTML":" abreviação para a expressão inglesa HyperText Markup Language, que significa: Linguagem de Marcação de Hipertexto é uma linguagem de marcação utilizada na construção de páginas na Web. Documentos HTML podem ser interpretados por navegadores. A tecnologia é fruto da junção entre os padrões HyTime e SGML.",
            "JavaScript":" é uma linguagem de programação interpretada estruturada, de script em alto nível com tipagem dinâmica fraca e multiparadigma. Juntamente com HTML e CSS, o JavaScript é uma das três principais tecnologias da World Wide Web."}

for linguagem in glosario:
    print(f'{linguagem}: {glosario[linguagem]} \n' )