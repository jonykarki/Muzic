import torch
import torch.nn as nn

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, out_class_size):
        super(RNN, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.out_class_size = out_class_size

        self.embedding = nn.Embedding(input_size, hidden_size)
        self.lstm = nn.LSTM(hidden_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, out_class_size)

    def forward(self, X):
        out = self.embedding(X)
        out, _ = self.lstm(out.unsqueeze(1))
        out = self.fc(out.view(-1, self.hidden_size))
        return out