import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader

samples = 200
torch.manual_seed(42)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

x0 = torch.randn(samples, 2) + torch.tensor([-1.0, -1.0])
x1 = torch.randn(samples, 2) + torch.tensor([1.0, 1.0])

x = torch.cat([x0, x1], dim=0)
y = torch.cat([
    torch.zeros(samples),
    torch.ones(samples)
], dim=0)

class RandomDataset(Dataset):
    def __init__(self, x, y):
        self.x = x.float()
        self.y = y.long()

    def __len__(self):
        return len(self.x)
    
    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]
    
dataset = RandomDataset(x, y)

data_loader = DataLoader(
    dataset, batch_size=32, shuffle=True 
)

class MLP(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim)
        )

    def forward(self, x):
        return self.net(x)

model = MLP(input_dim=2, hidden_dim=16, output_dim=2).to(device)

def train_one_epoch(model, data_loader, optimizer, device):
    model.train()
    criterion = nn.CrossEntropyLoss()
    total_correct = 0
    total_samples = 0
    running_loss = 0.0

    for x_batch, y_batch in data_loader:
        x_batch = x_batch.to(device)
        y_batch = y_batch.to(device)

        y_pred = model(x_batch)
        loss = criterion(y_pred, y_batch)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        batch_size = x_batch.size(0)
        running_loss += loss.item() * batch_size

        preds = y_pred.argmax(dim=1)
        total_correct += (preds == y_batch).sum().item()
        total_samples += batch_size
    
    epoch_loss = running_loss / total_samples
    epoch_acc = total_correct / total_samples
    return epoch_loss, epoch_acc

epochs = 300
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(epochs):
    loss, acc = train_one_epoch(
        model, data_loader, optimizer, device
    )

    print(
        f"Epoch [{epoch + 1}/{epochs}] "
        f"loss={loss:.4f} "
        f"acc={acc:.4f} "
    )