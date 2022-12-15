# clases de bibliotecas
from Bio.SeqUtils import ProtParam
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from acppred.utils import ALLOWED_AMINOACIDS
import pandas as pd
import pickle


# sao classes que vao construindo e depois criam os metodos 

class Model:
    def __init__(self, estimator, positive_peptides, negative_peptides):
        """
        This class defines and train an estimator for anticancer peptides prediction

        Args:
            - estimator: a scikit_learn estimator
            - positive_peptides: a file containing anticancer peptides
            - negative_peptides: a file containing non-anticancer peptides
        """
        self.estimator = estimator
        self.positive_peptides = positive_peptides
        self.negative_peptides = negative_peptides

    def transform(self, X):
        """
        Transform a set of protein sequences into aminoacids percents

        Args:
            - X: list of protein sequences
        """
        # no notebook jupyter essa variável X_transform é a peptide_data = []
        X_transform = []

        # essa função vai receber qualquer sequencia de proteinas, seja positiva ou negativa, e fazer a transformação do protparam 
        # Diferente da função do notebook que recebia e analisava separada, esta é uma função generalista.
        # A adição de label para positivo ou negativo fica pra depois, provavelmente pra quem chamar essa função a partir do
        # tipo de arquivo de origem
        for peptide in X:
            # testar se a sequência é composta de aminoacidos permitidos/validos - determinados dentro do utils.py (ALLOWED_AMINOACIDS)
            peptide = ''.join([aminoacid for aminoacid in peptide.upper() if aminoacid in ALLOWED_AMINOACIDS])
            aa_percent = ProtParam.ProteinAnalysis(peptide).get_amino_acids_percent()
            X_transform.append(aa_percent)
        
        return pd.DataFrame(X_transform)

    def train(self):
        """
        Trains a predictive model for anticancer peptides
        """
        X = []
        y = []

        with open(self.positive_peptides) as reader:
            for peptide in reader:
                X.append(peptide)
                y.append(1)
        
        with open(self.negative_peptides) as reader:
            for peptide in reader:
                X.append(peptide)
                y.append(0)
            
        X_transform = self.transform(X)

        X_train, X_test, y_train, y_test = train_test_split(X_transform, y)

        self.estimator.fit(X_train, y_train)
        y_pred = self.estimator.predict(X_test) # .predict é uma função dentro de RandomForestClassifier(), que é alocado na variavel 'estimator' do objeto
        report = classification_report(y_test, y_pred)

        return report 

    def predict(self, sequence):
        """
        Predicts the anticance activity for a given peptide
        
        Args:
            - sequence: a peptide sequence to be analyzed
        """
        X_transform = self.transform([sequence])
        return self.estimator.predict_proba(X_transform)[0][1]

    def save(self, filename):
        """
        Saves the model to a file

        Args:
            -filename  
        """
        with open (filename,'wb') as writer:
            writer.write(pickle.dumps(self))
    
    @staticmethod
    def load(filename):
      """
      Loads a trained model objects
      
      Args:
        - filename: path to the train model file
      """
      with open(filename,'rb') as reader:
        return pickle.loads(reader.read())
