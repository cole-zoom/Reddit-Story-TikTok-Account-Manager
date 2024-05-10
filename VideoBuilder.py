from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

gameplay = VideoFileClip("Gameplay.mp4").subclip(4,260)

generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white')

story = 'Six months ago, a family in my wife\'s (30F) and my (30M) church was leaving the state. Their son (18M), who we will call Fred, was very against the change and pushed against his family’s decision to leave. I have been a mentor to this kid since he was 16. His family left anyway and, believing that 18 year olds are adults, left him without the resources to support himself.'

c = 0
t = 0
s = ''
subs = []
for i in story:
    if i == " ":
        c += 1
        t += 1
    s += i
    if c == 3:
        subs.append(((t-3,t),s))
        s = ""
        c = 0

print(subs)

subtitles = SubtitlesClip(subs, generator)
result = CompositeVideoClip([gameplay, subtitles.set_pos(('center','bottom'))])
result.write_videofile("output.mp4", fps=gameplay.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")