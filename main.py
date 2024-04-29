from Vector import Vector


def VectorRead(file_name):
    with open(file_name) as f:
        vectors = [Vector(line.split()) for line in f.readlines()]
    return vectors


def analyze_vectors(vectors):

    maxdimension = 0
    for vector in vectors:
        if vector.dimension() > maxdimension:
            maxdimension = vector.dimension()

    maxdimenvectors = []
    for vector in vectors:
        if vector.dimension() == maxdimension:
            maxdimenvectors.append(vector)

    smallestlength = float('inf')
    smallestlengthvector = []
    for vector in maxdimenvectors:
        if vector.length() < smallestlength:
            smallestlength = vector.length()
            smallestlengthvector = vector



    maxlength = max(el.length() for el in vectors)

    maxlengthvectors = [el for el in vectors if el.length() == maxlength]

    smallestdimensionvector = min(maxlengthvectors, key=lambda el: el.dimension())



    averagelength = sum(el.length() for el in vectors) / len(vectors)

    vectorsaboveaverage = [el for el in vectors if el.length() > averagelength]



    maxcomponentvalue = max(el.max_component() for el in vectors)

    maxcompvectors = [el for el in vectors if el.max_component() == maxcomponentvalue]

    mincompvector = min(maxcompvectors, key=lambda el: el.min_component())



    maxcomponentvalue = max(el.max_component() for el in vectors)

    vectorswithmaxcomponent = [el for el in vectors if el.max_component() == maxcomponentvalue]

    vectorwithmincomponent = min(vectorswithmaxcomponent, key=lambda el: el.min_component())

    print("Вектор з найбільшою розмірністю та найменшою довжиною", smallestlengthvector)
    print("Вектор з найбільшою довжиною та найменшою розмірністю", smallestdimensionvector)
    print("Середня довжина векторів", averagelength)
    print("Кількість векторів з довжиною вище середнього", len(vectorsaboveaverage))
    print("Вектор з максимальною найбільшою компонентою", mincompvector)
    print("Вектор з мінімальною найменшою компонентою", vectorwithmincomponent)




filenames = ["input01.txt", "input02.txt", "input03.txt", "input04.txt"]
for filename in filenames:
    print("Файл", filename)
    vectors = VectorRead(filename)
    analyze_vectors(vectors)

