# falta ___init___, models, pycache

from sklearn.ensemble import RandomForestClassifier
from acppred.models import Model

def main():
    model = Model(
        estimator=RandomForestClassifier(),
        positive_peptides='data/raw/positive.txt',
        negative_peptides='data/raw/negative.txt'
    )

    model.train()
    model.save('data/models/model.pickle')

# verificar quantidade de _______ neste trecho, com o doc do fred
if __name__ == '__main__':
    main()
