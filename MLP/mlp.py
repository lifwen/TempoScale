import torch
import torch.nn as nn
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


data = pd.read_csv('ALL_TRAIN.csv',encoding='gbk')


X = data.iloc[:, 0:96].values
y = data.iloc[:, 96:].values



scaler_X = StandardScaler()
scaler_y = StandardScaler()

X1 = scaler_X.fit_transform(X)[:]
y1 = scaler_y.fit_transform(y)[:]


data = pd.read_csv('ALL_TEST.csv',encoding='gbk')

X = data.iloc[:, 0:96].values
y = data.iloc[:, 96:].values


X2 = scaler_X.fit_transform(X)[:]
y2 = scaler_y.fit_transform(y)[:]


X_train, X_test, y_train, y_test = train_test_split(X1, y1, test_size=0.001, random_state=42)


X_train_tensor = torch.Tensor(X_train)
y_train_tensor = torch.Tensor(y_train)
X_test_tensor = torch.Tensor(X_test)
y_test_tensor = torch.Tensor(y_test)


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(96, 192)
        # self.fc2 = nn.Linear(22, 44)
        # self.fc3 = nn.Linear(44, 66)
        self.fc4 = nn.Linear(192, 48)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        # x = torch.relu(self.fc2(x))
        # x = torch.relu(self.fc3(x))
        x = self.fc4(x)
        return x



model = NeuralNetwork()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)


epochs = 10000
for epoch in range(epochs):
    optimizer.zero_grad()
    output = model(X_train_tensor)
    loss = criterion(output, y_train_tensor)
    loss.backward()
    optimizer.step()
    if epoch % 100 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')


with torch.no_grad():
    test_output = model(X_test_tensor)
    test_loss = criterion(test_output, y_test_tensor)
    print(f'Test Loss: {test_loss.item():.4f}')


torch.save(model.state_dict(), 'model.pth')




# ---------------------------------------------------------------------------------------------------------------


import torch
import pandas as pd

import torch.nn as nn

model = NeuralNetwork()
model.load_state_dict(torch.load('model.pth'))
model.eval()

data_to_predict_scaled = X2


data_to_predict_tensor = torch.Tensor(data_to_predict_scaled)

with torch.no_grad():
    predictions = model(data_to_predict_tensor)

predicted_df = pd.DataFrame(predictions.numpy())

predicted_df = scaler_y.inverse_transform(predicted_df)

predicted_unscaled_df = pd.DataFrame(predicted_df)

pd.DataFrame(y[:]).to_csv('actual_results_unscaled.csv', index=False)

predicted_unscaled_df.to_csv('predicted_results_unscaled.csv', index=False)
# predicted_df.to_csv('predicted_results.csv', index=False)
