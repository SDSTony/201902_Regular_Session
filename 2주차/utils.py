import numpy as np
import sys
sys.path.append('..')

class Grader():
    def __init__(self):
        self.part_names = [
        'Feature Normalization',
        'Computing Cost (for multiple variables)',
        'Gradient Descent (for multiple variables)',
        'Normal Equations'
        ]
        self.answer = {0:None, 1:None, 2:None, 3:None}
        self.correct = {0:self._correct_00, 1:self._correct_01, 2:self._correct_02, 3:self._correct_03}
        self.X1 = np.column_stack((np.ones(20), np.exp(1) + np.exp(2) * np.linspace(0.1, 2, 20)))
        self.Y1 = self.X1[:, 1] + np.sin(self.X1[:, 0]) + np.cos(self.X1[:, 1])
        self.X2 = np.column_stack((self.X1, self.X1[:, 1]**0.5, self.X1[:, 1]**0.25))
        self.Y2 = np.power(self.Y1, 0.5) + self.Y1

    def grade(self, num):
        self.correct[num](self.answer[num])

    def _correct_00(self, answer):
        def normalize(X):
            mu = X.mean(axis=0)
            sigma = X.std(axis=0)
            X = (X - mu) / sigma
            return X
        answer = answer(self.X2[:,1:])[0]
        correct = normalize(self.X2[:,1:])
        if np.mean(answer == correct) == 1:
            print('정답')
        else:
            print('오답')

    def _correct_01(self, answer):
        answer = answer(self.X2, self.Y2, np.array([0.1, 0.2, 0.3, 0.4]))
        answer = round(answer, 3)
        if answer == 64.382:
            print('정답')
        else:
            print('오답')

    def _correct_02(self, answer):
        theta, J_history = answer(self.X2, self.Y2, np.array([-0.1, -0.2, -0.3, -0.4]), 0.01, 10)
        theta = np.array([round(x, 3) for x in theta])
        correct = np.array([0.061, 1.316, 0.184, -0.122])
        if np.mean(theta == correct) == 1:
            print('정답')
        else:
            print('오답')

    def _correct_03(self, answer):
        answer = answer(self.X2, self.Y2)
        answer = np.array([round(x, 3) for x in answer])
        correct = np.array([-120.815, 5.064, -77.734, 185.693])
        if np.mean(answer == correct) == 1:
            print('정답')
        else:
            print('오답')
