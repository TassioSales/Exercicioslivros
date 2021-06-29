"""Agora que você já sabe como percorrer um dicionário com
um laço, limpe o código do Exercício 6.3 (página 148), substituindo sua
sequência de instruções print por um laço que percorra as chaves e os valores
do dicionário. Quando tiver certeza de que seu laço funciona, acrescente mais
cinco termos de Python ao seu glossário. Ao executar seu programa novamente,
essas palavras e significados novos deverão ser automaticamente incluídos na
saída.

"""
glosario = {
            "python":' é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.',
            "java":" é o ambiente computacional, ou plataforma, criada pela empresa estadunidense Sun Microsystems, e vendida para a Oracle depois de alguns anos. A plataforma permite desenvolver programas utilizando a linguagem de programação Java.",
            "C":" é uma linguagem de programação compilada de propósito geral, estruturada, imperativa, procedural, padronizada pela Organização Internacional para Padronização, criada em 1972 por Dennis Ritchie na empresa AT&T Bell Labs para desenvolvimento do sistema operacional Unix.",
            "R":" é uma linguagem de programação multi-paradigma orientada a objetos, programação funcional, dinâmica, fracamente tipada, voltada à manipulação, análise e visualização de dados. Foi criado originalmente por Ross Ihaka e por Robert Gentleman no departamento de Estatística da Universidade de Auckland, Nova Zelândia",
            "HTML":" abreviação para a expressão inglesa HyperText Markup Language, que significa: Linguagem de Marcação de Hipertexto é uma linguagem de marcação utilizada na construção de páginas na Web. Documentos HTML podem ser interpretados por navegadores. A tecnologia é fruto da junção entre os padrões HyTime e SGML.",
            "JavaScript":" é uma linguagem de programação interpretada estruturada, de script em alto nível com tipagem dinâmica fraca e multiparadigma. Juntamente com HTML e CSS, o JavaScript é uma das três principais tecnologias da World Wide Web."}


for v, a in enumerate(glosario):
    print(f'{v+1} {a} {glosario[a]}')
    