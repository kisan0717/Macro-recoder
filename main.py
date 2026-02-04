import pynput as pnp
import time

class Macro:
	def __init__(self):
		self.recs = {}
		self.mouse = pnp.mouse.Controller()
		self.recDispatch = {
			'mov': self.mov
		}

		self.listener = pnp.mouse.Listener(
    	on_move = self.on_move,
    	on_click = self.on_click,
    	on_scroll = self.on_scroll
		)

		self.listener.start()

		self.active = False
		self.currentRec = ''

	def on_move(self, x, y, injected):
		if not self.active: return
		self.recs[self.currentRec].append(
			{
				'x': x,
				'y': y,
				'action': 'mov'
			}
		)

	def on_click(self, x, y, button, pressed, injected):
		pass

	def on_scroll(self, x, y, dx, dy, injected):
		pass

	def start(self, rec_name: str, delay: int = 0):
		time.sleep(delay)
		print('started recording')
		self.recs[rec_name] = []
		self.currentRec = rec_name
		self.active = True

	def stop(self):
		self.active = False	

	def mov(self, action: dict):
		self.mouse.position = (action['x'], action['y'])


	def playback(self, rec_name: str):
		rec = self.recs[rec_name]
		
		for action in rec:
			self.recDispatch[action['action']](action)
			time.sleep(0.16)

m1 = Macro()

m1.start('rec1', 1)
time.sleep(1)
m1.stop()
print('recording stop')
time.sleep(1)
print('playback started')
m1.playback('rec1')
print('stop')