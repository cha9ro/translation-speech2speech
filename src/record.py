import pyaudio
import wave
import speech_recognition as sr
 
RECORD_SECONDS = 5 # record duarition [s]
WAVE_OUTPUT_FILENAME = "./audio/sample.wav" # audio file name
iDeviceIndex = 0 # record device index
 
# setting
FORMAT = pyaudio.paInt16 # audio format
CHANNELS = 1             # monoral (1)
RATE = 44100             # sample rate
CHUNK = 2**11            # #data point
audio = pyaudio.PyAudio()
 
stream = audio.open(format=FORMAT, channels=CHANNELS,
        rate=RATE, input=True,
        input_device_index = iDeviceIndex, # record device index
        frames_per_buffer=CHUNK)
 
#-------------- recording start ---------------
 
print ("recording...")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
 
 
print ("finished recording")
 
#-------------- recording end ---------------
 
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

#--------------- recognition start --------------
r = sr.Recognizer()
with sr.AudioFile(WAVE_OUTPUT_FILENAME) as source:
        audio = r.record(source) # read the entire audio file