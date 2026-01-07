# Month 11: Deep Learning Introduction

**Duration**: 4 weeks
**Focus**: Neural networks fundamentals

---

## Objectives

By the end of this month, you will:

- [ ] Understand neural network concepts
- [ ] Build models with PyTorch
- [ ] Train and evaluate neural networks
- [ ] Apply to image or text data
- [ ] Create a deep learning project

---

## Weekly Breakdown

| Week | Focus | Deliverables |
|------|-------|--------------|
| Week 1 | Neural Network Basics | Understanding NNs |
| Week 2 | PyTorch Fundamentals | First PyTorch model |
| Week 3 | Training & Optimization | Training pipeline |
| Week 4 | Project | DL application |

---

## Technologies

| Technology | Purpose |
|------------|---------|
| PyTorch | Deep learning |
| torchvision | Image datasets |
| Matplotlib | Visualization |

---

## Project: Image Classifier

Build an image classification model:

- Load image dataset
- Build neural network
- Train and validate
- Evaluate performance

---

## Key Concepts

### PyTorch Basics

```python
import torch
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super().__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        return x
```

### Training Loop

```python
model = SimpleNN(784, 128, 10)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for epoch in range(10):
    for inputs, labels in train_loader:
        outputs = model(inputs)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

### Evaluation

```python
model.eval()
correct = 0
total = 0

with torch.no_grad():
    for inputs, labels in test_loader:
        outputs = model(inputs)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = correct / total
```
