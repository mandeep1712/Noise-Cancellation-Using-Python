from scipy.io import wavfile
import noisereduce as nr
rate, data = wavfile.read(r'E:\project\conversation.wav')
data.shape
reduced_noise = nr.reduce_noise(y=data, sr=rate)
wavfile.write(r"E:\project\conversation_denoised.wav", rate, reduced_noise)