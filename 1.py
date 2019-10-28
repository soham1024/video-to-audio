import moviepy.editor as mp
#import imageio
#imageio.plugins.ffmpeg.download()
for i in  range(1,6):
	name_input='myvideo'+str(i)+'.mp4'
	clip = mp.VideoFileClip(name_input)
	name_output= 'audio'+str(i)+'.mp3'
	clip.audio.write_audiofile(name_output)


