from acppred.models import Model

def main():
    model = Model.load('data/models/model.pickle')
    sequence = input('peptide sequence: ')
    prediction = model.predict(sequence)

    print(prediction)

# verificar quantidade de _______ neste trecho, com o doc do fred
if __name__ == '__main__':
    main()
