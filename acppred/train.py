# falta ___init___, models, pycache

from sklearn.ensemble import RandomForestClassifier
from acppred.models import Model
from argparse import ArgumentParser

# posso colocar as variaveis aqui, ou no UTILS.PY e importar elas, depende de como quiser utilizar e de como forem necessárias durante o código
default_positive_file='data/raw/positive.txt'
default_negative_file='data/raw/negative.txt'

def main():
    argument_parser = ArgumentParser(description='Trains a anticancer peptide classification model')
    argument_parser.add_argument(
        '--positive-peptides',
        default=default_positive_file,
        help='a file containing anticancer peptides'
    )
    argument_parser.add_argument(
        '--negative-peptides',
        default=default_negative_file,
        help='a file containing non-anticancer peptides'
    )
    argument_parser.add_argument(
        '--output',
        help='path to the output trained model',
        required=True   
    )
    argument_parser.add_argument(
        '--show-report',
        help='shows the classification report after training',
        action='store_true'
    )
    arguments = argument_parser.parse_args()

    model = Model(
        estimator=RandomForestClassifier(),
        positive_peptides=arguments.positive_peptides,
        negative_peptides=arguments.negative_peptides
    )

    report = model.train()

    if arguments.show_report:
        print(report)

    model.save('data/models/model.pickle')

# quantidade de _______ neste trecho (são 2 __)
# TRAIN É O PRIMEIRO PARA TREINAR O MODELO, DEPOIS PREDICT PRA USAR O MODELO TREINADO.

if __name__ == '__main__':
    main()
