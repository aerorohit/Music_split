import soundfile as sf 
import sys
filename=sys.argv[1]
soxfile=open("split.sh",'w')
f=sf.SoundFile(filename+".wav")
print('samples = {}'.format(len(f)))
print('seconds = {}'.format(len(f) / f.samplerate))
time=len(f)/f.samplerate
x=int(time//10)
soxfile.write("mkdir "+filename+"\n")
for i in range(x):
    soxfile.write("sox "+filename+".wav "+filename+"/"+filename+"split_"+str(i)+".wav trim "+str(10*i)+" 10\n")

