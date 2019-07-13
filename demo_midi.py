import torch
import torch.nn as nn
import torch.optim
from torch.autograd import Variable

from mido import MidiFile,MidiTrack,Message

import matplotlib.pyplot as plt
import numpy as np

mid = MidiFile('./TS.mid')
for msg in mid:
	······

	if msg.type == 'note_on':
		note = msg.bytes()
		note = note[1:3]
		note.append(time - prev)
		prev = time
		notes.append(note)


def LSTMNETwork(nn.Module):
	def __init__(self, input_size, hidden_size, out_size, n_layers=1):
		·····
		self.lstm = nn.LSTM(input_size, hidden_size, n_layers, batch_first = True)
		·····

	def forward(self, input, hidden=None):
		hhh1 = hidden[0]
		hhh1 = self.lstm(input, hhh1)
		······


		x = self.softmax(out[:, :89])
		y = self.softmax(out[:, 89:89+128])
		z = self.softmax(out[:, 89+128:])
		return x, y, z



def criterion(outputs, target):
	x, y, z = outputs
	loss_f = nn.NLLLoss()
	loss1 = loss_f(x, target[:, 0])
	loss2 = loss_f(y, target[:, 1])
	loss3 = loss_f(z, target[:, 2])
	return loss1 + loss2 + loss3


pred_steps = 3000
seed = dataset[0:30]
x = seed
······
for i in range(pred_steps):
	xx = Variable(torch.FloatTensor(np.array(x, dtype = float)))
	preds = lstm(xx, initi)
	······
	x = np.concatenate((x, slot1), 1)


