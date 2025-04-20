from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
import moviepy.audio.fx.all as afx
import os

folder = "generated_videos"
bg_music_path = "bg_music.wav"

clips = [VideoFileClip(os.path.join(folder, f"video_{i}.mp4")) for i in range(15)]
final_video = concatenate_videoclips(clips, method="compose")

bg_music = AudioFileClip(bg_music_path)
bg_music_looped = afx.audio_loop(bg_music, duration=final_video.duration)

bg_music_looped = bg_music_looped.volumex(0.8)

final_video = final_video.set_audio(bg_music_looped)

final_video.write_videofile(
    "combined_video_with_music.mp4",
    fps=60,
    remove_temp=True
)
